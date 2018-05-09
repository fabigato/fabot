import argparse
import logging
from rasa_core import utils
import os
from os.path import isfile
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from fabot.custom.ensemble import MemNetPolicyEnsemble
from fabot.custom.memnet.data_utils import MemNetT5DataAdapter, MemNetT6DataAdapter
from fabot.custom.memnet.model import MemNetT5Policy, MemNetT6Policy
from globals import *
import pickle

logger = logging.getLogger(__name__)


def init():
    utils.configure_colored_logging(loglevel="DEBUG")
    logging.basicConfig(level="DEBUG")
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


def get_args():
    parser = argparse.ArgumentParser(
        description='Fabot: a bot for the bAbI t6 challenge')
    parser.add_argument(
        '--action',
        choices=["train-nlu", "train-dialogue", "run", "test-nlu", "ner-cv-eval"],
        help="what the bot should do - e.g. run or train?")
    parser.add_argument('--task', choices=['5', '6'], help='bAbI task to perform on')
    return parser.parse_args()


def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer
    training_data = load_data(os.path.join(RASA_TRAIN_PATH, 'dstc2_nlu_trndev_new.json'))
    trainer = Trainer(RasaNLUConfig(NLU_TRAIN_CONFIG_FILE))
    trainer.train(training_data)
    model_directory = trainer.persist(NLU_MODEL_PATH, project_name='', fixed_model_name='t6new')  # NLU_T6_MODEL_NAME)
    return model_directory


def train_dialogue(task):
    if task == '5':
        babi_train_file = BABI_T5_TRN_FILE
        babi_dev_file = BABI_T5_DEV_FILE
        domain_file = DOMAIN_T5_FILE
        model_path = DIALOGUE_T5_MODEL_PATH
        data_adapter = MemNetT5DataAdapter()
        h_len = data_adapter.utterance_len()
        print_cycle = 100
        hops = 2
        embedding_size = 10
        batch = 32
        mem_size = 8
        keep_prob = 0.95
        epochs = 40
        clip_norm = 25
    else:  # task is 6
        babi_train_file = BABI_T6_TRN_FILE
        babi_dev_file = BABI_T6_DEV_FILE
        domain_file = DOMAIN_T6_FILE
        model_path = DIALOGUE_T6_MODEL_PATH
        data_adapter = MemNetT6DataAdapter(join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME))
        h_len = data_adapter.utterance_len()
        print_cycle = 100
        hops = 1
        embedding_size = 20
        batch = 32
        mem_size = 8
        epochs = 40
        clip_norm = 25
        keep_prob = 0.86

    trn_saved_data_filename = 'fabot/custom/memnet/t{}_trn_memnet_data.pickle'.format(task)
    if isfile(trn_saved_data_filename):
        with open(trn_saved_data_filename, 'rb') as trn_fh:
            trn_history, trn_query, trn_label, batch_indexes = pickle.load(trn_fh)
        print('successfully loaded MemoryNetwork formatted training data')
    else:
        print('not saved MemoryNetwork formatted training data found. Creating it now')
        trn_history, trn_query, trn_label, batch_indexes = data_adapter.build_batches(
            data_adapter.format_babi_data(babi_train_file),
            batch_size=batch, max_memory_size=mem_size,
            utterance_length=h_len)
        with open(trn_saved_data_filename, 'wb') as trn_fh:
            pickle.dump((trn_history, trn_query, trn_label, batch_indexes), trn_fh)
            print('saved formatted training data')
    dev_saved_data_filename = 'fabot/custom/memnet/t{}_dev_memnet_data.pickle'.format(task)
    if isfile(dev_saved_data_filename):
        with open(dev_saved_data_filename, 'rb') as dev_fh:
            dev_history, dev_query, dev_label = pickle.load(dev_fh)
        print('successfully loaded MemoryNetwork formatted dev data')
    else:
        print('not saved MemoryNetwork formatted dev data found. Creating it now')
        dev_data = data_adapter.format_babi_data(babi_dev_file)
        dev_history, dev_query, dev_label, _ = data_adapter.build_batches(dev_data, batch_size=len(dev_data),
                                                                          max_memory_size=mem_size,
                                                                          utterance_length=h_len)
        with open(dev_saved_data_filename, 'wb') as dev_fh:
            pickle.dump((dev_history, dev_query, dev_label), dev_fh)
            print('saved formatted dev data')
    if task == '5':
        policy = MemNetT5Policy(trn_history, trn_query, trn_label,
                                batch_indexes,
                                encoder=data_adapter,
                                embedding_size=embedding_size,
                                hops=hops)
    else:
        policy = MemNetT6Policy(trn_history, trn_query, trn_label,
                                batch_indexes,
                                encoder=data_adapter,
                                embedding_size=embedding_size,
                                hops=hops)
    agent = Agent(domain_file, policies=MemNetPolicyEnsemble([policy]))
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
    if args.action == "train-nlu":
        train_nlu()
    elif args.action == "train-dialogue":
        train_dialogue(args.task)
    elif args.action == "run":
        run()
