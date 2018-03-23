from collections import defaultdict
import pandas as pd

BABI2FABOT_SLOT = {b: f for b, f in zip(['R_cuisine', 'R_location', 'R_price', 'R_address', 'R_phone', 'R_post_code'],
                                        ['food', 'area', 'pricerange', 'address', 'phone', 'postcode'])}

NOT_PREFIX = 'NOT|||'


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
