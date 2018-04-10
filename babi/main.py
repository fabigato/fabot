import argparse
import logging
from rasa_core import utils
import os
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.policies.keras_policy import KerasPolicy
from fabot.custom.ensemble import FabotPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from globals import *

logger = logging.getLogger(__name__)


def init():
    utils.configure_colored_logging(loglevel="DEBUG")
    logging.basicConfig(level="DEBUG")
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


def get_args():
    parser = argparse.ArgumentParser(
        description='Fabot: a bot for the bAbI t6 challenge')
    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "run", "test-nlu", "ner-cv-eval"],
        help="what the bot should do - e.g. run or train?")
    return parser.parse_args()


def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer
    training_data = load_data(os.path.join(RASA_TRAIN_PATH, 'dstc2_nlu_train.json'))
    trainer = Trainer(RasaNLUConfig(NLU_TRAIN_CONFIG_FILE))
    trainer.train(training_data)
    model_directory = trainer.persist(NLU_MODEL_PATH, project_name='fabot', fixed_model_name="current")
    return model_directory


def train_dialogue(domain_file=DOMAIN_FILE,
                   model_path=DIALOGUE_MODEL_PATH,
                   training_data_file=RASA_TRAIN_PATH + 'stories.md'):
    agent = Agent(domain_file,
                  # policies=[MemoizationPolicy(), KerasPolicy()])
                  # policies=[KerasPolicy()])
                  policies=[FabotPolicy()])

    agent.train(
            training_data_file,
            max_history=3,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def test_nlu():
    from rasa_core.channels.channel import UserMessage
    interpreter = RasaNLUInterpreter("models/nlu/fabot/current")
    # agent = Agent.load("models/dialogue", interpreter=interpreter)
    # agent.handle_channel(ConsoleInputChannel())
    # return agent
    texts = [
            'what is the telephone number',
            'what is the signature dish',
            'do they make indian food',
            'please give me the address and phone number',
            'what is the specialty',
            'what is the signature',
            'do they prepare chinese food',
            'what is the specialty of this place'
        ]
    print(texts)
    for text in texts:
        parse_data = interpreter.parse(text)
    pass


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/fabot/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)
    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    init()
    args = get_args()
    if args.task == "train-nlu":
        train_nlu()
    elif args.task == "train-dialogue":
        train_dialogue()
    elif args.task == "run":
        run()
