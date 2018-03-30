from rasa_core.actions import Action
from rasa_core.events import SlotSet
from data.database import BabiDB, NOT_PREFIX
from main import BABI_PATH
from os.path import join
import logging
from numpy.random import choice, seed
from main import DSTC2_ONTOLOGY_FILE
import json

seed(42)
db = BabiDB(babi_kb=join(BABI_PATH, 'dialog-babi-task6-dstc2-kb.txt'))
logger = logging.getLogger(__name__)

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
        message = 'no options available with the provided requirements'
    return message


def _produce_offer_restaurant_message(filters, name):
    filter_names = set(filters.keys())
    if filter_names == {'area', 'pricerange'}:
        message = '{name} is a nice place in the {area} of town and the prices are {pricerange}'.format(
            name=name,
            area=filters['area'],
            pricerange=filters['pricerange'])
    elif filter_names == {'area', 'food'}:
        message = '{name} is a nice place in the {area} of town serving tasty {food} food'.format(
            name=name, area=filters['area'], food=filters['food']
        )
    elif filter_names == {'area', 'food', 'pricerange'}:
        message = '{name} is a great restaurant serving {pricerange} {food} food in the {area} of town'.format(
            name=name, pricerange=filters['pricerange'], food=filters['food'], area=filters['area']
        )
    else:
        logger.info('unknown filter combination when producing offer restaurant message: {}'.format(filter_names))
        message = 'how about restaurant {name}?'.format(name=name)
    return message


def _build_request_answer(tracker, requested_entities):
    if tracker.current_slot_values()['last_offer_index'] is not None and \
            tracker.current_slot_values()['results'] is not None:
        rest = tracker.current_slot_values()['results'].iloc[tracker.current_slot_values()['last_offer_index']]
        message = []
        if 'address' in requested_entities:
            message.append('Sure , {name} is on {address}'.format(name=rest['name'], address=rest['address']))
        if 'phone' in requested_entities:
            message.append('The phone number of {name} is {phone}'.format(name=rest['name'], phone=rest['phone']))
        if 'pricerange' in requested_entities:
            message.append('{name} is in the {pricerange} price range'.format(name=rest['name'],
                                                                              pricerange=rest['pricerange']))
        if 'food' in requested_entities:
            message.append('{name} serves {food} food'.format(name=rest['name'], food=rest['food']))
        if 'postcode' in requested_entities:
            message.append('The post code of {name} is {postcode}'.format(name=rest['name'], postcode=rest['postcode']))
        if len({'area', 'name', 'signature'} & set(requested_entities.keys())) > 0:
            logger.warning('detected request with non requestable entities: {}, input: {}'.format(requested_entities),
                           tracker.latest_message.text)
        message = '. '.join(message)
    else:
        message = 'which restaurant are you talking about?'
    return message


def _search_and_inform(tracker, dispatcher):
    def search():
        results = db.find_restaurant(**filters)
        if len(results) == 0:
            message = _produce_unsuccessful_search_message(filters)
        else:
            message = _produce_offer_restaurant_message(filters, results.iloc[0]['name'])
        dispatcher.utter_message(message)
        return results

    filters = {var: value for var, value in tracker.current_slot_values().items() if
               var in ['food', 'pricerange', 'area'] and value not in [None, 'dontcare']}
    user_intent = tracker.latest_message.intent['name']
    if user_intent == 'request':
        requested_entities = {e['entity']: e['value'] for e in tracker.latest_message.entities}
        message = _build_request_answer(tracker, requested_entities)
        dispatcher.utter_message(message)
        return []
    elif user_intent == 'deny':
        # there are only 2 deny examples in training data, so it is unlikely we ever fall here in testing
        denied_entity = tracker.latest_message.entities[0]['entity']
        denied_value = tracker.latest_message.entities[0]['value']
        logger.info('processing a deny')
        filters[denied_entity] = NOT_PREFIX + denied_value
        results = search()
        return [SlotSet("results", results if len(results) > 0 else None),
                SlotSet("last_offer_index", 0 if len(results) > 0 else None)]
    elif user_intent == 'inform_dontcare':
        current_slot = tracker.current_slot_values()['current_slot']
        if current_slot in filters:
            del filters[current_slot]
        results = search()
        return [SlotSet("results", results if len(results) > 0 else None),
                SlotSet("last_offer_index", 0 if len(results) > 0 else None)]
    elif user_intent == 'query':
        results = search()
        requested_entities = {e['entity']: e['value'] for e in tracker.latest_message.entities
                              if e['entity'] not in ['food', 'area', 'pricerange']}
        if len(requested_entities) == 0:
            logger.warning('tried to perform query da, but all slots were informable')
            results = search()
            return [SlotSet("results", results if len(results) > 0 else None),
                    SlotSet("last_offer_index", 0 if len(results) > 0 else None)]
        else:
            message = _build_request_answer(tracker, requested_entities)
            dispatcher.utter_message(message)
            return [SlotSet("results", results if len(results) > 0 else None),
                    SlotSet("last_offer_index", 0 if len(results) > 0 else None)]
    elif user_intent == 'reqalts':
        results = tracker.current_slot_values()['results']
        if results is not None:
            current_index = tracker.current_slot_values()['last_offer_index'] + 1
            if current_index < len(results):
                message = _produce_offer_restaurant_message(filters, results.iloc[current_index]['name'])
                dispatcher.utter_message(message)
                return [SlotSet("last_offer_index", current_index)]
            else:
                message = _produce_no_more_options_message(filters)
                dispatcher.utter_message(message)
                return [SlotSet("last_offer_index", current_index - 1)]
        else:
            logger('user uttered reqalts when no results were available')
            message = 'What type of restaurant are you looking for?'
            dispatcher.utter_message(message)
            return []
    else:
        if user_intent not in ['inform', 'include_filter']:
            logger.warning('tried to perform a restaurant search with unexpected da: {}'.format(user_intent))
        results = search()
        return [SlotSet("results", results if len(results) > 0 else None),
                SlotSet("last_offer_index", 0 if len(results) > 0 else None)]


class ActionCantHelp(Action):
    def name(self):
        return 'canthelp'

    def run(self, dispatcher, tracker, domain):
        return _search_and_inform(tracker=tracker, dispatcher=dispatcher)


class ActionOffer(Action):
    def name(self):
        return 'offer'

    def run(self, dispatcher, tracker, domain):
        return _search_and_inform(tracker=tracker, dispatcher=dispatcher)


class ActionOfferDetailed(Action):
    def name(self):
        return 'offer_detailed'

    def run(self, dispatcher, tracker, domain):
        return _search_and_inform(tracker=tracker, dispatcher=dispatcher)


class ActionExplConf(Action):
    def name(self):
        return 'expl-conf'

    def run(self, dispatcher, tracker, domain):
        """Which field to ask for is very random. Often the bot asks about the value that the human just provided on its
        previous utterance, but this is not guaranteed. So we'll simply pick a random filled slot and ask about it
        """
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        selected_slot = choice(list(filters.keys()))
        value = filters[selected_slot]
        if selected_slot == 'food':
            if value == 'dontcare':
                message = choice(
                    ['You are looking for a restaurant serving any kind of food right?'])
            else:
                message = 'You are looking for a {} restaurant right?'.format(value)
        elif selected_slot == 'pricerange':
            if value == 'dontcare':
                message = 'Let me confirm , You are looking for a restaurant and you dont care about the price range ' \
                          'right?'
            else:
                message = 'Let me confirm , You are looking for a restaurant in the {} price range right?'.format(value)
        elif selected_slot == 'area':
            if value == 'dontcare':
                message = 'Ok , a restaurant in any part of town is that right?'
            else:
                message = 'Did you say you are looking for a restaurant in the {area} of town?'.format(area=value)
        dispatcher.utter_message(message)
        return []


class ActionSelect(Action):
    def name(self):
        return 'select'

    def run(self, dispatcher, tracker, domain):
        unset_slots = [var for var, value in tracker.current_slot_values().items() if
                       var in ['food', 'pricerange', 'area'] and value is None]
        if len(unset_slots) > 0:
            selected_slot = choice(unset_slots)
            value1, value2 = choice(ontology[selected_slot], size=2, replace=False)
            if selected_slot == 'food':
                if 'dontcare' in [value1, value2]:
                    other_value = value1 if value2 == 'dontcare' else value2
                    message = 'Sorry would you like {} food or you dont care'.format(other_value)
                else:
                    message = 'Sorry would you like {} or {} food'.format(value1, value2)
            elif selected_slot == 'pricerange':
                if 'dontcare' in [value1, value2]:
                    other_value = value1 if value2 == 'dontcare' else value2
                    message = 'Sorry would you like something in the {} price range or you dont care'.format(
                        other_value)
                else:
                    message = 'Sorry would you like something in the {} price range or in the {} price range'.format(
                        value1, value2)
            else:  # selected_slot == 'area':
                if 'dontcare' in [value1, value2]:
                    other_value = value1 if value2 == 'dontcare' else value2
                    message = 'Sorry would you like the {} of town or you dont care'.format(other_value)
                else:
                    message = 'Sorry would you like something in the {} or in the {}'.format(value1, value2)
            dispatcher.utter_message(message)
            return [SlotSet("current_slot", selected_slot)]
        else:
            logger.warning('bot predicted ActionSelect, but there are no currently unset slots')
            return _search_and_inform(tracker=tracker, dispatcher=dispatcher)


class ActionRequestAreaDetailed(Action):
    def name(self):
        return 'request_area_detailed'

    def run(self, dispatcher, tracker, domain):
        """The bot affirms there are available options with the provided slots, and then requests the value of
        area. Calling this action when area is already set is a mistake that will be logged but area will be
        requested anyway"""
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        if 'area' in filters:
            logger.warning('bot predicted request_area_detailed, but the area is already set. Uttering it anyway')
            del filters['area']
        num_results = db.num_results(**filters)
        other_slots = {s for s in filters}
        if other_slots == {'food'}:
            if filters['food'] == 'dontcare':
                message = "There are {} restaurants if you don't care about the food . What area do you want?".format(
                    num_results)
            else:
                message = 'There are {} restaurants serving {} food . What area do you want?'.format(num_results,
                                                                                                     filters['food'])
        elif other_slots == {'pricerange'}:
            if filters['pricerange'] == 'dontcare':  # never observed in test data
                message = "There are {} restaurants if you don't care about the price range . What area do you want?".\
                    format(num_results)
            else:
                message = 'There are {} restaurants in the {} price range . What area do you want?'.format(
                    num_results, filters['pricerange'])
        elif other_slots == {'food', 'pricerange'}:
            food, pricerange = filters['food'], filters['pricerange']
            if food == 'dontcare' and pricerange == 'dontcare':  # never observed
                message = 'There are {} restaurants if you don\'t care about the food in any price range . ' \
                          'What area would you like?'.format(num_results)
            elif food == 'dontcare' and pricerange != 'dontcare':  # never observed
                message = 'There are {} restaurants if you don\'t care about the food in the {} price range . ' \
                          'What area would you like?'.format(num_results, pricerange)
            elif food != 'dontcare' and pricerange == 'dontcare':
                message = 'There are {} restaurants serving {} in any price range . What area would you like?'.\
                    format(num_results, food)
            elif food != 'dontcare' and pricerange != 'dontcare':
                message = 'There are {} restaurants serving {} in the {} price range . What area would you like?'.\
                    format(num_results, food, pricerange)
        else:
            raise ValueError('Unknown combination of other slots when processing ActionRequestAreaDetailed: {}'.format(
                other_slots))
        dispatcher.utter_message(message)
        return [SlotSet("current_slot", 'area')]


class ActionRequestFoodDetailed(Action):
    def name(self):
        return 'request_food_detailed'

    def run(self, dispatcher, tracker, domain):
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        if 'food' in filters:
            logger.warning('bot predicted request_food_detailed, but the food is already set. Uttering it anyway')
            del filters['food']
        num_results = db.num_results(**filters)
        other_slots = {s for s in filters}
        if other_slots == {'area'}:
            if filters['area'] == 'dontcare':
                message = 'There are {} restaurants in all parts of town . What type of food do you want?'.format(
                    num_results)
            else:
                message = 'There are {} restaurants in the {} of town . What type of food do you want?'.format(
                    num_results, filters['area'])
        elif other_slots == {'pricerange'}:
            if filters['pricerange'] == 'dontcare':
                message = 'There are restaurants if you don\'t care about the price range . What type of food do ' \
                          'you want?'  # never observed in trn/dev/tst
            else:
                message = 'There are {} restaurants in the {} price range . What type of food do you want?'.format(
                    num_results, filters['pricerange'])
        elif other_slots == {'area', 'pricerange'}:
            area, pricerange = filters['area'], filters['pricerange']
            if area == 'dontcare' and pricerange == 'dontcare':
                message = 'There are restaurants if you don\'t care about the price range or area . What type of ' \
                          'food do you want?'  # never observed in trn/dev/tst
            elif area == 'dontcare' and pricerange != 'dontcare':
                message = 'There are restaurants in all parts of town in the {} price range . What type of food do ' \
                          'you want?'.format(pricerange)
            elif area != 'dontcare' and pricerange == 'dontcare':
                pass  # TODO
            elif area != 'dontcare' and pricerange != 'dontcare':
                message = 'There are {} restaurants in the {} price range and the {} of town . What type of food ' \
                          'would you like?'.format(num_results, pricerange, area)
        else:
            raise ValueError('Unknown combination of other slots when processing ActionRequestAreaDetailed: {}'.format(
                other_slots))
        dispatcher.utter_message(message)
        return [SlotSet("current_slot", 'food')]


class ActionRequestPricerangeDetailed(Action):
    def name(self):
        return 'request_pricerange_detailed'

    def run(self, dispatcher, tracker, domain):
        filters = {var: value for var, value in tracker.current_slot_values().items() if
                   var in ['food', 'pricerange', 'area'] and value is not None}
        if 'pricerange' in filters:
            logger.warning('bot predicted request_pricerange_detailed, but the food is already set. Uttering it anyway')
            del filters['pricerange']
        num_results = db.num_results(**filters)
        other_slots = {s for s in filters}
        if other_slots == {'area'}:
            if filters['area'] == 'dontcare':
                message = 'There are {} restaurants in all parts of town . What type of pricerange do you want?'.format(
                    num_results)
            else:
                pass  # TODO
        elif other_slots == {'food'}:
            if filters['food'] == 'dontcare':
                message = 'There are {} restaurants if you don\'t care about the food . What price range do you want?'.\
                    format(num_results)
            else:
                message = 'There are {} restaurants serving {} food . What price range do you want?'.format(
                    num_results, filters['food'])
        elif other_slots == {'area', 'food'}:
            area, food = filters['area'], filters['food']
            if area == 'dontcare' and food == 'dontcare':
                message = 'There are {} restaurants if you don\'t care about the area or the type of food . What ' \
                          'price range would you like?'.format(num_results)
            elif area == 'dontcare' and food != 'dontcare':
                message = 'There are {} restaurants serving {} food in any part of town . What price range would you'
                ' like?'.format(num_results, food)
            elif area != 'dontcare' and food == 'dontcare':
                message = 'There are {} restaurants in the {} of town serving any kind of food . What price range ' \
                          'would you like?'.format(num_results, area)
            elif area != 'dontcare' and food != 'dontcare':
                message = 'There are {} restaurants serving {} in the {} of town . What price range would you like?'.\
                    format(num_results, food, area)
        else:
            raise ValueError('Unknown combination of other slots when processing ActionRequestAreaDetailed: {}'.format(
                other_slots))
        dispatcher.utter_message(message)
        return [SlotSet("current_slot", 'pricerange')]
