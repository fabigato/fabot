import tensorflow as tf
from tensorflow.contrib.layers import xavier_initializer as xav
from globals import PERSISTED_T6_LSTM_OFFLINE_PATH, BABI_T6_TRN_FILE, BABI_T6_DEV_FILE, BABI_T6_TST_FILE
import logging
import numpy as np
from data.feature_factory import T6Featurizer
import pickle
from data.babi_reader import BabiReader
from copy import copy
from os.path import isfile, join
import json
import re
import argparse

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


class CustomLSTM(object):

    def __init__(self, input_dim, hidden_size=128, num_actions=16):

        self.input_dim = input_dim
        self.hidden_size = hidden_size
        self.num_actions = num_actions

        # build graph
        tf.reset_default_graph()

        # entry points
        x = tf.placeholder(tf.float32, [1, input_dim], name='X')
        init_state_c_, init_state_h_ = (tf.placeholder(tf.float32, [1, hidden_size]) for _ in range(2))
        action_ = tf.placeholder(tf.int32, name='label')
        action_mask_ = tf.placeholder(tf.float32, [num_actions], name='action_mask')

        # input projection
        Wi = tf.get_variable('Wi', [input_dim, hidden_size],
                             initializer=xav())
        bi = tf.get_variable('bi', [hidden_size],
                             initializer=tf.constant_initializer(0.))

        # add relu/tanh here if necessary
        projected_features = tf.matmul(x, Wi) + bi

        lstm_f = tf.contrib.rnn.LSTMCell(hidden_size, state_is_tuple=True)

        lstm_op, state = lstm_f(inputs=projected_features, state=(init_state_c_, init_state_h_))

        # reshape LSTM's state tuple (2,128) -> (1,256)
        state_reshaped = tf.concat(axis=1, values=(state.c, state.h))

        # output projection
        Wo = tf.get_variable('Wo', [2 * hidden_size, num_actions],
                             initializer=xav())
        bo = tf.get_variable('bo', [num_actions],
                             initializer=tf.constant_initializer(0.))
        # get logits
        logits = tf.matmul(state_reshaped, Wo) + bo
        # probabilities
        #  normalization : elemwise multiply with action mask
        probs = tf.multiply(tf.squeeze(tf.nn.softmax(logits)), action_mask_)

        # prediction
        prediction = tf.arg_max(probs, dimension=0)

        # loss
        loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=action_)

        # attach symbols to self
        self.loss = loss
        self.prediction = prediction
        self.probs = probs
        self.logits = logits
        self.state = state

        # attach placeholders
        self.features_ = x
        self.init_state_c_ = init_state_c_
        self.init_state_h_ = init_state_h_
        self.action_ = action_
        self.action_mask_ = action_mask_

        # start a session; attach to self
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        self.sess = sess
        # set init state to zeros
        self.init_state_c = np.zeros([1, self.hidden_size], dtype=np.float32)
        self.init_state_h = np.zeros([1, self.hidden_size], dtype=np.float32)

    def predict_turn(self, features):
        # forward
        action_mask = [1] * self.num_actions
        probs, prediction, state_c, state_h = self.sess.run([self.probs, self.prediction, self.state.c, self.state.h],
                                                            feed_dict={
                                                                self.features_: [features],
                                                                self.init_state_c_: self.init_state_c,
                                                                self.init_state_h_: self.init_state_h,
                                                                self.action_mask_: action_mask
                                                            })
        # maintain state
        self.init_state_c = state_c
        self.init_state_h = state_h
        # return argmax
        return probs

    def prediction(self, features):
        # forward
        action_mask = [1] * self.num_actions
        probs, prediction, state_c, state_h = self.sess.run([self.probs, self.prediction, self.state.c, self.state.h],
                                                            feed_dict={
                                                                self.features_: features.reshape([1, self.input_dim]),
                                                                self.init_state_c_: self.init_state_c,
                                                                self.init_state_h_: self.init_state_h,
                                                                self.action_mask_: action_mask
                                                            })
        # maintain state
        self.init_state_c = state_c
        self.init_state_h = state_h
        # return argmax
        return prediction

    # training
    def train_step(self, featurized_turn, action, action_mask, train_op):
        pred, _, loss_value, state_c, state_h = self.sess.run([self.prediction, train_op, self.loss, self.state.c,
                                                               self.state.h], feed_dict={
            self.features_: featurized_turn.reshape([1, self.input_dim]),
            self.action_: [action],
            self.init_state_c_: self.init_state_c,
            self.init_state_h_: self.init_state_h,
            self.action_mask_: action_mask
        })
        # maintain state
        self.init_state_c = state_c
        self.init_state_h = state_h
        return pred, loss_value

    def reset_conversation_state(self):
        # set init state to zeros
        self.init_state_c = np.zeros([1, self.hidden_size], dtype=np.float32)
        self.init_state_h = np.zeros([1, self.hidden_size], dtype=np.float32)

    def persist(self, path=PERSISTED_T6_LSTM_OFFLINE_PATH):
        config = {'input_dim': self.input_dim, 'hidden_size': self.hidden_size, 'num_actions': self.num_actions}
        with open(join(path, 'config.json'), 'w') as fh:
            json.dump(config, fh, indent=2)
        saver = tf.train.Saver()
        saver.save(self.sess, path, global_step=0)
        logging.info('successfully persisted the model at {}'.format(path))

    @staticmethod
    def load(path=PERSISTED_T6_LSTM_OFFLINE_PATH):
        with open(join(path, 'config.json')) as fh:
            config = json.load(fh)
        model = CustomLSTM(input_dim=config['input_dim'], hidden_size=config['hidden_size'],
                           num_actions=config['num_actions'])
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(path)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(model.sess, ckpt.model_checkpoint_path)
            logging.info('successfully restored LSTM model from {}'.format(path))
        else:
            logging.error('persisted model not found')
        return model


def format_babi_data(filename, featurizer):
    """
    produces bAbI data in a format suitable for the memory network. Each conversation provides as many training examples
    as turns.
    :param filename: bAbI conversation filename
    :param featurizer: featurizer object
    :return: List of dialogues, each dialogue is a sequence of training examples (turns). A turn is a dict with keys:
    x: List of floats, a featurized turn
    y: int, id of the target bot action
    e: Dictionary with the value of each entity at that point in the conversation (None, for those with no value set)
    """
    data = []
    for story in BabiReader.babi_dialogue_iterator(filename):
        dialog = []
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text='' if i == 0 else story[i-1]['bot'], turn=i)
            dialog.append({'x': np.array(x, dtype=np.float32), 'y': featurizer.get_bot_utterance_act_id(turn['bot']),
                           'e': copy(featurizer.slot_values)})
        featurizer.reset()
        data.append(dialog)
    return data


def train_t6():
    epochs = 12
    clip_norm = 1.
    logging.info('starting training\nConfig:\nactions: {}\ninput_dim: {}\nhidden_size: {}\nepochs: {}\ngradient clip '
                 'norm: {}\n'.format(num_actions, input_dim, hidden_size, epochs, clip_norm))
    saved_data = 'fabot/custom/lstm/t6_trn_lstm_offline_data.pickle'
    if isfile(saved_data):
        with open(saved_data, 'rb') as data_fh:
            trn_dialogs = pickle.load(data_fh)
    else:
        print('train data not found, now creating it')
        trn_dialogs = format_babi_data(filename=BABI_T6_TRN_FILE, featurizer=featurizer)
        print('saving data')
        with open(saved_data, 'wb') as data_fh:
            pickle.dump(trn_dialogs, data_fh)
        print('saved')
    saved_data = 'fabot/custom/lstm/t6_dev_lstm_offline_data.pickle'
    if isfile(saved_data):
        with open(saved_data, 'rb') as data_fh:
            dev_dialogs = pickle.load(data_fh)
    else:
        print('dev data not found, now creating it')
        dev_dialogs = format_babi_data(filename=BABI_T6_DEV_FILE, featurizer=featurizer)
        print('saving data')
        with open(saved_data, 'wb') as data_fh:
            pickle.dump(dev_dialogs, data_fh)
        print('saved')

    model = CustomLSTM(input_dim=input_dim, hidden_size=hidden_size, num_actions=num_actions)

    optimizer = tf.train.AdadeltaOptimizer(0.1)

    grads, vars = zip(*optimizer.compute_gradients(model.loss))
    grads_clipped, _ = tf.clip_by_global_norm(grads, clip_norm=clip_norm)
    train_op = optimizer.apply_gradients(zip(grads_clipped, vars))

    model.sess.run(tf.global_variables_initializer())
    total_turns = sum([len(dialog) for dialog in trn_dialogs])
    dev_total_turns = sum([len(dialog) for dialog in dev_dialogs])
    for epoch in range(epochs):
        total_loss = 0
        total_matches = 0
        perfect_dialogs = 0
        for dialog in trn_dialogs:
            dialog_matches = 0
            model.reset_conversation_state()
            for turn in dialog:
                pred, loss = model.train_step(featurized_turn=turn['x'], action=turn['y'],
                                              action_mask=[1] * num_actions, train_op=train_op)
                total_loss += loss
                dialog_matches += int(pred == turn['y'])
            total_matches += dialog_matches
            perfect_dialogs += int(dialog_matches == len(dialog))
        logging.info('epoch: {}\ttrn loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
            epoch, total_loss, total_matches, total_turns, total_matches/total_turns, perfect_dialogs, len(trn_dialogs),
            perfect_dialogs/len(trn_dialogs)))
        # evaluate in dev
        dev_total_loss = 0
        dev_total_matches = 0
        dev_perfect_dialogs = 0
        for dialog in dev_dialogs:
            dev_dialog_matches = 0
            for turn in dialog:
                pred = model.prediction(features=turn['x'])
                dev_total_loss += loss
                dev_dialog_matches += int(pred == turn['y'])
            dev_total_matches += dev_dialog_matches
            dev_perfect_dialogs += int(dev_dialog_matches == len(dialog))
        logging.info('dev loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
            dev_total_loss, dev_total_matches, dev_total_turns, dev_total_matches / dev_total_turns,
            dev_perfect_dialogs, len(dev_dialogs), dev_perfect_dialogs / len(dev_dialogs)))
    model.persist()


def test_t6_act_match():
    """tests act match vs test set"""
    model = CustomLSTM.load(path=PERSISTED_T6_LSTM_OFFLINE_PATH)
    saved_data = 'fabot/custom/lstm/t6_tst_lstm_offline_data.pickle'
    if isfile(saved_data):
        with open(saved_data, 'rb') as data_fh:
            tst_dialogs = pickle.load(data_fh)
    else:
        print('train data not found, now creating it')
        tst_dialogs = format_babi_data(filename=BABI_T6_TST_FILE, featurizer=featurizer)
        print('saving data')
        with open(saved_data, 'wb') as data_fh:
            pickle.dump(tst_dialogs, data_fh)
        print('saved')

    total_matches = 0
    perfect_dialogs = 0
    total_turns = sum([len(dialog) for dialog in tst_dialogs])
    for dialog in tst_dialogs:
        dialog_matches = 0
        for turn in dialog:
            pred = model.prediction(features=turn['x'])
            dialog_matches += int(pred == turn['y'])
        total_matches += dialog_matches
        perfect_dialogs += int(dialog_matches == len(dialog))
    logging.info('test accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_matches, total_turns, total_matches / total_turns, perfect_dialogs, len(tst_dialogs),
        perfect_dialogs / len(tst_dialogs)))


def produce_test_results_file():
    """tests literal match vs test set. Produces a json file with the results of both act and literal match"""
    model = CustomLSTM.load(path=PERSISTED_T6_LSTM_OFFLINE_PATH)

    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    total_turns = 11237
    total_dialogs = 1117
    for story in BabiReader.babi_dialogue_iterator(BABI_T6_TST_FILE):
        featurizer.reset()
        story_results = []
        dialog_act_matches, dialog_literal_matches = 0, 0
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text='' if i == 0 else story[i-1]['bot'], turn=i)
            pred = model.prediction(features=np.array(x, dtype=np.float32))
            turn_results = dict()
            turn_results['human'] = turn['human']
            turn_results['target'] = turn['bot']
            actual_da = featurizer.get_bot_act(turn['bot'])
            predicted_da = featurizer.id2act(pred)
            turn_results['actual'] = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
            turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                     string=turn_results['target']) is not None
            turn_results['act_match'] = actual_da == predicted_da
            story_results.append(turn_results)

            dialog_act_matches += int(turn_results['act_match'])
            dialog_literal_matches += int(turn_results['literal_match'])
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
        results.append(story_results)
    with open('tests/fabot/custom/lstm/tst_t6_lstm_offline_results.json', 'w') as fh:
        json.dump(results, fh, indent=2)
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_act_matches, total_turns, total_act_matches / total_turns, perfect_act_dialogs, total_dialogs,
        perfect_act_dialogs / total_dialogs))
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_literal_matches, total_turns, total_literal_matches / total_turns, perfect_literal_dialogs, total_dialogs,
        perfect_literal_dialogs / total_dialogs))


def get_args():
    parser = argparse.ArgumentParser(
        description='train or test an LSTM for bAbI tasks 5 or 6')
    parser.add_argument('--job', choices=['train', 'test'], required=True,
                        help='train the network or test an already trained one. Mandatory')
    parser.add_argument('--task', choices=['5', '6'], required=True, help='bAbI task, must be t5 or t6. Mandatory')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.task == '6':
        featurizer = T6Featurizer(use_bow=True, use_turn=True, use_bot_utter=True, use_embeddings=True,
                                  use_intent=False, use_nlu_entity_extractor=False, use_entities=True, use_context=True)
        num_actions = T6Featurizer.num_actions()
        input_dim = featurizer.feature_len()
        hidden_size = 128
        if args.job == 'train':
            train_t6()
        if args.job == 'test':
            produce_test_results_file()
    if args.task == '5':
        raise NotImplementedError
