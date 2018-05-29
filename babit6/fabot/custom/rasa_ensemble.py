from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.actions.action import ACTION_LISTEN_NAME
from numpy import argmax, max, exp
from rasa_core.policies.ensemble import SimplePolicyEnsemble

def softmax(z):
    e_x = exp(z - max(z))
    return e_x / e_x.sum()


class FabotPolicy(KerasPolicy):
    """
    Identical to KerasPolicy, but does extra rule based-checks on the prediction
    """
    @staticmethod
    def _check_no_double_listen(probs, tracker, domain):
        """Ensures action listen is not predicted if the latest bot action was also action_listen"""
        if tracker.latest_action_name == ACTION_LISTEN_NAME:
            listen_idx = domain.action_map[ACTION_LISTEN_NAME][0]
            chosen_idx = argmax(probs)
            if chosen_idx == listen_idx:
                probs[listen_idx] = 0
                probs = softmax(probs)
        return probs

    @staticmethod
    def _is_predicted(action_name, probs, domain):
        return domain.action_map[action_name][0] == argmax(probs)

    @staticmethod
    def _check_business_rules(probs, tracker, domain):
        # slots = set(tracker.current_slot_values().keys()) |\
        #                {e['entity'] for e in tracker.latest_message.parse_data['entities']}
        slots = {**tracker.current_slot_values(),
                 **{e['entity']: e['value'] for e in tracker.latest_message.parse_data['entities']}}
        filled_informables = set(slots.keys()) & {'food', 'area', 'pricerange'}
        if 'food' in filled_informables:
            unwanted_actions = [domain.action_map[action][0] for action in ['confirm_ask_food']]
            for action in unwanted_actions:
                probs[action] = 0
        if 'area' in filled_informables:
            unwanted_actions = [domain.action_map[action][0] for action in ['confirm_ask_area', 'utter_request_area']]
            for action in unwanted_actions:
                probs[action] = 0
        if 'pricerange' in filled_informables:
            unwanted_actions = [domain.action_map[action][0] for action in ['confirm_ask_price']]
            for action in unwanted_actions:
                probs[action] = 0
        # more intricate rules

        # there are 2066 cases in which Fabot issues api call but target doesn't.
        # 628 out of those, target requests food. 402 asks for area and 194 times asks for price range. 63 times asks
        # to select price range

        # utter_select_food and utter_select_area never occur in test data

        # there are only 78 test cases where food is not present, at least one other informable is not present and yet
        # bot issues api_call. It is way more common to request food in these instances

        # there are 235 test cases where fabot says bye and target says another thing
        # don't say bye unless user said bye
        if FabotPolicy._is_predicted('utter_bye', probs, domain) \
                and tracker.latest_message.intent['name'] != 'bye':
            probs[domain.action_map['utter_bye'][0]] = 0

        # requested_slots = {k for k, v in slots.items() if k in {'phone', 'address', 'area', 'food', 'pricerange',
        #                                                         'postcode', 'signature'} and v == REQUESTED_ENTITY_FLAG}
        # only offer a field if user requested it
        # if tracker.latest_message.intent['name'] == 'request':
        #     requested_slots = {e['entity']: e['value'] for e in tracker.latest_message.parse_data['entities']
        #                        if e['value'] == REQUESTED_ENTITY_FLAG}
        #     # if 'area' in requested_slots:
        #     #     probs = [0] * len(probs)
        #     #     probs[domain.action_map['utter_offer_area'][0]] = 1
        #     # if 'phone' in requested_slots:
        #     #     probs = [0] * len(probs)
        #     #     probs[domain.action_map['offer_phone'][0]] = 1
        #     # if 'pricerange' in requested_slots:
        #     #     probs = [0] * len(probs)
        #     #     probs[domain.action_map['utter_offer_area'][0]] = 1
        probs = softmax(probs)
        return probs

    def predict_action_probabilities(self, tracker, domain):
        probs = super(FabotPolicy, self).predict_action_probabilities(tracker, domain)
        probs = FabotPolicy._check_no_double_listen(probs, tracker, domain)
        probs = FabotPolicy._check_business_rules(probs, tracker, domain)
        return probs


class MemNetPolicyEnsemble(SimplePolicyEnsemble):
    """
    A patch on Rasa's SimplePolicyEnsemble to bypass the need to have KerasPolicy's format training data. MemNet uses
    its own
    """
    def train(self, training_data, domain, featurizer, **kwargs):
        # type: (DialogueTrainingData, Domain, Featurizer, **Any) -> None
        """Same as PolicyEnsemble.train, just removing the check on training_data not being empty. Cause I want it
        empty!"""
        for policy in self.policies:
            policy.prepare(featurizer,
                           max_history=training_data.max_history())
            policy.train(training_data, domain, **kwargs)
            self.training_metadata.update(training_data.metadata)
