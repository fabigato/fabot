from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.events import SlotSet

logger = logging.getLogger(__name__)


class RestaurantAPI:
    def search(self, info):
        return "papi's pizza place"


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for restaurants")
        restaurant_api = RestaurantAPI()
        restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        return [SlotSet("matches", restaurants)]


class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("matches"))
        dispatcher.utter_message("is it ok for you? "
                                 "hint: I'm not going to "
                                 "find anything else :)")
        return []


class RestaurantPolicy(KerasPolicy):
    def model_architecture(self, num_features, num_actions, max_history_len):
        """Build a Keras model and return a compiled model."""
        from keras.layers import LSTM, Activation, Masking, Dense
        from keras.models import Sequential

        n_hidden = 32  # size of hidden layer in LSTM
        # Build Model
        batch_shape = (None, max_history_len, num_features)

        model = Sequential()
        model.add(Masking(-1, batch_input_shape=batch_shape))
        model.add(LSTM(n_hidden, batch_input_shape=batch_shape))
        model.add(Dense(input_dim=n_hidden, output_dim=num_actions))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        logger.debug(model.summary())
        return model


def train_dialogue(domain_file="restaurant_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/babi_stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), RestaurantPolicy()])

    agent.train(
            training_data_file,
            max_history=3,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer

    training_data = load_data('data/franken_data.json')
    trainer = Trainer(RasaNLUConfig("nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")

    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


def get_parser():
    parser = argparse.ArgumentParser(
        description='starts the bot')
    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "run", "test-nlu", "ner-cv-eval"],
        help="what the bot should do - e.g. run or train?")
    return parser


def rid_warnings():
    import os
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


def nlu_test(nlu_test_config, nlu_model_directory, nlu_data):
    import numpy as np
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.converters import load_data
    from rasa_nlu.evaluate import run_evaluation
    from rasa_nlu.evaluate import run_cv_evaluation
    from rasa_nlu.evaluate import prepare_data

    logger = logging.getLogger(__name__)

    nlu_config = RasaNLUConfig(nlu_test_config)

    # Evaluation
    run_evaluation(nlu_config, nlu_model_directory)

    # Cross validation evaluation: takes long!
    data = load_data(nlu_data)
    data = prepare_data(data, cutoff=5)
    folds = 10
    results = run_cv_evaluation(data, folds, nlu_config)
    logger.info("CV evaluation (n={})".format(folds))
    for k,v in results.items():
        logger.info("{}: {:.3f} ({:.3f})".format(k, np.mean(v), np.std(v)))

    logger.info("Finished evaluation")


def ner_cv_eval():
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.converters import load_data
    from rasa_nlu.evaluate import prepare_data
    import numpy as np
    from test_utils.ner import ner_cv
    results = ner_cv(prepare_data(load_data("data/franken_data.json"), cutoff=5), 3,
                          RasaNLUConfig("test_utils/data/config/crf_config.json"))
    for k, v in results.items():
        logger.info("{}: {:.3f} ({:.3f})".format(k, np.mean(v), np.std(v)))
    logger.info("Finished evaluation")


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    utils.configure_colored_logging(loglevel="INFO")
    rid_warnings()
    parser = get_parser()
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    elif task == "test-nlu":
        nlu_test(nlu_test_config="nlu_model_config.json", nlu_model_directory="models/nlu/current",
                  nlu_data="data/franken_data.json")
    elif task == "ner-cv-eval":
        ner_cv_eval()
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)
