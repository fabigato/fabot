from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.actions.action import ACTION_LISTEN_NAME
from numpy import argmax, max, exp


def softmax(z):
    e_x = exp(z - max(z))
    return e_x / e_x.sum()


class FabotPolicy(KerasPolicy):
    """
    Identical to KerasPolicy, but won't predict action listen if the previous action was also listen
    """
    def predict_action_probabilities(self, tracker, domain):
        probs = super(FabotPolicy, self).predict_action_probabilities(tracker, domain)
        if tracker.latest_action_name == ACTION_LISTEN_NAME:
            listen_idx = domain.action_map[ACTION_LISTEN_NAME][0]
            chosen_idx = argmax(probs)
            if chosen_idx == listen_idx:
                probs[listen_idx] = 0
                probs = softmax(probs)
        return probs