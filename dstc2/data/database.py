from collections import defaultdict
import pandas as pd

BABI2FABOT_SLOT = {b: f for b, f in zip(['R_cuisine', 'R_location', 'R_price', 'R_address', 'R_phone', 'R_post_code'],
                                        ['food', 'area', 'pricerange', 'address', 'phone', 'postcode'])}

NOT_PREFIX = 'NOT|||'

BABI_MESSAGES = {
    'no_more_options': [
        'I am sorry but there is no other [\w ]+ restaurant that matches your request',
        'I am sorry but there is no other [\w ]+ restaurant in the \w+ price range',
        'I am sorry but there is no other [\w ]+ restaurant in the \w+ of town',
        'Sorry but there is no other [\w ]+ restaurant in the \w+ price range and the \w+ of town',
        'Sorry but there is no other restaurant in the \w+ price range and the \w+ of town'
    ],
    'canthelp': [
        'I\'m sorry but there is no restaurant serving [\w ]+ food',
        'I\'m sorry but there is no [\w ]+ restaurant in the \w+ of town',
        'I\'m sorry but there is no restaurant serving \w+ [\w ]+ food',
        'I\'m sorry but there is no [\w ]+ restaurant in the \w+ of town',
        'Sorry there is no [\w ]+ restaurant in the \w+ price range',
        'Sorry there is no [\w ]+ restaurant in the \w+ of town',
        'I am sorry but there is no [\w ]+ restaurant that matches your request',
        'I\'m sorry but there is no restaurant serving barbeque foo'
    ],
    'offer_restaurant': [
        '[\w ]+ is a nice place in the \w+ of town and the prices are \w+',
        '[\w ]+ is a nice place in the \w+ of town serving tasty [\w ]+ food',
        '[\w ]+ is a great restaurant serving \w+ [\w ]+ food in the \w+ of town',
        '[\w ]+ is a great restaurant',
        '[\w ]+ is a nice place in the \w+ of town',
        '[\w ]+ is in the \w+ part of town .',
        '[\w ]+ is a nice restaurant in the \w+ of town serving [\w ]+ food',
        'The price range at [\w ]+ is \w+ .',
        '[\w ]+ is a nice restaurant in the \w+ of town in the \w+ price range'
    ],
    'answer_request': [
        'Sure , [\w ]+ is on [\w ]+',
        'The phone number of [\w ]+ is [\w ]+',
        '[\w ]+ is in the \w+ price range',
        '[\w ]+ serves [\w ]+ food',
        'The post code of [\w ]+ is [\w ]+',
        '[\w ]+ is on [\w ]+',
        'The address of [\w ]+ is [\w ]+ .',
        '[\w ]+ is in the \w+ , at [\w. ,]'
    ],
    'reqmore': [
        'Can I help you with anything else?'
    ],
    'request_food': [
        'What kind of food would you like?'
    ],
    'request_area': [
        'in which area?',
        'What part of town do you have in mind?',
        'There are restaurants . That area would you like?'
    ],
    'request_pricerange': [
        'Would you like something in the cheap , moderate , or expensive price range?'
    ],
    'confirm-domain': [
        'You are looking for a restaurant is that right?'
    ],
    'bye': [
        ' you are welcome'
    ],
    'expl-conf': [
        'Let me confirm , You are looking for a restaurant and you dont care about the price range right?',
        'You are looking for a restaurant serving any kind of food right?',
        'You are looking for a [\w ]+ restaurant right?',
        'Let me confirm , You are looking for a restaurant in the \w+ price range right?',
        'Ok , a restaurant in any part of town is that right?',
        'Did you say you are looking for a restaurant in the \w+ of town?'
    ],
    'select': [
        'Sorry would you like [\w ]+ food or you dont care',
        'Sorry would you like [\w ]+ or [\w ]+ food',
        'Sorry would you like something in the \w+ price range or you dont care',
        'Sorry would you like something in the \w+ price range or in the \w+ price range',
        'Sorry would you like the \w+ of town or you dont care',
        'Sorry would you like something in the \w+ or in the \w+'
    ],
    'request_area_detailed': [
        'There are (\d+ )?restaurants if you don\'t care about the food . What area do you want?',
        'There are \d+ restaurants serving [\w ]+ food . What area do you want?',
        'There are \d+ restaurants if you don\'t care about the price range . What area do you want?',
        'There are \d+ restaurants in the \w+ price range . What area do you want?',
        'There are \d+ restaurants if you don\'t care about the food in the \w+ price range . What area would you '
        'like?',
        'There are \d+ restaurants serving [\w ]+ in any price range . What area would you like?',
        'There are \d+ restaurants serving [\w ]+ in the \w+ price range . What area would you like?',
        'There are restaurants in the \w+ price range . What area do you want?',
        'There are restaurants serving [\w ]+ food . What area do you want?',
        'There are restaurants serving any kind of food in the \w+ price range . What area would you like?',
        'There are restaurants serving [\w ]+ in any price range . What area would you like?',
        'There are restaurants serving [\w ]+ in the \w+ price range . What area would you like?'
    ],
    'request_food_detailed': [
        'There are \d+ restaurants in all parts of town . What type of food do you want?',
        'There are (\d+ )?restaurants in the \w+ of town . What type of food do you want?',
        'There are \d+ restaurants in the \w+ price range . What type of food do you want?',
        'There are \d+ restaurants in the \w+ price range and the \w+ of town . What type of food would you like?',
        'There are \d+ restaurants in the \w+ price range and the \w+ of town . What type of food would you like?',
        'There are restaurants in the \w+ price range and the \w+ of town . What type of food would you like?',
        'There are restaurants in the \w+ price range . What type of food do you want?',
        'There are restaurants in all parts of town . What type of food do you want?',
        'There are restaurants if you don\'t care about the price range . What type of food do you want?',  # fabot only
        'There are restaurants if you don\'t care about the price range or area . What type of food do you '
        'want?',  # fabot only
        'There are restaurants in all parts of town in the \w+ price range . What type of food do you '
        'want?'  # fabot only
    ],
    'request_pricerange_detailed': [
        'There are \d+ restaurants in all parts of town . What type of pricerange do you want?',
        'There are (\d+ )?restaurants if you don\'t care about the food . What price range do you want?',
        'There are \d+ restaurants if you don\'t care about the area or the type of food . What price range would '
        'you like?',
        'There are \d+ restaurants serving [\w ]+ food in any part of town . What price range would you like?',
        'There are (\d+ )?restaurants in the \w+ of town serving any kind of food . What price range would you like?',
        'There are \d+ restaurants serving [\w ]+ in the \w+ of town . What price range would you like?',
        'There are restaurants serving [\w ]+ food . What price range do you want?',
        'There are restaurants serving [\w ]+ food in any part of town . What price range would you like?',
        'There are restaurants serving [\w ]+ in the \w+ of town . What price range would you like?',
        'There are restaurants in all parts of town . What type of pricerange do you want?',
        'There are restaurants if you don\'t care about the area or the type of food . What price range would you like?'
    ],
    'misc': [
        'api_call [\w]+ [\w]+ [\w]+',
        'Sorry, I can\'t hear you',
        'Sorry I am a bit confused ; please tell me again what you are looking for .',
        'Hello , welcome to the Cambridge restaurant system . You can ask for restaurants by area , price range or '
        'food type . How may I help you ?',
        'Could you please repeat that?'
    ]
}


class BabiDB(object):

    def __init__(self, babi_kb):
        restaurants = defaultdict(dict)
        with open(babi_kb, 'r') as babi_kb_handler:
            for line in babi_kb_handler:
                _, name, var, value = line.split()
                restaurants[name][BABI2FABOT_SLOT[var]] = value
        self.restaurants = pd.DataFrame(columns=['name', 'food', 'area', 'pricerange', 'address', 'phone', 'postcode'])
        for restaurant, data in restaurants.items():
            # add the missing values as None:
            for var in BABI2FABOT_SLOT.keys():
                if BABI2FABOT_SLOT[var] not in data:
                    data[BABI2FABOT_SLOT[var]] = None
            self.restaurants = self.restaurants.append({'name': restaurant, **data}, ignore_index=True)

    def find_restaurant(self, **kwargs):
        """
        query the database with an arbitrary number of requestable parameters
        :param kwargs: arguments with the name of the requestable slots in the database (i.e. 'food', 'area',
        'pricerange' and 'name'). Any value not passed is not used as a filter
        :return: a pandas.DataFrame with the records that fulfill the query
        """
        result = self.restaurants
        for var, value in kwargs.items():  # go through each condition
            if value.startswith(NOT_PREFIX):  # search all but those with this value
                result = result[result[var] != value]
            else:
                result = result[result[var].str.contains(value)] if var == 'name' else result[result[var] == value]
        return result

    def num_results(self, **kwargs):
        return len(self.find_restaurant(**kwargs))
