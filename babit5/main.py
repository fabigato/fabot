import argparse
import logging
from rasa_core import utils
import os
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from globals import *
from rasa_core.channels.console import ConsoleInputChannel

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def init():
    logging.basicConfig(level="DEBUG")
    utils.configure_colored_logging(loglevel="DEBUG")
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


def get_args():
    parser = argparse.ArgumentParser(
        description='Fabot t5. A bot for the bAbI dialog task 5')
    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "run", "test-nlu"],
        help="what the bot should do - e.g. run or train?")
    parser.add_argument('--template-based', action='store_true', default=False, help='train/run a dialog system '
                                                                                     'completely based on answer '
                                                                                     'templates with no actual '
                                                                                     'database backend')
    return parser.parse_args()


def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer
    training_data = load_data(NLU_TRAINING_DATA_FILE)
    trainer = Trainer(RasaNLUConfig(NLU_CONFIG_FILE))
    trainer.train(training_data)
    model_directory = trainer.persist(PERSISTED_NLU_PATH, project_name='', fixed_model_name=NLU_MODEL_NAME)
    return model_directory


def train_dialogue(domain_file=DOMAIN_TEMPLATES_FILE,
                   model_path=PERSISTED_DIALOG_PATH,
                   training_data_file=DIALOG_TRAINING_DATA_FILE):
    agent = Agent(domain_file, policies=[KerasPolicy()])

    agent.train(
            training_data_file,
            max_history=2,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )
    agent.persist(model_path)
    return agent


def run(interpreter_path, dialog_path):
    interpreter = RasaNLUInterpreter(interpreter_path)
    agent = Agent.load(dialog_path, interpreter=interpreter)
    agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    init()
    args = get_args()
    if args.task == "train-nlu":
        train_nlu()
    elif args.task == "train-dialogue":
        if args.template_based:
            train_dialogue(DOMAIN_TEMPLATES_FILE, PERSISTED_DIALOG_UTTERS_PATH, DIALOG_TRAINING_DATA_UTTER_FILE)
        else:
            train_dialogue(DOMAIN_CODE_FILE, PERSISTED_DIALOG_PATH, DIALOG_TRAINING_DATA_FILE)
    elif args.task == "run":
        if args.template_based:
            run(join(PERSISTED_NLU_PATH, NLU_MODEL_NAME), PERSISTED_DIALOG_UTTERS_PATH)
        else:
            run(join(PERSISTED_NLU_PATH, NLU_MODEL_NAME), PERSISTED_DIALOG_PATH)
