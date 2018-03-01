import argparse
import logging
from rasa_core import utils
import os

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


if __name__ == '__main__':
    init()
    args = get_args()
    pass
