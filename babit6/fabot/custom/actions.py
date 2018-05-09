from rasa_core.actions import Action


class ActionAPICall(Action):
    def name(self):
        return 'api_call'

    def run(self, dispatcher, tracker, domain):
        food = tracker.current_slot_values()['cuisine'] if tracker.current_slot_values()['cuisine'] else 'R_cuisine'
        area = tracker.current_slot_values()['location'] if tracker.current_slot_values()['location'] else 'R_location'
        pricerange = tracker.current_slot_values()['price'] if tracker.current_slot_values()['price'] \
            else 'R_price'
        dispatcher.utter_message('api_call {} {} {}'.format(food, area, pricerange))
        return []


class ActionOfferRestAreaPrice(Action):
    def name(self):
        return 'offer_rest_area_price'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        area = tracker.current_slot_values()['location']
        pricerange = tracker.current_slot_values()['price']
        dispatcher.utter_message('_restaurant_ is a nice place in the {area} of town and the prices are {pricerange}'.
                                 format(area=area, pricerange=pricerange))
        return []


class ActionOfferRestAreaFood(Action):
    def name(self):
        return 'offer_rest_area_food'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        area = tracker.current_slot_values()['location']
        food = tracker.current_slot_values()['cuisine']
        dispatcher.utter_message('_restaurant_ is a nice place in the {area} of town serving tasty {food} food'.
                                 format(area=area, food=food))
        return []


class ActionOfferRestAreaFoodPrice(Action):
    def name(self):
        return 'offer_rest_area_food_price'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        pricerange = tracker.current_slot_values()['price']
        food = tracker.current_slot_values()['cuisine']
        area = tracker.current_slot_values()['location']
        dispatcher.utter_message('_restaurant_ is a great restaurant serving {pricerange} \w+ food in '
                                 'the \w+ of town .'.format(pricerange=pricerange, food=food, area=area))
        return []


class ActionOfferRestArea(Action):
    def name(self):
        return 'offer_rest_area'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        area = tracker.current_slot_values()['location']
        dispatcher.utter_message('_restaurant_ is a nice place in the {area} of town'.format(area=area))
        return []


class ActionOfferRestFoodPrice(Action):
    def name(self):
        return 'offer_rest_food_price'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        pricerange = tracker.current_slot_values()['price']
        food = tracker.current_slot_values()['cuisine']
        dispatcher.utter_message('_restaurant_ serves {food} food in the {pricerange} price range'.format(
            food=food, pricerange=pricerange))
        return []


class ActionOfferRestFood(Action):
    def name(self):
        return 'offer_rest_food'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        food = tracker.current_slot_values()['cuisine']
        dispatcher.utter_message('_restaurant_ serves {food} food'.format(food=food))
        return []


class ActionOfferRestPrice(Action):
    def name(self):
        return 'offer_rest_price'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        pricerange = tracker.current_slot_values()['price']
        dispatcher.utter_message('_restaurant_ is in the {pricerange} price range'.format(pricerange=pricerange))
        return []


class ActionOfferRestPricePostcode(Action):
    def name(self):
        return 'offer_rest_price_postcode'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        pricerange = tracker.current_slot_values()['price']
        dispatcher.utter_message('_restaurant_ is in the {pricerange} price range , and their post code is _postcode_'.
                                 format(pricerange=pricerange))
        return []


class ActionOfferRest(Action):
    def name(self):
        return 'offer_rest'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        dispatcher.utter_message('_restaurant_ is a great restaurant')
        return []


class ActionGivePhone(Action):
    def name(self):
        return 'give_phone'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        dispatcher.utter_message('The phone number of _restaurant_ is _phone_')
        return []


class ActionGivePhone2(Action):
    def name(self):
        return 'give_phone2'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        food = tracker.current_slot_values()['cuisine']
        dispatcher.utter_message('_restaurant_ is a great restaurant serving {food} food . Their phone number '
                                 'is _phone_ .'.format(food=food))
        return []


class ActionGivePostcode(Action):
    def name(self):
        return 'give_postcode'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        dispatcher.utter_message('The post code of _restaurant_ is _postcode_')
        return []


class ActionGiveAddress(Action):
    def name(self):
        return 'give_address'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        dispatcher.utter_message('The address of _restaurant is _address_ .')
        return []


class ActionGiveArea(Action):
    def name(self):
        return 'give_area'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        area = tracker.current_slot_values()['location']
        dispatcher.utter_message('Sure , _restaurant is on {area}'.format(area=area))
        return []


class ActionGiveAddress2(Action):
    def name(self):
        return 'give_address2'

    def run(self, dispatcher, tracker, domain):
        # TODO query a database
        dispatcher.utter_message('_restaurant_ is on _address_')
        return []
