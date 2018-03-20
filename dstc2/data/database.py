from collections import defaultdict
import pandas as pd

BABI2FABOT_SLOT = {b: f for b, f in zip(['R_cuisine', 'R_location', 'R_price', 'R_address', 'R_phone', 'R_post_code'],
                                        ['food', 'area', 'pricerange', 'address', 'phone', 'postcode'])}


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
        self.latest_results = None  # tmp storage to keep results of latest query, to iterate over them if user wants
        self.last_offered_index = None  # when this = len(latest_results), we know options were exhausted

    def _update_latest_search_results(self, results):
        """updates the latest results so that it can be referenced later upon user request"""
        if len(results) > 0:
            self.latest_results, self.latest_results = results, 0
        else:
            self.latest_results, self.latest_results = None, None
        return results

    def find_restaurant(self, **kwargs):
        """
        query the database with an arbitrary number of requestable parameters
        :param kwargs: arguments with the name of the requestable slots in the database (i.e. 'food', 'area',
        'pricerange' and 'name'). Any value not passed is not used as a filter
        :return: a pandas.DataFrame with the records that fulfill the query
        """
        result = self.restaurants
        for var, value in kwargs.items():  # go through each condition
            result = result[result[var] == value]
        return self._update_latest_search_results(result)
