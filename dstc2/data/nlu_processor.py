import re
import json
from itertools import chain, combinations, product
from string import Formatter

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
    }
]

regex_features = [
    {

    }
]

def _add_intent(examples, intent):
    for e in examples:
        e["intent"] = intent


def _powerset(l):
    """returns the powerset of an iterable, minus the empty set"""
    return list(chain.from_iterable(combinations(l, r) for r in range(1, len(l) + 1)))


def request_examples():
    """
    Generates examples of request utterances, considering all combinations of requests from the 8 requestable slots in
    the DSTC2 domain, using several example sentence structures for each combination
    :return:
    """
    def concatenate_options(text, options):
        """
        generates concatenations of requestables in a single sentence, taking care of commas and the 'and' word where
        appropriate
        :param text: initial text, the concatenated options will be appended to it (assumes no trailing space in text)
        :param options: list of requestables (strings) to concatenate. E.g. options = ['address', 'phone', 'specialty']
        would yield concatenations like 'address, phone and specialty', 'address and phone', 'phone and specialty, etc
        :return: every time, a possible concatenation from all the combinations in the power set of options
        """
        for subset in _powerset(options):
            concatenated = text + " {option0}"
            if len(subset) > 1:
                for i in range(1, len(subset)-1):
                    concatenated += ", {option" + str(i) + "}"
                concatenated += " and {option" + str(len(subset)-1) + "}"
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
    #questions = ['can you give me']
    template = '{question} the'
    for combination in product(*[requestables[requestable]['examples'] for requestable in requestables]):  # 4200...
        for concatenated_template, subset in concatenate_options(template, combination):  # all possible combinations
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


def confirm_examples(food_types, prices, areas):
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


def inform_examples(food_types, priceranges, areas):
    text = 'i want a restaurant'
    # area indicators
    area_template = '{area_preposition} {area} {area_noun}'
    area_prepositions = ['in the', 'near the']
    area_nouns = ['area', 'region', '']


if __name__ == '__main__':
    json_result = {"rasa_nlu_data": {"common_examples": [], "entity_synonyms": entity_synonyms}}
    with open('trndev/dstc2/scripts/config/ontology_dstc2.json') as ontology_file:
        ontology = json.load(ontology_file)['informable']
    food_types, priceranges, areas = ontology['food'], ontology['pricerange'], ontology['area']
    # for example in request_examples():
    #    json_result["rasa_nlu_data"]["common_examples"].append(example)
    for example in confirm_examples(food_types=food_types, prices=priceranges, areas=areas):
        json_result["rasa_nlu_data"]["common_examples"].append(example)
    with open("test_nlu_output_confirm_request.json", "w") as nlu_output:
        json.dump(json_result, nlu_output, indent=2)
