import re
import json
from itertools import chain, combinations, product

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
        "value": 'signature dish',
        "synonyms": ['signature plate', 'special dish', 'special plate', 'specialty', 'signature']
    },
    {
        "value": "area",
        "synonyms": ['location']
    },
    {
        "value": "type of food",
        "synonyms": ['kind of food', 'cuisine type', 'type of cuisine', 'kind of dishes']
    },
    {
        "value": "price",
        "synonyms": ['price range', 'pricerange', 'range of price']
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
            'entity': 'requested_phone'
        },
        'address': {
            'examples': ['address'],
            'entity': 'requested_address'
        },
        'postcode': {
            # 'examples': ['postcode', 'postal code', 'area code'],
            'examples': ['postcode'],
            'entity': 'requested_postcode'
        },
        'signature': {
            # 'examples': ['signature dish', 'signature plate', 'special dish', 'special plate', 'specialty',
            #             'signature'],
            'examples': ['signature dish', 'specialty'],
            'entity': 'requested_signature'
        },
        'name': {
            'examples': ['name'],
            'entity': 'requested_name'
        },
        'area': {
            'examples': ['area'],
            'entity': 'requested_area'
        },
        'food': {
            'examples': ['type of food'],
            'entity': 'requested_food'
        },
        'pricerange': {
            'examples': ['price'],
            'entity': 'requested_pricerange'
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


def confirm_examples(ontology_json_file='trndev/dstc2/scripts/config/ontology_dstc2.json'):
    with open(ontology_json_file) as ontology_file:
        ontology = json.load(ontology_file)['informable']
        del ontology['name']
    # food examples
    template = '{question} {food} {noun}'
    questions = ['do they serve', 'does it serve', 'do they prepare', 'do they make']
    food = ontology['food']
    nouns = ['food', 'cuisine', 'dishes']
    food_re = re.compile('|'.join(['({})'.format(ex) for ex in food]))
    for question in questions:
        for food_type in food:
            for noun in nouns:
                text = template.format(question=question, food=food_type, noun=noun)
                match = food_re.search(text)
                yield {"text": text,
                       "intent": "confirm",
                       "entities": [
                           {"start": match.start(),
                            "end": match.end(),
                            "value": food_type,  # json conversion will put the quotes
                            "entity": "food"
                            }
                       ] if match is not None else []
                       }
    # price examples
    template = '{question} {price}'
    questions = ['is it']

    template = '{question} {price} {noun}'
    questions = ['is it on the']
    #nouns =


if __name__ == '__main__':
    json_result = {"rasa_nlu_data": {"common_examples": [], "entity_synonyms": entity_synonyms}}
    # for example in request_examples():
    for example in request_examples():
        json_result["rasa_nlu_data"]["common_examples"].append(example)
    for example in confirm_examples():
        json_result["rasa_nlu_data"]["common_examples"].append(example)
    with open("test_nlu_output_confirm_request.json", "w") as nlu_output:
        json.dump(json_result, nlu_output, indent=2)
