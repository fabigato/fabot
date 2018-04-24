import argparse
import logging
from rasa_core import utils
import os
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from custom.memnet.model import MemNetPolicy, MemNetPolicyEnsemble, BabiT5Featurizer
from custom.memnet.data_utils import format_babi_data, build_batches, utterance_len, query_len
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
    model_directory = trainer.persist(PERSISTED_NLU_PATH, project_name='', fixed_model_name=NLU_T5_MODEL_NAME)
    return model_directory


def train_dialogue(domain_file=DOMAIN_TEMPLATES_FILE,
                   model_path=PERSISTED_DIALOG_UTTERS_PATH,
                   training_data_file=DIALOG_TRAINING_DATA_FILE):
    # agent = Agent(domain_file, policies=[KerasPolicy()])
    hops = 2
    h_len = utterance_len()
    embedding_size = 10
    batch = 32
    mem_size = 8
    keep_prob = 0.95
    epochs = 40
    clip_norm = 25
    print_cycle = 100
    trn_history, trn_query, trn_label, batch_indexes = build_batches(format_babi_data(BABI_TRN_DIALOG_FILE),
                                                                     batch_size=batch, max_memory_size=mem_size,
                                                                     utterance_length=h_len)
    dev_data = format_babi_data(BABI_DEV_DIALOG_FILE)
    dev_history, dev_query, dev_label, _ = build_batches(dev_data, batch_size=len(dev_data),
                                                         max_memory_size=mem_size,
                                                         utterance_length=h_len)
    agent = Agent(domain_file, policies=MemNetPolicyEnsemble([MemNetPolicy(trn_history, trn_query, trn_label,
                                                                           batch_indexes,
                                                                           featurizer=BabiT5Featurizer(mem_size),
                                                                           embedding_size=embedding_size,
                                                                           hops=hops)]))
    agent.train(
        filename=None,
        # max_history=2,
        # epochs=400,
        # batch_size=100,
        # validation_split=0.2,
        mn_dev_data={'history': dev_history, 'query': dev_query, 'label': dev_label}, mn_keep_prob=keep_prob,
        mn_epochs=epochs, mn_clip_norm=clip_norm, mn_print_cycle=print_cycle
    )
    # let's make the session a property of MemNetPolicy so we use the same for everything. Fuckers
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
            run(join(PERSISTED_NLU_PATH, NLU_T5_MODEL_NAME), PERSISTED_DIALOG_UTTERS_PATH)
        else:
            run(join(PERSISTED_NLU_PATH, NLU_T5_MODEL_NAME), PERSISTED_DIALOG_PATH)
