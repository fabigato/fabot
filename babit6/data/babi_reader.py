from copy import deepcopy
from json import dump
from os.path import isfile, splitext, join
from rasa_core.interpreter import RasaNLUInterpreter
import re
from itertools import chain
from globals import NLU_MODEL_PATH, NLU_T6_MODEL_NAME, BABI_T6_TRN_FILE, BABI_T6_DEV_FILE, BABI_T6_TST_FILE, \
    BABI_T6_KB_FILE, BABI_T5_TRN_FILE, BABI_T5_DEV_FILE, BABI_T5_TST_FILE
import logging
import argparse
from collections import Counter

logger = logging.getLogger(__name__)


class BabiReader(object):
    """
    Abstract class providing all facilities necessary to produce rasa NLU and dialog training files. It is meant to be
    inherited by subclasses specific to each bAbI task
    """

    def get_user_act(self, text):
        """
        Determines the dialog act of a bAbI t5 user utterance
        :param text: user utterance
        :return: da of the utterance (str) or None if no match found
        """
        raise NotImplementedError

    def get_bot_act(self, text):
        """
        Determines the dialog act of a bAbI t5 bot utterance
        :param text: bot utterance
        :return: da of the utterance (str) or None if no match found
        """
        raise NotImplementedError

    def extract_rasa_nlu_training_examples(self, input_filename):
        """
        Produces the contents of the 'common examples' section of the rasa format NLU training file
        :param input_filename: bAbI format conversation file
        :return: examples, synonyms, regex_features, unparsable. The examples collected, synonyms, regex features  and
        the texts that couldn't be classified. examples is a List of examples, each one is a dictionary as required by
        the rasa format (i.e. with text, intent and entities keys). synonyms is a list with the rasa format synonyms.
        regex_features is a list with the rasa format regex features. unparsable is a list of tuples, the first element
        is the unparsable text and the second element is the bot reply to that text, to provide context for further
        analysis
        """
        raise NotImplementedError

    @staticmethod
    def produce_rasa_nlu_training_file(examples, filename, synonyms=list(), regex_features=list()):
        """
        Produces the rasa nlu training file, given a list of examples in the rasa format
        :param examples: List of examples, each one a dictionary in the rasa format (i.e. with text, intent and
        entities keys)
        :param synonyms: rasa format list of synonyms
        :param regex_features: rasa format regex features
        :param filename: name of the output file, json extension is preferred
        """
        result = {"rasa_nlu_data": {"common_examples": examples,
                                    "entity_synonyms": synonyms,
                                    "regex_features": regex_features}}
        with open(filename, "w") as nlu_output_fh:
            dump(result, nlu_output_fh, indent=2)

    @property
    def bot_das(self):
        """
        :return: Iterable[str] with all the valid bot dialog acts in the domain
        """
        raise NotImplementedError

    @classmethod
    def produce_dialog_rasa_training_file(cls, input_filename, output_filename, action_prefixes=None):
        """
        Creates the rasa dialog training data file
        :param input_filename: babi format input filename to convert to rasa format
        :param output_filename: output filename
        :param action_prefixes: if provided, it must be a dictionary mapping each action name to the prefix it must have
        in the output file, useful to prepend rasa's 'utter_' prefix for template actions
        :return:
        """
        action_prefixes = {action: '' for action in cls.bot_das} if not action_prefixes else action_prefixes
        with open(output_filename, 'w') as output_fh:
            for i, story in enumerate(BabiReader.babi_dialogue_iterator(input_filename)):
                output_fh.write('## {}'.format(i) + '\n')
                for turn in story:
                    intent, entities = cls.get_user_act(turn['human'])
                    bot_says = cls.get_bot_act(turn['bot'])
                    output_fh.write('* ' + BabiReader.rasafy(intent, entities) + '\n')
                    output_fh.write(' - ' + action_prefixes[bot_says] + bot_says + '\n')
                output_fh.write('\n')

    @staticmethod
    def babi_dialogue_iterator(babi_filename):
        """
        Generator for bAbI stories. Skips api call results
        :param babi_filename: bAbI file name
        :return: list of message exchanges, as dictionaries with 'human', 'bot' pairs
        """
        story = []
        with open(babi_filename, 'r') as babi_file:
            for line in babi_file:
                if line == '\n':  # end of story
                    _story = deepcopy(story)
                    story = []
                    yield _story
                chunks = line.split('\t')
                chunks[0] = ' '.join(chunks[0].split(' ')[1:])  # rid of initial number
                if len(chunks) == 1:  # api call results, garbage
                    continue
                elif len(chunks) == 2:  # normal line
                    human, bot = chunks
                    story.append({'human': human, 'bot': bot[:-1]})  # removing final \n
                else:
                    raise Exception('Unknown formatted line: {}'.format(line))

    @staticmethod
    def rasafy(intent, entities):
        if entities:
            return intent + '{' + ', '.join(['"{}": "{}"'.format(e['entity'], e['value']) for e in entities]) + '}'
        else:
            return intent

    @staticmethod
    def vocab(filename, threshold):
        words = []
        for story in BabiReader.babi_dialogue_iterator(filename):
            for turn in story:
                words += turn['human'].split()
        words = Counter(words)
        for word in list(words):
            if words[word] < threshold:
                del words[word]
        word2id = {w: i for i, w in enumerate(list(words))}
        return word2id, {i: w for w, i in word2id.items()}


class BabiT5Reader(BabiReader):
    def __init__(self):
        self.user_das = {
            'greet': [
                '^good morning$',
                '^hello$',
                '^hi$'
            ],
            'inform': [
                '^i love (?P<cuisine>\w+) food$',
                '^(?P<location>\w+) please$',
                '^i am looking for a (?P<price>\w+) restaurant$',  # watchout: not totally sure only price can go there
                '^(i\'d like to book a table|may i have a table|instead could it be|actually i would prefer|'
                'can you make a restaurant reservation|can you book a table)?'
                '(( ?with (?P<cuisine>\w+) (cuisine|food))?( ?in a (?P<price>\w+) price range)?'
                '( ?for (?P<number>\w+)( people)?)?( ?in (?P<location>\w+))?)+( please)?$',
                '^we will be (?P<number>\w+)$'
            ],
            'deny': [
                '^no$',
                '^no this does not work for me$',
                '^do you have something else$',
                '^no i don\'t like that$'
            ],
            'affirm': [
                '^it\'s perfect$',
                '^i love that$',
                '^let\'s do it$',
                '^that looks great$'
            ],
            'request_phone': [
                '^may i have the phone number of the restaurant$',
                '^what is the phone number of the restaurant$',
                '^do you have its phone number$'
            ],
            'request_address': [
                '^may i have the address of the restaurant$',
                '^do you have its address$',
                '^can you provide the address$'
            ],
            'thankyou': [
                '^thanks$',
                '^thank you$',
                '^you rock$'
            ],
            'bye': [
                '^no thank you$',
                '^no thanks$'
            ],
            'silence': [
                '^<SILENCE>$'
            ]
        }
        for da in self.user_das:
            self.user_das[da] = [re.compile(pattern) for pattern in self.user_das[da]]
        self._bot_das = {
            'give_phone': [
                '^here it is \w+phone$'
            ],
            'give_address': [
                '^here it is \w+address$'
            ],
            'suggest_restaurant': [
                '^what do you think of this option: \w+$'
            ],
            'announce_search': [
                '^ok let me look into some options for you$'
            ],
            'request_updates': [
                '^sure is there anything else to update$'
            ],
            'announce_keep_searching': [
                '^sure let me find an other option for you$'
            ],
            'api_call': [
                '^api_call \w+ \w+ \w+ \w+$'
            ],
            'reserve': [
                '^great let me do the reservation$'
            ],
            'greet': [
                '^hello what can i help you with today$'
            ],
            'on_it': [
                '^i\'m on it$'
            ],
            'ask_location': [
                '^where should it be$'
            ],
            'ask_number_of_people': [
                '^how many people would be in your party$'
            ],
            'ask_price': [
                '^which price range are looking for$'
            ],
            'ask_cuisine': [
                '^any preference on a type of cuisine$'
            ],
            'ask_anything_else': [
                '^is there anything i can help you with$'
            ],
            'bye': [
                '^you\'re welcome$'
            ]
        }
        for da in self._bot_das:
            self._bot_das[da] = [re.compile(pattern) for pattern in self._bot_das[da]]

    def get_user_act(self, text):
        for act in self.user_das:
            for pattern in self.user_das[act]:
                match = pattern.search(text)
                if match:
                    return act, [{"start": match.span(ent)[0], "end": match.span(ent)[1], "value": val, "entity": ent}
                                 for ent, val in match.groupdict().items() if val]
        return None

    def get_bot_act(self, text):
        for act in self.bot_das:
            for pattern in self._bot_das[act]:
                if pattern.search(text):
                    return act
        return None

    def extract_rasa_nlu_training_examples(self, input_filename):
        examples = []
        for story in BabiReader.babi_dialogue_iterator(input_filename):
            for turn in story:
                text = turn['human']
                intent, entities = self.get_user_act(text)
                examples.append({"text": text, "intent": intent, "entities": entities})
        return examples, [], [], []

    @property
    def bot_das(self):
        return self._bot_das.keys()


class BabiT6Reader(BabiReader):
    das = {
        'greet': (
        'Hello , welcome to the Cambridge restaurant system \. You can ask for restaurants by area , price range or food type \. How may I help you \?$', 'Hello , welcome to the Cambridge restaurant system \. You can ask for restaurants by area , price range or food type \. How may I help you \?$'),  # 1117
        'api_call': ('api_call \w+ \w+ \w+$', 'api_call {cuisine} {location} {price}'),  # 1088
        'offer_rest_area_price': ('.+ is a nice place in the \w+ of town and the prices are \w+$', '.+ is a nice place in the {location} of town and the prices are {price}$'),  # 574
        'offer_rest_area_food': ('(.+ is a nice place in the \w+ of town serving tasty \w+ food$)|(.+ is a nice restaurant in the \w+ of town serving \w+ food$)', '.+ is a nice place in the {location} of town serving tasty {cuisine} food$'),  # 270
        'offer_rest_area_food_price': ('(.+ is a great restaurant serving \w+ \w+ food in the \w+ of town .$)|(.+ is a nice restaurant in the \w+ of town in the \w+ price range$)', '.+ is a great restaurant serving {price} {cuisine} food in the {location} of town .$'),  # no exact template in tst to match this trn one, semi-arbitrary choice here   71
        'offer_rest_area': ('.+ is a nice place in the \w+ of town$', '.+ is a nice place in the {location} of town$'),  # 90
        'offer_rest_food_price': ('.+ serves \w+ food in the \w+ price range$', '.+ serves {cuisine} food in the {price} price range$'),  # 268
        'offer_rest_food': ('(.+ serves \w+ food$)|(\w+ serves \w+ food \.$)', '.+ serves {cuisine} food$'),  # 371
        'offer_rest_price': ('(.+ is in the \w+ price range$)|(The price range at .+ is \w+ \.$)', '.+ is in the {price} price range$'),  # 110
        'offer_rest_price_postcode': ('\w+ is in the \w+ price range , and their post code is .+$', '\w+ is in the {price} price range , and their post code is .+$'),  # 3
        'offer_rest': ('.+ is a great restaurant$', '.+ is a great restaurant$'),  # 303
        'confirm_food_dontcare': ('You are looking for a restaurant serving any kind of food right\?$', 'You are looking for a restaurant serving any kind of food right\?$'),  # 247
        'confirm_price': ('Let me confirm , You are looking for a restaurant in the \w+ price range right\?$', 'Let me confirm , You are looking for a restaurant in the {price} price range right\?$'),  # 24
        'confirm_price_dontcare': ('Let me confirm , You are looking for a restaurant and you dont care about the price range right\?$', 'Let me confirm , You are looking for a restaurant and you dont care about the price range right\?$'),  # 8
        'confirm_area': ('Did you say you are looking for a restaurant in the \w+ of town\?$', 'Did you say you are looking for a restaurant in the {location} of town\?$'),  # 116
        'confirm_area_dontcare': ('Ok , a restaurant in any part of town is that right\?$', 'Ok , a restaurant in any part of town is that right\?$'),  # 45
        'bye': (' you are welcome$', ' you are welcome$'),  # 1117
        'ask_food': ('(What kind of food would you like\?$)|(Sorry would you like \w+ or \w+ food\?$)|(Sorry would you like \w+ food or you dont care)$', 'What kind of food would you like\?$'),  # 302
        'ask_area': ('(What part of town do you have in mind\?$)|(Sorry would you like the \w+ of town or you dont care$)|(Sorry would you like something in the \w+ or in the \w+$)|(There are restaurants \. That area would you like\?$)', 'What part of town do you have in mind\?$'),  # 244
        'ask_price': ('(Would you like something in the cheap , moderate , or expensive price range\?$)|(Sorry would you like something in the \w+ price range or in the \w+ price range$)|(Sorry would you like something in the \w+ price range or in the \w+ price range$)|(Sorry would you like something in the \w+ price range or you dont care$)', 'Would you like something in the cheap , moderate , or expensive price range\?$'),  # 157
        'canthelp_food': ('I\'m sorry but there is no restaurant serving \w+ food$', 'I\'m sorry but there is no restaurant serving {cuisine} food$'),  # 597
        'canthelp_food2': ('(I am sorry but there is no other \w+ restaurant that matches your request$)|(I am sorry but there is no \w+ restaurant that matches your request$)', 'I am sorry but there is no other {cuisine} restaurant that matches your request$'),  # 24
        'canthelp_food_price': ('(I am sorry but there is no other \w+ restaurant in the \w+ price range$)|(Sorry there is no \w+ restaurant in the \w+ price range$)', 'I am sorry but there is no other {cuisine} restaurant in the {price} price range$'),  # 10
        'canthelp_food_area': ('I am sorry but there is no other \w+ restaurant in the \w+ of town$', 'I am sorry but there is no other {cuisine} restaurant in the {location} of town$'),  # 14
        'canthelp_price_area': ('Sorry but there is no other restaurant in the \w+ price range and the \w+ of town$', 'Sorry but there is no other restaurant in the {price} price range and the {location} of town$'),  # 30
        'canthelp_food_price_area': ('Sorry but there is no other \w+ restaurant in the \w+ price range and the \w+ of town$', 'Sorry but there is no other {cuisine} restaurant in the {price} price range and the {location} of town$'),  # 10
        'canthelp_food_area2': ('(I\'m sorry but there is no \w+ restaurant in the \w+ of town$)|(Sorry there is no \w+ restaurant in the \w+ of town$)', 'I\'m sorry but there is no {cuisine} restaurant in the {location} of town$'),  # 85
        'canthelp_price_food': ('I\'m sorry but there is no restaurant serving \w+ \w+ food$', 'I\'m sorry but there is no restaurant serving {price} {cuisine} food$'),  # 54
        'canthelp_food_area_price': ('(I\'m sorry but there is no \w+ restaurant in the \w+ of town and the \w+ price range$)|(Sorry there is no \w+ restaurant in the \w+ of town serving \w+ food$)', 'I\'m sorry but there is no {cuisine} restaurant in the {location} of town and the {price} price range$'),  # 11
        'repeat': ('(Could you please repeat that\?$)|(Sorry I am a bit confused ; please tell me again what you are looking for \.$)|(You are looking for a restaurant is that right\?$)', 'Could you please repeat that\?$'),  # semi-arbitrary 'looking for a restaurant' addition, but in training practice, that's how they use it  518
        'canthear': ('Sorry, I can\'t hear you$', 'Sorry, I can\'t hear you$'),  # 25
        'confirm_food_area_ask_price': ('There are restaurants serving \w+ in the \w+ of town \. What price range would you like\?$', 'There are restaurants serving {cuisine} in the {location} of town \. What price range would you like\?$'),  # 107
        'confirm_food_price_ask_area': ('There are restaurants serving \w+ in the \w+ price range \. What area would you like\?$', 'There are restaurants serving {cuisine} in the {price} price range \. What area would you like\?$'),  # 106
        'confirm_food_price_dontcare_ask_area': ('There are restaurants serving \w+ in any price range \. What area would you like\?$', 'There are restaurants serving {cuisine} in any price range \. What area would you like\?$'),  # 10
        'confirm_area_food_dontcare_ask_price': ('There are restaurants in the \w+ of town serving any kind of food \. What price range would you like\?$', 'There are restaurants in the {location} of town serving any kind of food \. What price range would you like\?$'),  # 61
        'confirm_price_area_ask_food': ('There are restaurants in the \w+ price range and the \w+ of town \. What type of food would you like\?$', 'There are restaurants in the {price} price range and the {location} of town \. What type of food would you like\?$'),  # 210
        'confirm_food_ask_area': ('There are restaurants serving \w+ food \. What area do you want\?$', 'There are restaurants serving {cuisine} food \. What area do you want\?$'),  # 164
        'confirm_food_area_dontcare_ask_price': ('There are restaurants serving \w+ food in any part of town \. What price range would you like\?$', 'There are restaurants serving {cuisine} food in any part of town \. What price range would you like\?$'),  # 107
        'confirm_food_ask_price': ('There are restaurants serving \w+ food \. What price range do you want\?$', 'There are restaurants serving {cuisine} food \. What price range do you want\?$'),  # 14
        'confirm_area_ask_food': ('There are restaurants in the \w+ of town \. What type of food do you want\?$', 'There are restaurants in the {location} of town \. What type of food do you want\?$'),  # 155
        'confirm_price_ask_food': ('There are restaurants in the \w+ price range . What type of food do you want\?$', 'There are restaurants in the {price} price range . What type of food do you want\?$'),  # 184
        'confirm_price_ask_area': ('There are restaurants in the \w+ price range \. What area do you want\?$', 'There are restaurants in the {price} price range \. What area do you want\?$'),  # 1
        'confirm_area_dontcare_ask_price': ('There are restaurants in all parts of town \. What type of pricerange do you want\?$', 'There are restaurants in all parts of town \. What type of pricerange do you want\?$'),  # 1
        'confirm_food_dontcare_ask_area': ('There are restaurants if you don\'t care about the food \. What area do you want\?$', 'There are restaurants if you don\'t care about the food \. What area do you want\?$'),  # 21
        'confirm_food_dontcare_ask_price': ('There are restaurants if you don\'t care about the food \. What price range do you want\?$', 'There are restaurants if you don\'t care about the food \. What price range do you want\?$'),  # 1
        'confirm_area_dontcare_food_dontcare_ask_price': ('There are restaurants if you don\'t care about the area or the type of food \. What price range would you like\?$', 'There are restaurants if you don\'t care about the area or the type of food \. What price range would you like\?$'),  # 15
        'confirm_food_dontcare_price_ask_area': ('There are restaurants serving any kind of food in the \w+ price range \. What area would you like\?$', 'There are restaurants serving any kind of food in the {price} price range \. What area would you like\?$'),  # 39
        'confirm_area_dontcare_ask_food': ('There are restaurants in all parts of town \. What type of food do you want\?$', 'There are restaurants in all parts of town \. What type of food do you want\?$'),  # 8
        'confirm_food': ('You are looking for a \w+ restaurant right\?$', 'You are looking for a {cuisine} restaurant right\?$'),  # 368
        'give_phone': ('The phone number of .+ is \w+$', 'The phone number of .+ is \w+$'),  # 795
        'give_phone2': ('\w+ is a great restaurant serving \w+ food \. Their phone number is .+ \.$', '\w+ is a great restaurant serving {cuisine} food \. Their phone number is .+ \.$'),  # 1
        'give_postcode': ('The post code of .+ is \w+$', 'The post code of .+ is \w+$'),  # 163
        'give_address': ('The address of \w+ is .+ \.$', 'The address of \w+ is .+ \.$'),  # 3
        'give_area': ('(Sure , .+ is on \w+$)|(.+ is in the \w+ part of town \.$)|(\w+ is in the \w+ , at .+$)', 'Sure , .+ is on \w+$'),  # This gives address     611
        'give_address2': ('(\w+ is on \w+$)|(the good luck chinese food takeaway is on \w+$)', '\w+ is on \w+$'),  # both OR clauses are seen in test data  24
        'askmore': ('Can I help you with anything else\?$', 'Can I help you with anything else\?$')  # 165
    }
    das = {da: (re.compile(patterns[0]), patterns[1]) for da, patterns in das.items()}
    act2id = {da: i for i, da in enumerate(das)}
    id2act = {i: da for da, i in act2id.items()}

    intents = {
        'affirm': 0,
        'bye': 1,
        'dontcare': 2,
        'inform': 3,
        'negate': 4,
        'reqalts': 5,
        'request_address': 6,
        'request_food': 7,
        'request_location': 8,
        'request_phone': 9,
        'request_postcode': 10,
        'request_price': 11,
        'silence': 12
    }

    entity2id = {
        'cuisine': 0,
        'location': 1,
        'price': 2
    }

    cuisine_types = []
    with open(BABI_T6_KB_FILE) as kb_fh:
        for line in kb_fh:
            match = re.search('R_cuisine (?P<value>\w+)', line)
            if match:
                cuisine_types.append(match.group('value'))
    cuisine_types = list(set(cuisine_types))
    prices = ['cheap', 'moderate', 'expensive']
    locations = ['centre', 'north', 'south', 'east', 'west']
    location_syns = {'centre': ['center']}
    prices_syns = {'moderate': ['moderately']}

    w2id, id2w = BabiReader.vocab(BABI_T6_TRN_FILE, 1)

    def __init__(self, nlu_model_path, babit6_kb_filename):
        """
        :param nlu_model_path: path the the Rasa NLU saved model
        :param babit6_kb_filename: bAbI knowledge base file
        """
        self.babi_kb = babit6_kb_filename
        self.interpreter = RasaNLUInterpreter(nlu_model_path)

    def get_bot_act(self, text):
        for da, (pattern, _) in BabiT6Reader.das.items():
            if pattern.match(text):
                return da
        return None

    def get_user_act(self, text):
        parse_data = self.interpreter.parse(text)
        return parse_data['intent']['name'], parse_data['entities']

    @property
    def bot_das(self):
        return BabiT6Reader.das.keys()

    def extract_rasa_nlu_training_examples(self, input_filename):
        # nlu_data, failed_examples = _generate_dstc2_examples(ontology_file=ontology, path_prefix=dstc2_datapath,
        #                                                      file_index=file_index)
        # get all possible values for all entities
        values = {'cuisine': [], 'location': [], 'price': []}
        with open(self.babi_kb) as kb_fh:
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
                '.*(?P<cuisine>(' + '|'.join(all_values['cuisine']) + ')).*',  # cuisine
                '.*(?P<location>(' + '|'.join(all_values['location']) + ')).*',  # location
                '.*(?P<price>(' + '|'.join(all_values['price']) + ')).*',  # price

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
                '^no$',
                '^wrong$'
            ]
        }
        human_templates = {intent: [re.compile(pattern) for pattern in human_templates[intent]]
                           for intent in human_templates}
        intent_priority = [  # re patterns are tried in this order. More general patterns go last
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
        unknown = []

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

        for story in BabiReader.babi_dialogue_iterator(input_filename):
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
                    # unknown.append('human: {}\t (bot: {})'.format(human_says, turn['bot']))
                    unknown.append((human_says, turn['bot']))
        return [examples[intent][text] for intent in examples for text in examples[intent]], \
               [{"value": value, "synonyms": synonyms[entity][value]}
                for entity in synonyms for value in synonyms[entity]
                if synonyms[entity][value]], [], unknown


def _get_args():
    parser = argparse.ArgumentParser(
        description='produce Rasa format training files')
    parser.add_argument('--nlu', action='store_true', default=False, help='produce Rasa format NLU training file')
    parser.add_argument('--dialog', action='store_true', default=False, help='produce Rasa format dialog training file')
    parser.add_argument('--task', choices=['t5', 't6'], help='bAbI task, must be t5 or t6. Mandatory if --nlu flag set')
    parser.add_argument('--trn', action='store_true', help='if set, the default training file for the task will be '
                                                           'used. If flags --dev or --tst are set or the --input '
                                                           'argument is provided, the data gathered from all of them '
                                                           'is combined')
    parser.add_argument('--dev', action='store_true', help='if set, the default development file for the task will be '
                                                           'used. If flags --trn or --tst are set or the --input '
                                                           'argument is provided, the data gathered from all of them '
                                                           'is combined')
    parser.add_argument('--tst', action='store_true', help='if set, the default test file for the task will be '
                                                           'used. If flags --dev or --trn are set or the --input '
                                                           'argument is provided, the data gathered from all of them '
                                                           'is combined')
    parser.add_argument('--input', type=str, help='babi input file name')
    parser.add_argument('--nlu-output', dest='nlu_output', type=str, help='NLU output file name, mandatory if --nlu '
                                                                          'flag is set')
    parser.add_argument('--dialog-output', dest='dialog_output', type=str, help='dialog output file name, mandatory if '
                                                                          '--dialog flag is set')
    parser.add_argument('--utter-prefixes', dest='utter_prefixes', action='store_true', default=False)

    args = parser.parse_args()
    # basic checks
    if not args.nlu and not args.dialog:
        raise Exception('either --nlu or --dialog argument must be provided')
    if args.nlu:
        if not args.task:
            raise Exception('argument --task is mandatory if --nlu flag is set')
        if args.task not in ['t5', 't6']:
            raise Exception('--task must be either t5 or t6')
        if not args.nlu_output:
            raise Exception('argument --nlu-output is mandatory if --nlu flag is set')
    if not (args.input or args.trn or args.dev or args.tst):
        raise Exception('at least one input source must be specified. Set any of the --trn, --dev or --tst flags or '
                        'provide the --input argument')
    if args.input and not isfile(args.input):
        raise FileNotFoundError('input file {} does not exist'.format(args.input))
    if args.dialog and not args.dialog_output:
        raise Exception('argument --dialog-output is mandatory if --dialog flag is set')
    return args


if __name__ == '__main__':
    def get_input_sources():
        sources = [args.input] if args.input else []
        if args.task == 't5':
            if args.trn:
                sources.append(BABI_T5_TRN_FILE)
            if args.dev:
                sources.append(BABI_T5_DEV_FILE)
            if args.tst:
                sources.append(BABI_T5_TST_FILE)
        if args.task == 't6':
            if args.trn:
                sources.append(BABI_T6_TRN_FILE)
            if args.dev:
                sources.append(BABI_T6_DEV_FILE)
            if args.tst:
                sources.append(BABI_T6_TST_FILE)
        return sources
    args = _get_args()
    sources = get_input_sources()
    reader = BabiT6Reader(join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME), BABI_T6_KB_FILE) if args.task == 't6' else \
        BabiT5Reader()
    if args.nlu:
        examples, synonyms, regex_features, unparsables = [], [], [], []
        for input in sources:
            e, s, r, u = reader.extract_rasa_nlu_training_examples(input)
            examples += e
            synonyms += s
            regex_features += r
            unparsables += u
        reader.produce_rasa_nlu_training_file(examples, args.nlu_output, synonyms, regex_features)
        unparsable_fn, _ = splitext(args.nlu_output)
        with open(unparsable_fn + '_unparsable.txt', "w") as unparsable_fh:
            for h, r in unparsables:
                unparsable_fh.write('user: {}\t (bot: {})\n'.format(h, r))
    if args.dialog:
        prefixes = {action: 'utter_' for action in reader.bot_das} if args.utter_prefixes else None
        reader.produce_dialog_rasa_training_file(input_filename=args.input, output_filename=args.dialog_output,
                                                 action_prefixes=prefixes)
