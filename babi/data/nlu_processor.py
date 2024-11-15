import re
import json
from itertools import chain, combinations, product
from string import Formatter
from numpy import random
from collections import defaultdict
import logging
from data.dialogue_processor import REQUESTED_ENTITY_FLAG, process_dstc2_files, get_user_intent
from globals import DSTC2_TRN_DEV_DATA_PATH, RASA_TRAIN_PATH, RASA_TST_PATH, DSTC2_TST_DATA_PATH, DSTC2_ONTOLOGY_FILE

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


def _text_is_troublesome(text):
    """Checks if text is bad for training, for a variety of reasons"""
    # these sentences make rasa create spurious synonyms
    troublesome_sentences = [
        'chinese food im looking for sea food',  # this made chinese a synonym of seafood
        'no not indian scandinavian food',  # scandinavian -> indian
        'i am looking for kitalian food',  # italian -> catalan
        'i dont give a damn about chinese food i want thai food',  # chinese -> thai
        'i dont give a fuck if hk fusion serves chinese food im looking for thai food',
        'not chinese food thai food',  # chinese -> thai
        'north east',  # north -> east
        'was that in the east part of town west part of town',  # east -> west
        'ok if there is no restaurant serving indonesian food how about a '
        'restaurant serving chinese food',  # indonesian -> chinese
        'not european fusion',  # european -> fusion
        'id like a restaurant that serves australian asian food',  # australian asian -> australian
        'im looking for a restaurant in any area and it should serve pan asian food'  # panasian -> asian oriental
    ]
    # we don't want unintelligible text. Plus, only 32 instances in tst, 47 in trn/dev
    return text.find('noise') != -1 or text in troublesome_sentences


class NLUExampleGenerator(object):

    def __init__(self, ontology_file, random_seed=None):
        if random_seed is not None:
            random.seed(random_seed)
        with open(ontology_file) as ontology_handler:
            ontology = json.load(ontology_handler)['informable']
        food_types, priceranges, areas, names = ontology['food'], ontology['pricerange'], \
                                                                    ontology['area'], ontology['name']
        self._requestables = {  # maps each requestable to a list of synonyms and an informable flag
            'address': {'syn_hints': ['address'],
                        'informable': False},
            'area': {'syn_hints': ['location', 'part of town', 'located', 'area', 'part'],
                     'informable': True, 'values': areas},
            'food': {'syn_hints': ['kind of food', 'cuisine type', 'type of cuisine', 'kind of dishes', 'type of food',
                                   'food'],
                     'informable': True, 'values': food_types},
            'phone': {'syn_hints': ['telephone number', 'telephone', 'phone number', 'number', 'phone'],
                      'informable': False},
            'pricerange': {'syn_hints': ['price range', 'price', 'range of price', 'cost', 'pricerange'],
                           'informable': True, 'values': priceranges},
            'postcode': {'syn_hints': ['postal code', 'area code', 'post code', 'postcode'],
                         'informable': False},
            'signature': {'syn_hints': ['signature plate', 'special dish', 'special plate', 'specialty',
                                        'signature dish', 'specialized'],
                          'informable': False},
            'name': {'syn_hints': ['called', 'name'],
                     'informable': True, 'values': names}
        }
        # add the dontcare option to all informables
        for r in self._requestables:
            if self._requestables[r]['informable'] == True:
                self._requestables[r]['values'].append('dontcare')

        self._entity_synonyms = [
            {
                "value": REQUESTED_ENTITY_FLAG,
                "synonyms": [synonym for v in self._requestables.values() for synonym in v['syn_hints']],
                "entity": "any"
            },
            {
                "value": "moderate",  # moderate value of the pricerange entity
                "synonyms": ["affordable", "not too expensive", "moderately"],
                "entity": "pricerange"  # this is not rasa NLU json field, added for own convenience, will be removed
            },
            {
                "value": "expensive",  # moderate value of the pricerange entity
                "synonyms": ["high priced"],
                "entity": "pricerange"  # this is not rasa NLU json field, added for own convenience, will be removed
            },
            {
                "value": "middle eastern",
                "synonyms": ['middle-eastern', 'middleeastern'],
                "entity": "food"
            },
            {
                "value": "seafood",
                "synonyms": ['sea food'],
                "entity": "food"
            },
            {
                "value": "centre",
                "synonyms": ["center"],
                "entity": "area"
            },
            {
                "value": "dontcare",
                "synonyms": ["dont care", "don't care", "do not care", "does not matter", "doesnt matter",
                             "doesn't matter", "not important", 'anywhere', 'any', 'dont mind'],
                "entity": "any"
            },
            {
                "value": "north american",
                "synonyms": ['american', 'USA', 'US'],
                "entity": "food"
            },
            {
                "value": "belgian",
                "synonyms": ['belgium'],
                "entity": "food"
            },
            {
                "value": "barbeque",
                "synonyms": ['barbecue'],
                "entity": "food"
            },
            {
                "value": "panasian",
                "synonyms": ['pan asian'],
                "entity": "food"
            },
            {
                "value": "steakhouse",
                "synonyms": ['steak house'],
                "entity": "food"
            },
            {
                "value": "australasian",
                "synonyms": ['australian asian'],
                "entity": "food"
            }
        ]

        # remember: this is just an extra feature to help the CRF and intent classifier do their thing. The regex are
        # applied to each user input and if matching, the corresponding flag is set. If many "give me the zipcode"
        # intents have the same zipcode flag on, the classifier will profit from it
        # the entity synonyms will also be appended to the patterns later
        regex_features = [
            # intents
            {
                "name": "inform",  # just a human readable name, has no effect on behavior
                "pattern": "find \w+ restaurant"
            },
            {
                "name": "confirm_food",
                "pattern": "(do|does) (they|it) (serve|prepare|have|make)"
            },
            {
                "name": "bye",
                "pattern": "bye|see you|goodbye|see ya|cya|ciao"
            },
            # now requested entities. Just meant to recognize the presence of it, not its boundaries
            {
                "name": "area",
                "pattern": "where is it( located)?"
            },
            {
                "name": "pricerange",
                "pattern": "how much|what is the cost"
            },
            {
                "name": "food",
                "pattern": "(serves what)|(what does (\w+ )+serve)"
            },
            {
                "name": "name",
                "pattern": "what is the name.*|how is it called.*|name of the.*"
            },
            {
                "name": "address",
                "pattern": ""
            },
            {
                "name": "phone",
                "pattern": ""
            },
            {
                "name": "postcode",
                "pattern": ""
            },
            {
                "name": "signature",
                "pattern": ""
            }
        ]
        # include requested entity synonyms as regex patterns
        for requestable in self._requestables:
            reg_feat = next(feat for feat in regex_features if feat['name'] == requestable)
            prefix = '' if reg_feat['pattern'] == '' else '|'  # append the regex or only if necessary
            reg_feat['pattern'] += prefix + '|'.join(self._requestables[requestable]['syn_hints'])

        # include informed entity synonyms as regex patterns
        # for each informable (i.e. food, area, pricerange)
        #   for each value (e.g. chinese, north american)
        #       gather synonyms
        #       build regex with value or synonyms
        #       include pattern under new regex, with name 'informed_' + value
        for inf, data in [(k, v) for k, v in self._requestables.items() if v['informable']]:  # (food, area, price)
            for value in data['values']:
                patterns = [value]
                syns = [s for s in self._entity_synonyms if s['value'] == value]
                if syns:
                    patterns += syns[0]['synonyms']
                regex_features.append({'name': 'informed_' + value, 'pattern': '|'.join(patterns)})

        self.nlu_json = {"rasa_nlu_data": {"common_examples": [], "entity_synonyms": [{"value": syn["value"],
                                                                                       "synonyms": syn["synonyms"]}
                                                                                      for syn in self._entity_synonyms],
                                           "regex_features": regex_features}}

    def generate_dstc2_examples(self, **kwargs):
        """
        processes dstc2 dialogues, converting each utterance to rasa json format
        :param kwargs: arguments passed to data.dialogue_processor.process_dstc2_files. Do not send the 'process'
        argument since this function does it
        :return: examples, failed_examples. Examples is a list of dictionaries, each being an NLU example compatible
        with rasa json format. failed_examples is a dictionary that maps a list of failed examples to their intents.
        Each file example is a dictionary with keys 'text' (the raw utterance) and 'semantics' (the utterance semantics
        as captured in dstc2 log_turn['semantics']['json']
        """
        examples = []
        failed_examples = defaultdict(list)
        dstc2fabot_entity_map = lambda x: 'address' if x == 'addr' else x

        # regex for requested entities
        requested_entity_res = {requestable: '|'.join(self._requestables[requestable]['syn_hints'])
                                for requestable in self._requestables}
        # extra custom regex
        requested_entity_res['pricerange'] = '|'.join([requested_entity_res['pricerange'], 'how much$'])
        requested_entity_res['area'] = '|'.join([requested_entity_res['area'], '(?<=where is )it|where$'])

        # sort or patterns from longest to shortest
        for requestable in requested_entity_res:
            requested_entity_res[requestable] = '|'.join(
                sorted(requested_entity_res[requestable].split('|'), key=lambda i: -len(i)))

        # compile regex
        for requestable in requested_entity_res:
            requested_entity_res[requestable] = re.compile(requested_entity_res[requestable])

        # regex for informed entities
        informed_entity_res = {informable: '|'.join(self._requestables[informable]['values'] + ['australian asian'])
                               for informable in self._requestables
                               if self._requestables[informable]['informable'] == True}

        # add extra values for informables
        for entity in informed_entity_res:
            for syn in self._entity_synonyms:
                if syn['entity'] == entity:
                    informed_entity_res[entity] = '|'.join([informed_entity_res[entity]] + syn['synonyms'])

        # sort or patterns from longest to shortest
        for informable in informed_entity_res:
            informed_entity_res[informable] = '|'.join(sorted(informed_entity_res[informable].split('|'), key=lambda i: -len(i)))

        # compile regex
        for informable in informed_entity_res:
            informed_entity_res[informable] = re.compile(informed_entity_res[informable])

        # dontcare regex
        # add the dontcare value option for all informables
        dontcare_values = next(syn for syn in self.nlu_json['rasa_nlu_data']['entity_synonyms']
                               if syn['value'] == 'dontcare')['synonyms'] + ['dontcare']
        dontcare_re = re.compile('|'.join(sorted(dontcare_values, key=lambda i: -len(i))))

        def collect_nlu_example(human, bot, **kwargs):
            """I just wanted to say that I'm baffled by python's flexibility, by allowing me to pass this function as an
            argument to a function in a different module, yet preserving its namespace so that it could access objects
            defined here only"""
            for bot_turn, human_turn in zip(bot['turns'], human['turns']):
                curated_human_semantics = get_user_intent(human_turn['semantics']['json'])
                # bot_da = get_bot_da(bot_turn['output']['dialog-acts'])
                if isinstance(curated_human_semantics, dict):
                    text = human_turn['transcription']
                    curated_act = curated_human_semantics['act']
                    if _text_is_troublesome(text):
                        failed_examples[curated_act].append(
                            {'text': text, 'semantics': human_turn['semantics']['json']})
                        continue
                    if curated_act in ['request', 'inform', 'inform_dontcare', 'correct', 'confirm', 'query',
                                       'include_filter', 'deny']:  # look for entities
                        entities = []
                        for i, act_semantics in enumerate(human_turn['semantics']['json']):
                            for slot in act_semantics['slots']:  # there's always one slot per act, but cycle won't hurt
                                if act_semantics['act'] == 'request':
                                    entity = dstc2fabot_entity_map(slot[1])
                                    if entity == 'this':
                                        if len(human_turn['semantics']['json']) > 1:  # if there are other entities
                                            continue  # just this regard this entity
                                        else:
                                            # this sentences are usually 'i dont care', so no way to infer the entity
                                            logger.warning('"this" value found, ignoring entity')
                                            break
                                    match = requested_entity_res[entity].search(text)
                                    if match is None:
                                        logger.warning('couldn\'t find match for "{}", while looking for entity {}'.
                                                       format(text, entity))
                                        failed_examples[curated_act].append(
                                            {'text': text, 'semantics': human_turn['semantics']['json']})
                                    else:
                                        entities.append({'start': match.start(), 'end': match.end(),
                                                         'value': REQUESTED_ENTITY_FLAG, 'entity': entity})
                                else:
                                    entity = dstc2fabot_entity_map(slot[0])
                                    if entity == 'this':
                                        if len(human_turn['semantics']['json']) > 1:  # if there are other entities
                                            continue  # just this regard this entity
                                        else:
                                            # this sentences are usually 'i dont care', so no way to infer the entity
                                            logger.warning('"this" value found, ignoring entity')
                                            break
                                    raw_value = slot[1]
                                    if raw_value not in self._requestables[entity]['values']:
                                        # look if available in synonyms
                                        available = False  # synonym found flag
                                        for syn in [s for s in self._entity_synonyms if s['entity'] in [entity, 'any']]:
                                            if raw_value in syn['synonyms']:
                                                # all good
                                                available = True
                                                break
                                        if available:
                                            match = informed_entity_res[entity].search(text)
                                            if match is not None:
                                                entities.append({'start': match.start(), 'end': match.end(),
                                                                 'value': raw_value, 'entity': entity})
                                            else:
                                                logger.warning(
                                                    'couldn\'t find match for "{}", while looking for entity {}'.format(
                                                        text, entity))
                                                failed_examples[curated_act].append(
                                                    {'text': text, 'semantics': human_turn['semantics']['json']})
                                        else:
                                            logger.warning('unknown value "{}" found for entity {}, in sentence: {} '.
                                                format(raw_value, entity, text))
                                    else:
                                        if raw_value == 'dontcare':
                                            # check if there was any entity before with value dontcare: you dont want to
                                            # get that previous dontcare, you want the next: e.g. 'any area any price'
                                            look_from = 0
                                            if i > 0 and 'dontcare' in [e['value'] for e in entities]:
                                                look_from = int(next(e['end'] for e in entities
                                                                     if e['value'] == 'dontcare'))
                                            match = dontcare_re.search('x'*look_from + text[look_from:])
                                            # from last match onwards. I'm literally replacing the previously matched
                                            # part of the string with xs, that's how dirty this is!
                                        else:
                                            match = informed_entity_res[entity].search(text)
                                        if match is not None:
                                            entities.append({'start': match.start(), 'end': match.end(),
                                                             'value': raw_value, 'entity': entity})
                                        else:
                                            logger.warning(
                                                'couldn\'t find match for "{}", while looking for entity {}'.format(
                                                    text, entity))
                                            failed_examples[curated_act].append(
                                                {'text': text, 'semantics': human_turn['semantics']['json']})
                        if len(entities) == 0:
                            failed_examples[curated_act].append({'text': text,
                                                                 'semantics': human_turn['semantics']['json']})
                        else:
                            examples.append({'text': text, 'intent': curated_act, 'entities': entities})
                    else:  # other acts, with no entities. We just do basic checks
                        if text.find('noise') != -1:
                            failed_examples[curated_act].append(
                                {'text': text, 'semantics': human_turn['semantics']['json']})
                            continue
                        examples.append({'text': text, 'intent': curated_act, 'entities': []})

        process_dstc2_files(process=collect_nlu_example, **kwargs)
        self.nlu_json["rasa_nlu_data"]["common_examples"] = examples
        return self.nlu_json, failed_examples


def _powerset(l):
    """returns the powerset of an iterable, minus the empty set"""
    return list(chain.from_iterable(combinations(l, r) for r in range(1, len(l) + 1)))


def generate_request_examples():
    """
    Generates examples of request utterances, considering all combinations of requests from the 8 requestable slots in
    the DSTC2 domain, using several example sentence structures for each combination
    :return: an example in rasa json format:
    {"text": str, "intent": "request", entities: [{"start": int, "end": int, "value": str, "entity": str}]}
    """
    def _concatenate_options(text, options):
        """
        generates concatenations of requestables in a single sentence, taking care of commas and the 'and' word where
        appropriate
        :param text: initial text, the concatenated options will be appended to it (assumes no trailing space in text)
        :param options: list of requestables (strings) to concatenate. E.g. options = ['address', 'phone', 'specialty']
        would yield concatenations like 'address, phone and specialty', 'address and phone', 'phone and specialty, etc
        :return: a generator of text=str, options_used=List[str], each representing a possible concatenation from all the
        combinations in the power set of options. The string has named format slots {option_0} ...
        {option_len(options_used)}. The values to fill those slots are in options_used
        """
        for subset in _powerset(options):
            concatenated = text + " {option0}"
            if len(subset) > 1:
                for i in range(1, len(subset) - 1):
                    concatenated += ", {option" + str(i) + "}"
                concatenated += " and {option" + str(len(subset) - 1) + "}"
            yield concatenated, subset
    """
    note you could put all the examples per entity in these 'examples' lists. But that would increase the amount of
    examples by factorial order (leading to a GBs big NLU training data file). Instead, we just give one example and
    leverage rasa's synonyms feature to provide all the different ways in which you could refer to a phone number
    """
    requestables = {
        'phone': {
            # 'examples': ['telephone number', 'telephone', 'phone number', 'phone', 'number'],
            'examples': ['phone'],
            # very important that longer examples come before shorter (subsumed) ones, since re | operator is not greedy
            'entity': 'phone'
        },
        'address': {
            'examples': ['address'],
            'entity': 'address'
        },
        'postcode': {
            # 'examples': ['postcode', 'postal code', 'area code'],
            'examples': ['postcode'],
            'entity': 'postcode'
        },
        'signature': {
            # 'examples': ['signature dish', 'signature plate', 'special dish', 'special plate', 'specialty',
            #             'signature'],
            'examples': ['signature dish'],
            'entity': 'signature'
        },
        'name': {
            'examples': ['name'],
            'entity': 'name'
        },
        'area': {
            'examples': ['area'],
            'entity': 'area'
        },
        'food': {
            'examples': ['type of food', 'kind of food'],
            'entity': 'food'
        },
        'pricerange': {
            'examples': ['price'],
            'entity': 'pricerange'
        }
    }  # 4200 possible combinations of examples from all these lists
    for key in requestables:  # build the regex: (telephone number)|(telephone)|...
        requestables[key]['re'] = re.compile('|'.join(['({})'.format(ex) for ex in requestables[key]['examples']]))
    questions = ['what is', 'can you give me', 'please tell me what is', 'please give me',
                 'can you please tell me what is', 'can you please give me']
    # questions = ['can you give me']
    template = '{question} the'
    for combination in product(*[requestables[requestable]['examples'] for requestable in requestables]):  # 4200...
        for concatenated_template, subset in _concatenate_options(template, combination):  # all possible combinations
            for question in questions:  # 6 ways to ask
                options = {'option'+str(i): requestable for i, requestable in enumerate(subset)}
                text = concatenated_template.format(question=question, **options)
                yield {"text": text,
                       "intent": "request",
                       "entities": [
                           {"start": requestables[other_requestable]['re'].search(text).start(),
                            "end": requestables[other_requestable]['re'].search(text).end(),
                            "value": other_requestable,
                            "entity": requestables[other_requestable]['entity']
                            }
                           for other_requestable in requestables
                           if requestables[other_requestable]['re'].search(text) is not None
                       ]
                       }


def _generate_examples_with_entity(template, parts, value_index, intent):
    """
    Rasa NLU common example generator, based on a templated sentence, with 1 entity
    :param template: string with the structure of the generated sentences. It can have n format slots between {}. E.g.
    '{question} {type_of_food} {noun}' so later it can be formatted with format(question='do they have',
    type_of_food='south african', noun='food'. The slots can be anonymous (i.e. {}) or have names (e.g. {type_of_food}
    but the usual rules of named parameters apply, i.e. there can't be anonymous slots after named slots
    :param parts: list of n lists. parts[i] has all the options to fill in the ith slot in template. In the example
    above, a possible parts could be [['do they have', 'do they serve'], ['south african', 'colombian'],
    ['food', 'dishes', 'cuisine']], so a total 2x2x3 sentences can be produced
    :param value_index: integer, index of the list in parts that contains the entity values. In the example above,
    value_index = 1 since parts[1] is the list with food types, which is the entity
    :param intent: string, label of the intents generated
    :return: an example in rasa json format:
    {"text": str, "intent": str, entities: [{"start": int, "end": int, "value": str, "entity": str}]}
    """
    formatter = Formatter()
    pattern = re.compile('|'.join(['({})'.format(ex) for ex in parts[value_index]]))
    for combination in product(*parts):  # for each combination taking one value of each template part in parts
        fields = [p[1] for p in formatter.parse(template)]  # the items inside {} in the template
        format_dic = {key: value for key, value in zip(fields, combination)}
        text = template.format(**format_dic)
        match = pattern.search(text)
        yield {"text": text,
               "intent": intent,
               "entities": [
                   {"start": match.start(),
                    "end": match.end(),
                    "value": text[match.start():match.end()],  # json conversion will put the quotes
                    "entity": "food"
                    }
               ] if match is not None else []
               }


def generate_confirm_examples(food_types, prices, areas):
    """
    Generates examples of the confirm intent, each with one entity being confirmed
    :param food_types: list of food types to use in the examples
    :param prices: list of price ranges to use in the examples
    :param areas: list of areas to use in the examples
    :return: an example in rasa json format:
    {"text": str, "intent": "confirm", entities: [{"start": int, "end": int, "value": str, "entity": str}]}
    """
    intent = 'confirm'
    # food examples
    template = '{question} {food} {noun}'
    questions = ['do they serve', 'does it serve', 'do they prepare', 'do they make']
    nouns = ['food', 'cuisine', 'dishes']
    for example in _generate_examples_with_entity(template=template, parts=[questions, food_types, nouns], value_index=1,
                                                  intent=intent):
        yield example
    # price examples 1
    template = '{question} {price}'
    questions = ['is it', 'is that']
    for example in _generate_examples_with_entity(template=template, parts=[questions, prices], value_index=1,
                                                  intent=intent):
        yield example
    # price examples 2
    template = '{question} {price} range'
    questions = ['is it on the', 'is that on the']
    for example in _generate_examples_with_entity(template=template, parts=[questions, prices], value_index=1,
                                                  intent=intent):
        yield example
    # no request(name) examples seen in training or dev data
    # area examples
    template = '{question} {area}'
    questions = ['is it located at the', 'is it at the', 'is it in the', 'is it located in the']
    for example in _generate_examples_with_entity(template=template, parts=[questions, areas], value_index=1,
                                                  intent=intent):
        yield example


def generate_inform_examples(food_types, priceranges, areas):
    """
    Generates example sentences of the inform da in rasa json format, sampling sentence constructions from a template
    and randomly choosing combinations of provided informable values
    :param food_types: list of food types. Generated examples will use all values in this list
    :param priceranges: list of price ranges. Generated examples will use all values in this list
    :param areas: list of areas. Generated examples will use all values in this list
    :return: an example in rasa json format:
    {"text": str, "intent": "inform", entities: [{"start": int, "end": int, "value": str, "entity": str}]}
    """
    intro_texts = ['i want a restaurant', 'please find me a restaurant', 'i would like a restaurant',
                   'can you please find me a place']
    # area indicators
    area_template = '{area_intro} {area} {area_noun}'
    area_intros = ['in the', 'near the', 'located in the']
    area_nouns = ['area', 'region', '']

    price_template = 'in the {price} range'

    # food type indicators
    food_template = '{food_intro} {food} {food_noun}'
    food_intros = ['that serves', 'that prepares', 'that makes']
    food_nouns = ['food', 'dishes']

    patterns = {'food': re.compile('|'.join(['({})'.format(ex) for ex in food_types])),
                'pricerange': re.compile('|'.join(['({})'.format(ex) for ex in priceranges])),
                'area': re.compile('|'.join(['({})'.format(ex) for ex in areas]))}

    # for inform_combination in product(list(product(area_intros, areas, area_nouns)),
    #                                   priceranges,
    #                                   list(product(food_intros, food_types, food_nouns))):
    for inform_combination in product(areas, priceranges, food_types):
        area_text = area_template.format(area_intro=random.choice(area_intros), area=inform_combination[0],
                                         area_noun=random.choice(area_nouns))
        price_text = price_template.format(price=inform_combination[1])
        food_text = food_template.format(food_intro=random.choice(food_intros), food=inform_combination[2],
                                         food_noun=random.choice(food_nouns))
        subsets = _powerset(random.permutation([area_text, price_text, food_text]))
        for subset in random.choice(subsets, size=min(len(subsets), 5)):  # take at most 5 subsets, cause of reasons
            concatenated_text = random.choice(intro_texts) + ' ' + ', '.join(subset).strip()
            entities = []
            for entity in patterns:
                match = patterns[entity].search(concatenated_text)
                if match is not None:
                    entities.append(
                        {"start": match.start(),
                         "end": match.end(),
                         "value": concatenated_text[match.start():match.end()],
                         "entity": entity
                         }
                    )
            yield {"text": concatenated_text,
                   "intent": "inform",
                   "entities": entities
                   }


if __name__ == '__main__':
    nlu_generator = NLUExampleGenerator(ontology_file=DSTC2_ONTOLOGY_FILE, random_seed=42)
    nlu_data, failed_examples = nlu_generator.generate_dstc2_examples(path_prefix=DSTC2_TRN_DEV_DATA_PATH)
    with open(RASA_TRAIN_PATH + "dstc2_nlu_train.json", "w") as nlu_output:
         json.dump(nlu_data, nlu_output, indent=2)
    with open(RASA_TRAIN_PATH + "dstc2_nlu_train_unparsable.json", 'w') as fails:
        json.dump(failed_examples, fails, indent=2)
    nlu_data, failed_examples = nlu_generator.generate_dstc2_examples(path_prefix=DSTC2_TST_DATA_PATH)
    with open(RASA_TST_PATH + "dstc2_nlu_test.json", "w") as nlu_output:
        json.dump(nlu_data, nlu_output, indent=2)
    with open(RASA_TST_PATH + "dstc2_nlu_test_unparsable.json", 'w') as fails:
        json.dump(failed_examples, fails, indent=2)
