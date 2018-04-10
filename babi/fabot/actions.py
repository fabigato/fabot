from rasa_core.actions import Action
from rasa_core.events import SlotSet
from data.database import BabiDB
from globals import BABI_PATH, DSTC2_ONTOLOGY_FILE
from os.path import join
import logging
from numpy.random import choice, seed
import json
from rasa_core import utils

seed(42)
db = BabiDB(babi_kb=join(BABI_PATH, 'dialog-babi-task6-dstc2-kb.txt'))
logger = logging.getLogger(__name__)
utils.configure_colored_logging(loglevel="INFO")
logging.basicConfig(level="INFO")

with open(DSTC2_ONTOLOGY_FILE, 'r') as ontology_handler:
    ontology = json.load(ontology_handler)['informable']
for informable in ontology:
    ontology[informable].append('dontcare')


def _produce_no_more_options_message(filters):
    filter_names = set(filters.keys())
    if filter_names == {'food'}:
        message = 'I am sorry but there is no other {food} restaurant that matches your request'.format(
            food=filters['food'])
    elif filter_names == {'food', 'pricerange'}:
        message = 'I am sorry but there is no other {food} restaurant in the {pricerange} price range'.format(
            food=filters['food'], pricerange=filters['pricerange'])
    elif filter_names == {'food', 'area'}:
        message = 'I am sorry but there is no other {food} restaurant in the {area} of town'.format(
            food=filters['food'], area=filters['area'])
    else:
        logger.warning('tried to produce <no-more-options> message, but encountered unknown filter combination: {}'.
                       format(filter_names))
        message = 'I am sorry but there is no other restaurant that matches your request'
    return message


def _produce_unsuccessful_search_message(filters):
    """
    Builds the right 'no results found' sentence used in bAbI t6 which depends on the filters provided
    :param filters: dictionary mapping slot names to their value
    :return: message as a string
    """
    # every message here should be compatible with this regex:
    # '^(Sorry|I am sorry but|I\'m sorry but) there is no(?! other) .*restaurant'
    filter_names = set(filters.keys())
    if filter_names == {'food'}:
        message = 'I\'m sorry but there is no restaurant serving {food} food'.format(food=filters['food'])
    elif filter_names == {'food', 'area'}:
        message = 'I\'m sorry but there is no {food} restaurant in the {area} of town'.format(food=filters['food'],
                                                                                              area=filters['area'])
    elif filter_names == {'pricerange', 'food'}:
        message = 'I\'m sorry but there is no restaurant serving {pricerange} {food} food'.format(
            pricerange=filters['pricerange'], food=filters['food'])
    elif filter_names == {'food', 'area'}:
        message = 'I\'m sorry but there is no {food} restaurant in the {area} of town'.format(
            food=filters['food'], area=filters['area']
        )
    else:
        logger.info('unknown filter combination when producing unsuccess message: {}'.format(filter_names))
        message = 'I\'m sorry but there is no restaurant with the provided criteria'
    return message


def _produce_offer_restaurant_message(tracker):
    filters = {var: value for var, value in tracker.current_slot_values().items() if
               var in ['food', 'pricerange', 'area'] and value not in [None, 'dontcare']}
    filter_names = set(filters.keys())
    restaurant = _get_current_restaurant(tracker)
    if filter_names == {'area', 'pricerange'}:
        message = '{name} is a nice place in the {area} of town and the prices are {pricerange}'.format(
            name=restaurant['name'],
            area=restaurant['area'],
            pricerange=restaurant['pricerange'])
    elif filter_names == {'area', 'food'}:
        message = '{name} is a nice place in the {area} of town serving tasty {food} food'.format(
            name=restaurant['name'], area=restaurant['area'], food=restaurant['food']
        )
    elif filter_names == {'area', 'food', 'pricerange'}:
        message = '{name} is a great restaurant serving {pricerange} {food} food in the {area} of town .'.format(
            name=restaurant['name'], pricerange=restaurant['pricerange'], food=restaurant['food'],
            area=restaurant['area']
        )
    else:
        logger.info('unknown filter combination when producing offer restaurant message: {}'.format(filter_names))
        message = '{name} serves {food} food'.format(name=restaurant['name'], food=restaurant['food'])
    return message


def _get_current_restaurant(tracker):
    if tracker.current_slot_values()['last_offer_index'] is not None and \
            tracker.current_slot_values()['results'] is not None:
        return tracker.current_slot_values()['results'].iloc[tracker.current_slot_values()['last_offer_index']]
    else:
        return None


def _search_and_inform(tracker, dispatcher):
    def search():
        results = db.find_restaurant(**filters)
        if len(results) == 0:
            message = _produce_unsuccessful_search_message(filters)
        else:
            # message = _produce_offer_restaurant_message(tracker)
            food = filters['food'].lower().replace(' ', '_') if ('food' in filters and filters['food'] != 'dontcare') \
                else 'R_cuisine'
            area = filters['area'].lower() if ('area' in filters and filters['area'] != 'dontcare') else 'R_location'
            pricerange = filters['pricerange'] if ('pricerange' in filters and filters['pricerange'] != 'dontcare') \
                else 'R_price'
            message = 'api_call ' + food + ' ' + area + ' ' + pricerange
        dispatcher.utter_message(message)
        return results

    filters = {var: value for var, value in tracker.current_slot_values().items() if
               var in ['food', 'pricerange', 'area'] and value not in [None, 'dontcare']}
    if tracker.latest_message.intent['name'] not in {'reqalts', 'request'}:
        # if user did not ask for options or a slot value, we must do a new query
        results = search()
        return [SlotSet("results", results if len(results) > 0 else None),
                SlotSet("last_offer_index", 0 if len(results) > 0 else None)]
    else:
        results = tracker.current_slot_values()['results']
        if results is not None:
            current_index = tracker.current_slot_values()['last_offer_index'] + 1
            if current_index < len(results):
                message = _produce_offer_restaurant_message(tracker)
                dispatcher.utter_message(message)
                return [SlotSet("last_offer_index", current_index)]
            else:
                message = _produce_no_more_options_message(filters)
                dispatcher.utter_message(message)
                return [SlotSet("last_offer_index", current_index - 1)]
        else:
            results = search()
            return [SlotSet("results", results if len(results) > 0 else None),
                    SlotSet("last_offer_index", 0 if len(results) > 0 else None)]


class ActionCantHelp(Action):
    def name(self):
        return 'canthelp'

    def run(self, dispatcher, tracker, domain):
        return _search_and_inform(tracker=tracker, dispatcher=dispatcher)


class ActionOfferRestaurant(Action):
    def name(self):
        return 'offer_restaurant'

    def run(self, dispatcher, tracker, domain):
        return _search_and_inform(tracker=tracker, dispatcher=dispatcher)


class ActionNoMoreOptions(Action):
    def name(self):
        return 'no_more_options'

    def run(self, dispatcher, tracker, domain):
        return _search_and_inform(tracker=tracker, dispatcher=dispatcher)


class ActionOfferPhone(Action):
    def name(self):
        return 'offer_phone'

    def run(self, dispatcher, tracker, domain):
        restaurant = _get_current_restaurant(tracker)
        if restaurant is not None:  # '^The phone number of .+ is .+$'
            message = 'The phone number of {} is {}'.format(restaurant['name'], restaurant['phone'])
        else:
            logger.warning('predicted offer_phone when there was no topic restaurant set')
            message = 'The phone number of UNSET is UNSET'
        dispatcher.utter_message(message)
        return []


class ActionOfferPostcode(Action):
    def name(self):
        return 'offer_postcode'

    def run(self, dispatcher, tracker, domain):
        restaurant = _get_current_restaurant(tracker)
        if restaurant is not None:  # '^The post code of .+ is .+$'
            message = 'The post code of {} is {}'.format(restaurant['name'], restaurant['postcode'])
        else:
            logger.warning('predicted offer_postcode when there was no topic restaurant set')
            message = 'The post code of UNSET is UNSET'
        dispatcher.utter_message(message)
        return []


class ActionOfferAddress(Action):
    def name(self):
        return 'offer_address'

    def run(self, dispatcher, tracker, domain):
        restaurant = _get_current_restaurant(tracker)
        if restaurant is not None:  # '^The address of .* is .* \.$'
            message = 'The address of {} is {} .'.format(restaurant['name'], restaurant['address'])
        else:
            logger.warning('predicted offer_address when there was no topic restaurant set')
            message = 'The address of UNSET is UNSET .'
        dispatcher.utter_message(message)
        return []


class ActionOfferPricerange(Action):
    def name(self):
        return 'offer_pricerange'

    def run(self, dispatcher, tracker, domain):
        restaurant = _get_current_restaurant(tracker)
        if restaurant is not None:  # '^The price range at .* is \w+$'
            message = 'The price range at {} is {}'.format(restaurant['name'], restaurant['pricerange'])
        else:
            logger.warning('predicted offer_pricerange when there was no topic restaurant set')
            message = 'The price range at UNSET is UNSET'
        dispatcher.utter_message(message)
        return []


class ActionConfirmAskPrice(Action):
    def name(self):
        return 'confirm_ask_price'

    def run(self, dispatcher, tracker, domain):
        '^There are restaurants .+ What (type of )?price ?range (do you want|would you like)\?$'
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        if 'pricerange' in filters:
            logger.warning('bot predicted request_pricerange_detailed, but the food is already set. Uttering it anyway')
            del filters['pricerange']
        other_slots = {s for s in filters}
        if other_slots == {'area'}:
            if filters['area'] == 'dontcare':
                message = 'There are restaurants in all parts of town . What type of pricerange do you want?'
            else:
                message = 'There are restaurants in the {} of town . What type of pricerange do you want?'.format(
                    filters['area']
                )
        elif other_slots == {'food'}:
            if filters['food'] == 'dontcare':
                message = 'There are restaurants if you don\'t care about the food . What price range do you want?'
            else:
                message = 'There are restaurants serving {} food . What price range do you want?'.format(
                    filters['food'])
        elif other_slots == {'area', 'food'}:
            area, food = filters['area'], filters['food']
            if area == 'dontcare' and food == 'dontcare':
                message = 'There are restaurants if you don\'t care about the area or the type of food . What ' \
                          'price range would you like?'
            elif area == 'dontcare' and food != 'dontcare':
                message = 'There are restaurants serving {} food in any part of town . What price range would you'
                ' like?'.format(food)
            elif area != 'dontcare' and food == 'dontcare':
                message = 'There are restaurants in the {} of town serving any kind of food . What price range ' \
                          'would you like?'.format(area)
            elif area != 'dontcare' and food != 'dontcare':
                message = 'There are restaurants serving {} in the {} of town . What price range would you like?'. \
                    format(food, area)
        else:
            logger.warning('Unknown combination of other slots when processing ActionRequestAreaDetailed: {}'.format(
                other_slots))
            message = 'There are restaurants available. What pricerange do you want?'
        dispatcher.utter_message(message)
        return [SlotSet("current_slot", 'pricerange')]


class ActionConfirmAskArea(Action):
    def name(self):
        return 'confirm_ask_area'

    def run(self, dispatcher, tracker, domain):
        """The bot affirms there are available options with the provided slots, and then requests the value of
                area. Calling this action when area is already set is a mistake that will be logged but area will be
                requested anyway"""
        '^There are  ?restaurants .+ What area (do you want\?|would you like\?)$'
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        if 'area' in filters:
            logger.warning('bot predicted request_area_detailed, but the area is already set. Uttering it anyway')
            del filters['area']
        other_slots = {s for s in filters}
        if other_slots == {'food'}:
            if filters['food'] == 'dontcare':
                message = "There are restaurants if you don't care about the food . What area do you want?"
            else:
                message = 'There are restaurants serving {} food . What area do you want?'.format(filters['food'])
        elif other_slots == {'pricerange'}:
            if filters['pricerange'] == 'dontcare':  # never observed in test data
                message = "There are restaurants if you don't care about the price range . What area do you want?"
            else:
                message = 'There are restaurants in the {} price range . What area do you want?'.format(
                    filters['pricerange'])
        elif other_slots == {'food', 'pricerange'}:
            food, pricerange = filters['food'], filters['pricerange']
            if food == 'dontcare' and pricerange == 'dontcare':  # never observed
                message = 'There are restaurants if you don\'t care about the food in any price range . ' \
                          'What area would you like?'
            elif food == 'dontcare' and pricerange != 'dontcare':  # never observed
                message = 'There are restaurants if you don\'t care about the food in the {} price range . ' \
                          'What area would you like?'.format(pricerange)
            elif food != 'dontcare' and pricerange == 'dontcare':
                message = 'There are restaurants serving {} in any price range . What area would you like?'. \
                    format(food)
            elif food != 'dontcare' and pricerange != 'dontcare':
                message = 'There are restaurants serving {} in the {} price range . What area would you like?'. \
                    format(food, pricerange)
        else:
            logger.warning('Unknown combination of other slots when processing ActionRequestAreaDetailed: {}'.format(
                other_slots))
            message = 'There are restaurants available. What area do you want?'
        dispatcher.utter_message(message)
        return [SlotSet("current_slot", 'area')]


class ActionConfirmAskFood(Action):
    def name(self):
        return 'confirm_ask_food'

    def run(self, dispatcher, tracker, domain):
        '^There are  ?restaurants .+ What type of food (do you want|would you like)\?$'
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        if 'food' in filters:
            logger.warning('bot predicted request_food_detailed, but the food is already set. Uttering it anyway')
            del filters['food']
        other_slots = {s for s in filters}
        if other_slots == {'area'}:
            if filters['area'] == 'dontcare':
                message = 'There are restaurants in all parts of town . What type of food do you want?'
            else:
                message = 'There are restaurants in the {} of town . What type of food do you want?'.format(
                    filters['area'])
        elif other_slots == {'pricerange'}:
            if filters['pricerange'] == 'dontcare':
                message = 'There are restaurants if you don\'t care about the price range . What type of food do ' \
                          'you want?'  # never observed in trn/dev/tst
            else:
                message = 'There are restaurants in the {} price range . What type of food do you want?'.format(
                    filters['pricerange'])
        elif other_slots == {'area', 'pricerange'}:
            area, pricerange = filters['area'], filters['pricerange']
            if area == 'dontcare' and pricerange == 'dontcare':
                message = 'There are restaurants if you don\'t care about the price range or area . What type of ' \
                          'food do you want?'  # never observed in trn/dev/tst
            elif area == 'dontcare' and pricerange != 'dontcare':
                message = 'There are restaurants in all parts of town in the {} price range . What type of food do ' \
                          'you want?'.format(pricerange)
            elif area != 'dontcare' and pricerange == 'dontcare':
                message = 'There are restaurants in all parts of town if you don\'t care about the price range . ' \
                          'What type of food do you want?'  # never observed
            elif area != 'dontcare' and pricerange != 'dontcare':
                message = 'There are restaurants in the {} price range and the {} of town . What type of food ' \
                          'would you like?'.format(pricerange, area)
        else:
            logger.warning('Unknown combination of other slots when processing ActionRequestAreaDetailed: {}'.format(
                other_slots))
            message = 'There are restaurants available. What type of food do you want?'
        dispatcher.utter_message(message)
        return [SlotSet("current_slot", 'food')]


class ActionConfirmFood(Action):
    def name(self):
        return 'confirm_food'

    def run(self, dispatcher, tracker, domain):
        # '^You are looking for a .*restaurant .*right\?$'
        value = tracker.current_slot_values()['food']
        if value == 'dontcare':
            message = 'You are looking for a restaurant serving any kind of food right?'
        elif isinstance(value, str):
            message = 'You are looking for a {} restaurant right?'.format(value)
        else:
            message = 'You are looking for a restaurant right?'
            logger.warning('unexpected food value when issuing confirm_food: {}'.format(value))
        dispatcher.utter_message(message)
        return []


class ActionConfirmArea(Action):
    def name(self):
        return 'confirm_area'

    def run(self, dispatcher, tracker, domain):
        value = tracker.current_slot_values()['area']
        if value == 'dontcare':
            message = 'Ok , a restaurant in any part of town is that right?'
        elif isinstance(value, str):
            message = 'Did you say you are looking for a restaurant in the {} of town?'.format(value)
        else:
            message = 'Ok , a restaurant in any part of town is that right?'
            logger.warning('unexpected area value when issuing confirm_area: {}'.format(value))
        dispatcher.utter_message(message)
        return []


class ActionConfirmSummary(Action):
    def name(self):
        return 'confirm_summary'

    def run(self, dispatcher, tracker, domain):
        """Which field to ask for is very random. Often the bot asks about the value that the human just provided on its
        previous utterance, but this is not guaranteed. So we'll simply pick a random filled slot and ask about it
        """
        '^Let me confirm , You are looking for a restaurant .* right\?$'
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        if len(filters) > 0:
            selected_slot = choice(list(filters.keys()))
            value = filters[selected_slot]
            if selected_slot == 'food':
                if value == 'dontcare':
                    message = 'Let me confirm , You are looking for a restaurant serving any kind of food right?'
                else:
                    message = 'Let me confirm , You are looking for a restaurant serving {} food right?'.format(value)
            elif selected_slot == 'pricerange':
                if value == 'dontcare':
                    message = 'Let me confirm , You are looking for a restaurant and you dont care about the price range ' \
                              'right?'
                else:
                    message = 'Let me confirm , You are looking for a restaurant in the {} price range right?'.format(value)
            elif selected_slot == 'area':
                if value == 'dontcare':
                    message = 'Let me confirm , You are looking for a restaurant in any part of town right?'
                else:
                    message = 'Let me confirm , You are looking for a restaurant in the {} of town right?'.format(value)
        else:  # if there were no filters set, we fall here
            logger.warning('predicted confirm_summary when there were no slots set')
            message = 'Let me confirm , You are looking for a restaurant , right?'
        dispatcher.utter_message(message)
        return []


class ActionFutileOfferRestaurant(Action):
    def name(self):
        return 'futile_offer_restaurant'

    def run(self, dispatcher, tracker, domain):
        results = tracker.current_slot_values()['results']
        name = '<name>'
        if results is not None:
            name = tracker.current_slot_values()['results'].\
            iloc[tracker.current_slot_values()['last_offer_index']]['name']
        else:
            logger.warning('predicted futile_offer_restaurant when there is no restaurant to refer to')
        message = '{name} is a great restaurant'.format(name=name)
        dispatcher.utter_message(message)
        return []
