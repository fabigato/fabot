import tensorflow as tf
from tensorflow.contrib.layers import xavier_initializer as xav
from globals import PERSISTED_LSTM_PATH, BABI_T6_TRN_FILE, BABI_T6_DEV_FILE, BABI_T6_TST_FILE, \
    BABI_T5_TRN_FILE, BABI_T5_DEV_FILE, BABI_T5_TST_FILE, BABI_T5_TST_OOV_FILE
import logging
import numpy as np
from data.feature_factory import T6Featurizer, T5Featurizer
import pickle
from data.babi_reader import BabiReader
from copy import copy
from os.path import isfile, join, exists
import json
import re
import argparse
from os import mkdir

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
        self.predicted_action = prediction
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
        probs, prediction, state_c, state_h = self.sess.run([self.probs, self.predicted_action, self.state.c, self.state.h],
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
        probs, prediction, state_c, state_h = self.sess.run([self.probs, self.predicted_action, self.state.c, self.state.h],
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
        pred, _, loss_value, state_c, state_h = self.sess.run([self.predicted_action, train_op, self.loss, self.state.c,
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

    def persist(self, path):
        config = {'input_dim': self.input_dim, 'hidden_size': self.hidden_size, 'num_actions': self.num_actions}
        if not exists(path):
            mkdir(path)
        with open(join(path, 'config.json'), 'w') as fh:
            json.dump(config, fh, indent=2)
        saver = tf.train.Saver()
        saver.save(self.sess, path, global_step=0)
        logging.info('successfully persisted the model at {}'.format(path))

    @staticmethod
    def load(path):
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


def bot_prev_utter(story, turn, prev_pred):
    if turn == 0:
        return ''
    elif args.bot_prev == 'offline':
        return story[turn - 1]['bot']
    elif args.bot_prev == 'online':
        return prev_pred
    elif args.bot_prev == 'no':
        return prev_pred  # just to update the current rest correctly
    else:
        raise ValueError('bot-prev argument should be online, offline or no. Received {}'.format(args.bot_prev))


def train(task):
    if task == '6':
        trn_file = BABI_T6_TRN_FILE
        dev_file = BABI_T6_DEV_FILE
    elif task == '5':
        trn_file = BABI_T5_TRN_FILE
        dev_file = BABI_T5_DEV_FILE
    epochs = 35
    clip_norm = 1.
    logging.info('starting training\nConfig:\nactions: {}\ninput_dim: {}\nhidden_size: {}\nepochs: {}\ngradient clip '
                 'norm: {}\n'.format(num_actions, input_dim, hidden_size, epochs, clip_norm))
    saved_data = 'fabot/custom/lstm/saved_data/t{task}_trn_lstm_{bot_prev}_{ent}_{feats}_data.pickle'.format(
        task=task, ent=args.entities, feats=args.features,
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline')  # online is no valid train setting
    if isfile(saved_data):
        with open(saved_data, 'rb') as data_fh:
            trn_dialogs = pickle.load(data_fh)
    else:
        print('train data not found, now creating it')
        trn_dialogs = format_babi_data(filename=trn_file, featurizer=featurizer)
        print('saving data')
        with open(saved_data, 'wb') as data_fh:
            pickle.dump(trn_dialogs, data_fh)
        print('saved')
    saved_data = 'fabot/custom/lstm/saved_data/t{task}_dev_lstm_{bot_prev}_{ent}_{feats}_data.pickle'.format(
        task=task, ent=args.entities, feats=args.features,
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline')
    if isfile(saved_data):
        with open(saved_data, 'rb') as data_fh:
            dev_dialogs = pickle.load(data_fh)
    else:
        print('dev data not found, now creating it')
        dev_dialogs = format_babi_data(filename=dev_file, featurizer=featurizer)
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
    highest_dev_matches = 0
    chances2improve = 5
    stop = False
    for epoch in range(epochs):
        if stop:
            break
        total_loss = 0
        total_matches = 0
        perfect_dialogs = 0
        for di, dialog in enumerate(trn_dialogs):
            dialog_matches = 0
            model.reset_conversation_state()
            for turn in dialog:
                pred, loss = model.train_step(featurized_turn=turn['x'], action=turn['y'],
                                              action_mask=[1] * num_actions, train_op=train_op)
                total_loss += loss
                dialog_matches += int(pred == turn['y'])
            total_matches += dialog_matches
            perfect_dialogs += int(dialog_matches == len(dialog))
        logging.info('epoch: {}\ttrn loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({:.2%})'.format(
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
        logging.info('dev loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({:.2%})'.format(
            dev_total_loss, dev_total_matches, dev_total_turns, dev_total_matches / dev_total_turns,
            dev_perfect_dialogs, len(dev_dialogs), dev_perfect_dialogs / len(dev_dialogs)))
        if dev_total_matches >= highest_dev_matches:
            highest_dev_matches = dev_total_matches
            chances2improve = 5
            model.persist(path=PERSISTED_LSTM_PATH.format(
                task=task, ent=args.entities, feats=args.features,
                bot_prev=args.bot_prev if args.bot_prev != 'online' else 'noprev'))
        else:
            chances2improve -= 1
            if chances2improve == 0:
                logger.info('no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                stop = True


def test_act_match(task):
    """tests act match vs test set"""
    if task == '6':
        tst_file = BABI_T6_TST_FILE
    elif task == '5':
        tst_file = BABI_T5_TST_FILE
    model = CustomLSTM.load(path=PERSISTED_LSTM_PATH.format(
        task=task, ent=args.entities, feats=args.features,
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'noprev'))
    saved_data = 'fabot/custom/lstm/t{task}_tst_lstm_act{prev}_data.pickle'.format(
        task=task, prev='_noprev' if args.bot_prev == 'no' else '')
    if isfile(saved_data):
        with open(saved_data, 'rb') as data_fh:
            tst_dialogs = pickle.load(data_fh)
    else:
        print('train data not found, now creating it')
        tst_dialogs = format_babi_data(filename=tst_file, featurizer=featurizer)
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
            pred = model.predicted_action(features=turn['x'])
            dialog_matches += int(pred == turn['y'])
        total_matches += dialog_matches
        perfect_dialogs += int(dialog_matches == len(dialog))
    logging.info('test accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_matches, total_turns, total_matches / total_turns, perfect_dialogs, len(tst_dialogs),
        perfect_dialogs / len(tst_dialogs)))


def produce_test_results_file(task):
    """tests literal match vs test set. Produces a json file with the results of both act and literal match"""
    model = CustomLSTM.load(path=PERSISTED_LSTM_PATH.format(
        task=task, ent=args.entities, feats=args.features,
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline'))
    if task == '6':
        tst_file = BABI_T6_TST_FILE
        total_turns = 11237
        total_dialogs = 1117
    elif task == '5':
        tst_file = BABI_T5_TST_FILE if not args.oov else BABI_T5_TST_OOV_FILE
        total_turns = 18398 if not args.oov else 18368
        total_dialogs = 1000
    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    for si, story in enumerate(BabiReader.babi_dialogue_iterator(tst_file)):
        print('\rstory {}'.format(si+1), end="", flush=True)
        featurizer.reset()
        story_results = []
        dialog_act_matches, dialog_literal_matches = 0, 0
        prev_pred = ''  # just to have an initial previous prediction
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text=bot_prev_utter(story, i, prev_pred), turn=i)
            pred = model.prediction(features=np.array(x, dtype=np.float32))
            turn_results = dict()
            turn_results['human'] = turn['human']
            turn_results['target'] = turn['bot']
            actual_da = featurizer.get_bot_act(turn['bot'])
            predicted_da = featurizer.id2act(pred)
            prev_pred = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
            turn_results['actual'] = prev_pred
            turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                     string=turn_results['target']) is not None
            turn_results['act_match'] = actual_da == predicted_da
            story_results.append(turn_results)

            dialog_act_matches += int(turn_results['act_match'])
            dialog_literal_matches += int(turn_results['literal_match'])
        model.reset_conversation_state()
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
        results.append(story_results)
    with open('fabot/custom/lstm/results/tst_t{task}_lstm_{bot_prev}_{ent}_{feats}_{oov}results.json'.format(
            task=task, ent=args.entities, feats=args.features, bot_prev=args.bot_prev, oov='oov_' if args.oov else ''),
              'w') as fh:
        json.dump(results, fh, indent=2)
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_act_matches, total_turns,
                                                                                total_act_matches / total_turns,
                                                                                perfect_act_dialogs, total_dialogs,
                                                                                perfect_act_dialogs / total_dialogs))
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_literal_matches, total_turns,
                                                                                total_literal_matches / total_turns,
                                                                                perfect_literal_dialogs, total_dialogs,
                                                                                perfect_literal_dialogs / total_dialogs
                                                                                ))


def get_args():
    parser = argparse.ArgumentParser(
        description='train or test an LSTM for bAbI tasks 5 or 6')
    parser.add_argument('--job', choices=['train', 'test'], required=True,
                        help='train the network or test an already trained one. Mandatory')
    parser.add_argument('--task', choices=['5', '6'], required=True, help='bAbI task, must be t5 or t6. Mandatory')
    parser.add_argument('--entities', choices=['regex', 'nlu'], required=True,
                        help='regex if you want to use basic pattern match to find entities. nlu if you want to use '
                             'Rasa NLU instead. Mandatory')
    parser.add_argument('--features', choices=['williams', 'rasa'], required=True)
    parser.add_argument('--bot-prev', choices=['online', 'offline', 'no'], required=True,
                        help="'online' to use the actual bot last prediction as a feature. 'offline' to use the ground "
                             "truth previous prediction instead. 'no' to not use that feature at all")
    parser.add_argument('--oov', action='store_true', default=False, help='use OOV test file for task 5')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.task == '6':
        if args.features == 'williams':
            features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': args.bot_prev != 'no',
                        'use_embeddings': True, 'use_intent': False, 'use_nlu_entity_extractor': args.entities == 'nlu',
                        'use_entities': True, 'use_context': True}
        else:  # Rasa
            features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': args.bot_prev != 'no',
                        'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': args.entities == 'nlu',
                        'use_entities': True, 'use_context': True}
        featurizer = T6Featurizer(**features)
        num_actions = T6Featurizer.num_actions()
        input_dim = featurizer.feature_len()
        hidden_size = 128
        if args.job == 'train':
            train(args.task)
        if args.job == 'test':
            produce_test_results_file(args.task)
    if args.task == '5':
        if args.features == 'williams':
            features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': args.bot_prev != 'no',
                        'use_embeddings': True, 'use_intent': False, 'use_nlu_entity_extractor': args.entities == 'nlu',
                        'use_entities': True, 'use_context': False, 'use_oov': args.oov}
        else:  # Rasa
            features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': args.bot_prev != 'no',
                        'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': args.entities == 'nlu',
                        'use_entities': True, 'use_context': False, 'use_oov': args.oov}
        featurizer = T5Featurizer(**features)
        num_actions = T5Featurizer.num_actions()
        input_dim = featurizer.feature_len()
        hidden_size = 128
        if args.job == 'train':
            train(task=args.task)
        if args.job == 'test':
            produce_test_results_file(args.task)
