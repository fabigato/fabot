import argparse
import logging
from rasa_core import utils
import os
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel, ConsoleOutputChannel

logger = logging.getLogger(__name__)


def init():
    utils.configure_colored_logging(loglevel="INFO")
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
    training_data = load_data('data/test_nlu_output_confirm_request.json')
    trainer = Trainer(RasaNLUConfig("nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', project_name='fabot', fixed_model_name="current")
    return model_directory


def run():
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
    for text in texts:
        parse_data = interpreter.parse(text)
    pass


if __name__ == '__main__':
    init()
    args = get_args()
    if args.task == "train-nlu":
        train_nlu()
    elif args.task == "run":
        run()
