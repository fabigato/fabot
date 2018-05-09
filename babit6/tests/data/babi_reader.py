from unittest import TestCase
from globals import BABI_T6_TRN_FILE, BABI_T6_TST_FILE, BABI_T6_DEV_FILE, BABI_T6_KB_FILE, NLU_MODEL_PATH, \
    NLU_T6_MODEL_NAME
from data.babi_reader import BabiReader
from data.babi_reader import BabiT6Reader
import re
from itertools import chain
from os.path import join


class TestBabiReader(TestCase):
    def test_all_bot_acts(self):
        bot_templates = [
            'Hello , welcome to the Cambridge restaurant system \. You can ask for restaurants by area , price range or food type \. How may I help you \?$',  # 1117
            'api_call \w+ \w+ \w+$',  # 1088
            '.+ is a nice place in the \w+ of town and the prices are \w+$',  # 574
            '(.+ is a nice place in the \w+ of town serving tasty \w+ food$)|(.+ is a nice restaurant in the \w+ of town serving \w+ food$)',  # 270
            '(.+ is a great restaurant serving \w+ \w+ food in the \w+ of town .$)|(.+ is a nice restaurant in the \w+ of town in the \w+ price range$)',  # no exact template in tst to match this trn one, semi-arbitrary choice here   71
            '.+ is a nice place in the \w+ of town$',  # 90
            '.+ serves \w+ food in the \w+ price range$',  # 268
            '(.+ serves \w+ food$)|(\w+ serves \w+ food \.$)',  # 371
            '(.+ is in the \w+ price range$)|(The price range at .+ is \w+ \.$)',  # 110
            '\w+ is in the \w+ price range , and their post code is .+$',  # 3
            'You are looking for a restaurant serving any kind of food right\?$',  # 247
            'Let me confirm , You are looking for a restaurant in the \w+ price range right\?$',  # 24
            'Let me confirm , You are looking for a restaurant and you dont care about the price range right\?$',  # 8
            ' you are welcome$',  # 1117
            '(What kind of food would you like\?$)|(Sorry would you like \w+ or \w+ food\?$)|(Sorry would you like \w+ food or you dont care)$',  # 302
            '(What part of town do you have in mind\?$)|(Sorry would you like the \w+ of town or you dont care$)|(Sorry would you like something in the \w+ or in the \w+$)|(There are restaurants \. That area would you like\?$)',  # 244
            'I\'m sorry but there is no restaurant serving \w+ food$',  # 597
            '(I am sorry but there is no other \w+ restaurant that matches your request$)|(I am sorry but there is no \w+ restaurant that matches your request$)',  # 24
            '(I am sorry but there is no other \w+ restaurant in the \w+ price range$)|(Sorry there is no \w+ restaurant in the \w+ price range$)',  # 10
            'I am sorry but there is no other \w+ restaurant in the \w+ of town$',  # 14
            'Sorry but there is no other restaurant in the \w+ price range and the \w+ of town$',  # 30
            'Sorry but there is no other \w+ restaurant in the \w+ price range and the \w+ of town$',  # 10
            '(I\'m sorry but there is no \w+ restaurant in the \w+ of town$)|(Sorry there is no \w+ restaurant in the \w+ of town$)',  # 85
            'I\'m sorry but there is no restaurant serving \w+ \w+ food$',  # 54
            '(I\'m sorry but there is no \w+ restaurant in the \w+ of town and the \w+ price range$)|(Sorry there is no \w+ restaurant in the \w+ of town serving \w+ food$)',  # 11
            '(Could you please repeat that\?$)|(Sorry I am a bit confused ; please tell me again what you are looking for \.$)|(You are looking for a restaurant is that right\?$)',  # semi-arbitrary 'looking for a restaurant' addition, but in training practice, that's how they use it  518
            'Sorry, I can\'t hear you$',  # 25
            'Did you say you are looking for a restaurant in the \w+ of town\?$',  # 116
            'There are restaurants serving \w+ in the \w+ of town \. What price range would you like\?$',  # 107
            'There are restaurants serving \w+ in the \w+ price range \. What area would you like\?$',  # 106
            'There are restaurants serving \w+ in any price range \. What area would you like\?$',  # 10
            'There are restaurants in the \w+ of town serving any kind of food \. What price range would you like\?$',  # 61
            'There are restaurants in the \w+ price range and the \w+ of town \. What type of food would you like\?$',  # 210
            'There are restaurants serving \w+ food \. What area do you want\?$',  # 164
            'There are restaurants serving \w+ food in any part of town \. What price range would you like\?$',  # 107
            'There are restaurants serving \w+ food \. What price range do you want\?$',  # 14
            'There are restaurants in the \w+ of town \. What type of food do you want\?$',  # 155
            'There are restaurants in the \w+ price range . What type of food do you want\?$',  # 184
            'There are restaurants in the \w+ price range \. What area do you want\?$',  # 1
            'There are restaurants in all parts of town \. What type of pricerange do you want\?$',  # 1
            'There are restaurants if you don\'t care about the food \. What area do you want\?$',  # 21
            'There are restaurants if you don\'t care about the food \. What price range do you want\?$',  # 1
            'There are restaurants if you don\'t care about the area or the type of food \. What price range would you like\?$',  # 15
            'There are restaurants serving any kind of food in the \w+ price range \. What area would you like\?$',  # 39
            'There are restaurants in all parts of town \. What type of food do you want\?$',  # 8
            'You are looking for a \w+ restaurant right\?$',  # 368
            '(Would you like something in the cheap , moderate , or expensive price range\?$)|(Sorry would you like something in the \w+ price range or in the \w+ price range$)|(Sorry would you like something in the \w+ price range or in the \w+ price range$)|(Sorry would you like something in the \w+ price range or you dont care$)',  # 157
            'Ok , a restaurant in any part of town is that right\?$',  # 45
            '.+ is a great restaurant$',  # 303
            'The phone number of .+ is \w+$',  # 795
            '\w+ is a great restaurant serving \w+ food \. Their phone number is .+ \.$',  # 1
            'The post code of .+ is \w+$',  # 163
            'The address of \w+ is .+ \.$',  # 3
            '(Sure , .+ is on \w+$)|(.+ is in the \w+ part of town \.$)|(\w+ is in the \w+ , at .+$)',  # This gives address     611
            '(\w+ is on \w+$)|(the good luck chinese food takeaway is on \w+$)',  # both OR clauses are seen in test data  24
            'Can I help you with anything else\?$'  # 165
        ]
        # 74 templates, minus 16 trn only = 58, just like Williams. The trn only templates should be fused with test ones or mapped to UNK, a 59th template that Williams uses and masks to 0 so it's never predicted
        bot_templates = [re.compile(pattern) for pattern in bot_templates]
        for file in [BABI_T6_TST_FILE]:
            print(file)
            outliers = 0
            for story in BabiReader.babi_dialogue_iterator(file):
                for turn in story:
                    bot_says = turn['bot']
                    matched = False
                    for template in bot_templates:
                        if template.match(bot_says):
                            matched = True
                            break
                    if not matched:
                        outliers += 1
                        print(bot_says)
            print('outliers: {}'.format(outliers))

    def test_all_user_utterances(self):
        # get all possible values for all entities
        values = {'cuisine': [], 'location': [], 'price': []}
        with open(BABI_T6_KB_FILE) as kb_fh:
            for line in kb_fh:
                matches = {'cuisine': re.search('R_cuisine (?P<value>\w+)', line),
                           'location': re.search('R_location (?P<value>\w+)', line),
                           'price': re.search('R_price (?P<value>\w+)', line)
                           }
                for slot in matches:
                    if matches[slot]:
                        values[slot].append(matches[slot].group('value'))
        # food values not in the kb, but asked by users on train data (only if the bot detected it as food type)
        values['cuisine'] += ['canapes', 'kosher', 'creative', 'caribbean', 'tuscan', 'traditional', 'austrian',
                              'swedish', 'christmas', 'australian', 'cantonese', 'irish', 'welsh', 'polynesian',
                              'romanian', 'german', 'greek', 'afghan', 'moroccan', 'belgian', 'hungarian', 'unusual',
                              'halal', 'english', 'swiss', 'world', 'vegetarian']
        for slot in values:
            values[slot] = list(set(values[slot]))
        synonyms = {slot: {value: [] for value in values[slot]} for slot in values}
        synonyms['location']['centre'] = ['center']
        synonyms['cuisine']['north_american'] = ['american']
        synonyms['price']['moderate'] = ['moderately']
        all_values = {entity: sorted(values[entity] + list(chain(*[synonyms[entity][syn]
                                                                   for syn in synonyms[entity]])), reverse=True)
                      for entity in values}
        human_templates = {
            'silence': [
                '<SILENCE>'
            ],
            'inform': [  # will take anything that mentions an entity, should be checked only after request_food etc
                # with the 3 entities
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine location price
                         for entity in ['cuisine', 'location', 'price']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine price location
                         for entity in ['cuisine', 'price', 'location']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location cuisine price
                         for entity in ['location', 'cuisine', 'price']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location price cuisine
                         for entity in ['location', 'price', 'cuisine']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price cuisine location
                         for entity in ['price', 'cuisine', 'location']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price location cuisine
                         for entity in ['price', 'location', 'cuisine']]) + '.*',
                # with 2 entities
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine location
                         for entity in ['cuisine', 'location']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location cuisine
                         for entity in ['location', 'cuisine']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine price
                         for entity in ['cuisine', 'price']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price cuisine
                         for entity in ['price', 'cuisine']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price location
                         for entity in ['price', 'location']]) + '.*',
                ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location price
                         for entity in ['location', 'price']]) + '.*',
                # with 1 entity
                '.*(?P<cuisine>(' + '|'.join(all_values['cuisine']) + ')).*',            # cuisine
                '.*(?P<location>(' + '|'.join(all_values['location']) + ')).*',          # location
                '.*(?P<price>(' + '|'.join(all_values['price']) + ')).*',                 # price

                # not prividing any entities, still inform (only after the previous ones where discarded):
                'find a restaurant'
                # '.*(' + '|'.join(['(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'
                # for entity in all_values]) + ')+.*'
            ],
            'bye': [
                '\s*(good)?bye\s*'
            ],
            'dontcare': [
                'dont care',
                'it doesnt matter',
                '^any (part|area)',
                '^any price range$',
                '^doesnt matter$',
                '^any$',
                '^anything$',
                '^any kind$'
            ],
            'reqalts': [
                'anything else',
                'give me a different restaurant',
                '^what else$',
                'other (restaurant|choice)'
            ],
            'request_phone': [
                'what is the phone number',
                'phone( number)?( please)?( of the venue)?$',  # often bots answer only last request in a sentence
                # 'phone number and ((the )?area)|((the )?price range)'
                'phone number and (?!address)'
            ],
            'request_address': [
                'what is the address',
                'address( of the venue)?( please)?( there)?$',
                'where is it$',
                'address and the price range',
                'address and (the )?(?!phone)'
            ],
            'request_postcode': [
                'post ?code( of the venue)?( please)?$',
                'postal code$'
            ],
            'request_food': [
                '(type|kind) of food (do they)|(does it)',
                '^what type of food is it$',
                '^what type of food( does it serve)?$',
                '^(what is the )?type of food$'
            ],
            'request_location': [
                '^what is the area$',
                '^area$',
                '^what area$',
                '^and the area$',
                '^and what area of town is it in$',
                '^what area is it in$',
                'what part of town'
            ],
            'request_price': [
                'whats the price',
                'what is the price',
                'whats its price range',
                'the price range( of the venue)?$',
                '^price range$'
            ],
            'affirm': [
                '^yes$'
            ],
            'negate': [
                '^no$'
            ]
        }
        human_templates = {intent: [re.compile(pattern) for pattern in human_templates[intent]]
                           for intent in human_templates}
        intent_priority = [
            'silence',
            'dontcare',
            'bye',
            'reqalts',
            'request_phone',
            'request_address',
            'request_postcode',
            'request_food',
            'request_location',
            'request_price',
            'inform',
            'affirm',
            'negate'
        ]
        examples = {intent: {} for intent in human_templates}  # indexed by intent and then by text, so we don't repeat

        def parse_example(text, act, regex):
            def check_if_synonym(value, entity):
                if value in values[entity]:
                    return value
                else:
                    for candidate_value in synonyms[entity]:
                        if value in synonyms[entity][candidate_value]:
                            return candidate_value
                    raise Exception('unknown value for entity {}: {}'.format(entity, value))

            return {'text': text, 'intent': act,
                    'entities': [{'start': regex.span(entity)[0], 'end': regex.span(entity)[1],
                                  'value': check_if_synonym(regex.group(entity), entity), 'entity': entity}
                                 for entity in regex.groupdict()]
                    }
        for file in [BABI_T6_TRN_FILE, BABI_T6_DEV_FILE]:
            print(file)
            outliers = 0
            for story in BabiReader.babi_dialogue_iterator(file):
                for turn in story:
                    human_says = turn['human']
                    matched = False
                    for intent in intent_priority:
                        for template in human_templates[intent]:
                            match = template.search(human_says)
                            if match:
                                matched = True
                                examples[intent][human_says] = parse_example(human_says, intent, match)
                                break
                        if matched:  # no need to try further intents if we had a match already
                            break
                    if not matched:
                        outliers += 1
                        print('human: {}\t (bot: {})'.format(human_says, turn['bot']))
            print('outliers: {}'.format(outliers))
        examples = [examples[intent][text] for intent in examples for text in examples[intent]]
        print('done')

    def test_produce_nlu_rasa_t6_file(self):
        reader = BabiT6Reader(join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME), BABI_T6_KB_FILE)
        examples, synonyms, regex_features, unparsable = reader.extract_rasa_nlu_training_examples(BABI_T6_TRN_FILE)
        reader.produce_rasa_nlu_training_file(examples, 'tests/data/nlu_trn_t6.json', synonyms, regex_features)
        with open('tests/data/nlu_trn_t6_unparsable.txt', "w") as unparsable_fh:
            for h, r in unparsable:
                unparsable_fh.write('user: {}\t (bot: {})\n'.format(h, r))


