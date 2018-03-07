import argparse
import logging
from rasa_core import utils
import os
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel, ConsoleOutputChannel
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

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
    training_data = load_data('data/test_nlu_output_confirm_request.json')
    trainer = Trainer(RasaNLUConfig("nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', project_name='fabot', fixed_model_name="current")
    return model_directory


def train_dialogue(domain_file="fabot_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/stories_limited.md"):
    agent = Agent(domain_file,
                  # policies=[MemoizationPolicy(), KerasPolicy()])
                  policies=[KerasPolicy()])

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
