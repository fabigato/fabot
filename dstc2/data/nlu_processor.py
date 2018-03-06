import re
import json
from itertools import chain, combinations, product
from string import Formatter
from numpy import random

random.seed(42)

entity_synonyms = [
    {
         "value": "moderate",  # moderate value of the pricerange entity
         "synonyms": ["affordable", "not too expensive"]
    },
    {
        "value": "phone",
        "synonyms": ['telephone number', 'telephone', 'phone number', 'number']
    },
    {
        "value": "postcode",
        "synonyms": ['postal code', 'area code']
    },
    {
        "value": 'signature',
        "synonyms": ['signature plate', 'special dish', 'special plate', 'specialty', 'signature dish']
    },
    {
        "value": "area",
        "synonyms": ['location']
    },
    {
        "value": "food",
        "synonyms": ['kind of food', 'cuisine type', 'type of cuisine', 'kind of dishes', "type of food"]
    },
    {
        "value": "pricerange",
        "synonyms": ['price range', 'price', 'range of price']
    },
    {
        "value": "middle eastern",
        "synonyms": ['middle-eastern', 'middleeastern']
    },
    {
        "value": "centre",
        "synonyms": ["center"]
    },
    {
        "value": "dontcare",
        "synonyms": ["dont care", "don't care", "do not care", "does not matter", "doesnt matter", "doesn't matter",
                     "not important"]
    }
]

# remember: this is just an extra feature to help the CRF and intent classifier do their thing. The regex are
# applied to each user input and if matching, the corresponding flag is set. If many "give me the zipcode"
# intents have the same zipcode flag on, the classifier will profit from it
regex_features = [
    {
        "name": "dontcare",  # just a human readable name, has no effect on behavior
        "pattern": "dontcare|dont care|doesn't matter|does not matter|don't care|dont care"
    },
    {
        "name": "inform",
        "pattern": "find \w+ restaurant"
    },
    {
        "name": "confirm_food",
        "pattern": "(do|does) (they|it) (serve|prepare|have|make)"
    },
    {
        "name": "bye",
        "pattern": "bye|see you|goodbye|see ya|cya|ciao"
    }
]


def _add_intent(examples, intent):
    for e in examples:
        e["intent"] = intent


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


def generate_inform_dontcare_examples(food_types, priceranges, areas):
    """
    Generates example sentences of the inform_dontcare da in rasa json format, sampling sentence constructions from a
    template and randomly choosing combinations of provided informable values
    :param food_types: list of food types. Generated examples will use all values in this list
    :param priceranges: list of price ranges. Generated examples will use all values in this list
    :param areas: list of areas. Generated examples will use all values in this list
    :return: an example in rasa json format:
    {"text": str, "intent": "inform", entities: [{"start": int, "end": int, "value": str, "entity": str}]}
    """
    pattern = re.compile(next(rf for rf in regex_features if rf['name'] == 'dontcare')['pattern'])
    dontcare_texts = pattern.pattern.split('|')
    yield {"text": "i dont care",
           "intent": "inform_dontcare",
           "entities": []
           }
    things_you_dont_care_about = {'pricerange': ['price range', 'price'], 'area': ['area', 'location'],
                                  'food': ['food type', 'food']}
    for dontcare_informable in things_you_dont_care_about:
        for dontcare_value in things_you_dont_care_about['dontcare_informable']:
            text = 'i dont care about the ' + dontcare_value
            match = pattern.search(text)
            yield {"text": "i dont care",
                   "intent": "inform_dontcare",
                   "entities": [
                       {"start": match.start(),
                        "end": match.end(),
                        "value": 'dontcare',
                        "entity": dontcare_informable
                        }
                   ] if match is not None else []
                   }


def generate_bye_examples():
    # TODO include bye examples with "No thanks", "No", "thanks", etc
    bye_texts = next(rf for rf in regex_features if rf['name'] == 'bye')['pattern'].split('|')
    for bye_text in bye_texts:
        yield {"text": bye_text,
               "intent": "bye",
               "entities": []
               }


if __name__ == '__main__':
    json_result = {"rasa_nlu_data": {"common_examples": [], "entity_synonyms": entity_synonyms}}
    with open('trndev/dstc2/scripts/config/ontology_dstc2.json') as ontology_file:
        ontology = json.load(ontology_file)['informable']
    food_types, priceranges, areas = ontology['food'], ontology['pricerange'], ontology['area']
    inform_examples = []
    for example in generate_inform_examples(food_types, priceranges, areas):
        inform_examples.append(example)
    # since examples are sampled, remove duplicates. This looks dirty AF but believe me, I see no better way
    # and I know what you're thinking: no, changing the code so as to never generate duplicates would be worse
    json_result["rasa_nlu_data"]["common_examples"] += list({tmp["text"]: tmp for tmp in inform_examples}.values())
    for example in generate_request_examples():
        json_result["rasa_nlu_data"]["common_examples"].append(example)
    for example in generate_confirm_examples(food_types=food_types, prices=priceranges, areas=areas):
        json_result["rasa_nlu_data"]["common_examples"].append(example)
    for example in generate_bye_examples():
        json_result["rasa_nlu_data"]["common_examples"].append(example)
    with open("test_nlu_output_confirm_request.json", "w") as nlu_output:
        json.dump(json_result, nlu_output, indent=2)
