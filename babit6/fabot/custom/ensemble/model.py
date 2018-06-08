from data.feature_factory import T6Featurizer
import argparse
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.models import model_from_json
from keras.utils import to_categorical
from keras.callbacks import BaseLogger, EarlyStopping
from data.babi_reader import BabiReader
from fabot.custom.memnet.model import MemoryNetwork
from fabot.custom.lstm.model import CustomLSTM
import pickle
from os.path import isfile, join
import logging
import numpy as np
from numpy import argmax
from copy import copy
from globals import PERSISTED_ENSEMBLE_T6, PERSISTED_T6_MEMNET_OFFLINE_PATH, PERSISTED_LSTM_OFFLINE_PATH, \
    BABI_T6_TRN_FILE, BABI_T6_DEV_FILE, BABI_T6_TST_FILE
import json
import re

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class CustomEnsemble(object):
    """
    Ensemble of action prediction models. It takes the action probability distributions from all models in the ensemble
    and decides an action from there. There are several possible decision policies that can be set at the constructor
    """
    def __init__(self, models, num_actions, policy='highest'):
        """
        :param models: List of models in the ensemble. A model should have a predict_turn(x) function returning its
        probability distribution given the current featurized turn. Models should be trained already and all should
        understand the same data points
        :param num_actions: number of available actions. Therefore, the predict_turn function of each model should
        return a List of this size
        :param policy: indicator for which ensemble policy to use. Valid options are 'highest' (default, always choose
        the answer with highest confidence), 'average' (use the average probability distribution of all models and pick
        the highest probability from this new distribution) or 'learned' (train an MLP to learn the right action using
        the probability distributions from all the models as features. In this case, use the train function to train
        the MLP)
        """
        self.models = models
        self.policy = policy
        if policy == 'learned':
            ensemble = Sequential()
            ensemble.add(Dense(500, input_dim=num_actions * len(models), activation='relu'))
            ensemble.add(Dense(200, activation='relu'))
            ensemble.add(Dense(100, activation='relu'))
            # ensemble.add(Dropout(rate=0.1))
            ensemble.add(Dense(num_actions, activation='softmax'))
            ensemble.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
            self.ensemble = ensemble

    def train_t6_custom_featurizers(self, train_filename, featurizers, epochs=10):
        """
        trains the mlp, assuming each model in the ensemble uses different training data. The constructor should have
        been called with policy='learned' for this to work
        :param train_filename: training filename
        :param featurizers: List of featurizers. featurizers[i] is used to featurize data points for models[i]
        :param epochs: duh
        """
        # for epoch in range(epochs):
        trn_data_filename = 'fabot/custom/ensemble_t6_trn_data.pickle'
        if isfile(trn_data_filename):
            with open(trn_data_filename) as fh:
                data = pickle.load(fh)
        else:
            data = {i: [] for i in range(len(self.models))}
            for story in BabiReader.babi_dialogue_iterator(train_filename):
                dialog = {i: [] for i in range(len(self.models))}
                for i, turn in enumerate(story):
                    for m in range(len(self.models)):
                        x = featurizers[m].featurize(user_text=turn['human'],
                                                     prev_bot_text='' if i == 0 else story[i - 1]['bot'], turn=i)
                        dialog[i].append({'x': np.array(x, dtype=np.float32),
                                          'y': featurizers[m].get_bot_utterance_act_id(turn['bot']),
                                          'e': copy(featurizers[m].slot_values)})
                for i, f in enumerate(featurizers):
                    f.reset()
                    data[i].append(dialog[i])
        # TODO now freaking train

    def format_babi_data(self, filename, featurizer):
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
        x, y, e = [], [], []
        for si, story in enumerate(BabiReader.babi_dialogue_iterator(filename)):
            logger.info('story {}'.format(si))
            for i, turn in enumerate(story):
                f = featurizer.featurize(user_text=turn['human'], prev_bot_text='' if i == 0 else story[i - 1]['bot'],
                                         turn=i)
                preds = np.array([])
                for model in self.models:
                    preds = np.concatenate((preds, model.predict_turn(f)))
                x.append(preds)
                y.append(featurizer.get_bot_utterance_act_id(turn['bot']))
                e.append(copy(featurizer.slot_values))
            for m in self.models:
                m.reset_conversation_state()
            featurizer.reset()
        return np.array(x), np.array(y), e

    def train_t6(self, trn_filename, featurizer, epochs=10, dev_filename=None):
        def load_data(saved_filename, input_filename):
            if isfile(saved_filename):
                with open(saved_filename, 'rb') as fh:
                    x, y, _ = pickle.load(fh)
            else:
                logger.info('no saved data found. Building it now')
                x, y, e = self.format_babi_data(input_filename, featurizer)
                with open(saved_filename, 'wb') as fh:
                    pickle.dump((x, y, e), fh)
                    logger.info('successfully saved data at {}'.format(saved_filename))
            return x, y
        x_trn, y_trn = load_data('fabot/custom/ensemble/saved_data/ensemble_t6_trn_{ent}_{feats}_data.pickle'.format(
            ent=args.entities, feats=args.features), trn_filename)
        y_trn = to_categorical(np.array(y_trn), num_classes=num_actions)
        if dev_filename:
            x_dev, y_dev = load_data('fabot/custom/ensemble/saved_data/ensemble_t6_dev_{ent}_data.pickle'.format(
                ent=args.entities, feats=args.features), dev_filename)
            y_dev = to_categorical(y_dev, num_classes=num_actions)
            # y_dev = to_categorical(np.array(y_dev), num_classes=num_actions)
            self.ensemble.fit(x_trn, y_trn, epochs=epochs, verbose=2, validation_data=(x_dev, y_dev),
                              callbacks=[BaseLogger(), EarlyStopping(monitor='val_acc', patience=2)])
        else:
            self.ensemble.fit(x_trn, y_trn, epochs=epochs, verbose=2)
        # if dev_filename:
        #     x_dev, y_dev = load_data('fabot/custom/ensemble_t6_dev_data.pickle', dev_filename)
        #     y_dev = to_categorical(y_dev, num_classes=num_actions)
        #     score = self.ensemble.evaluate(x_dev, y_dev, batch_size=128)
        #     logger.info('accuracy on dev: {}', score[1])
        # save
        model_json = self.ensemble.to_json()
        with open(join(PERSISTED_ENSEMBLE_T6.format(ent=args.entities, feats=args.features), 'model.json'),
                  "w") as json_file:
            json_file.write(model_json)
        self.ensemble.save_weights(join(PERSISTED_ENSEMBLE_T6.format(ent=args.entities,
                                                                     feats=args.features), 'model.h5'))
        logger.info('successfully persisted ensemble at {}'.format(PERSISTED_ENSEMBLE_T6.format(ent=args.entities,
                                                                                                feats=args.features)))

    def load(self, path):
        with open(join(path, 'model.json')) as json_config:
            loaded_model = json_config.read()
            loaded_model = model_from_json(loaded_model)
        loaded_model.load_weights(join(path, 'model.h5'))
        logger.info('successfully loaded ensemble model from {}'.format(path))
        self.ensemble = loaded_model

    def ensemble_predict(self, x):
        inputs = []
        for model in self.models:
            inputs.append(model.predict_turn(x))
        if self.policy == 'learned':
            input = np.concatenate(inputs)
            input = np.reshape(input, (1, input.shape[0]))
            prediction = self.ensemble.predict(input, batch_size=1)
        elif self.policy == 'highest':
            max_confidence = -1
            for candidate in inputs:
                confidence = np.max(candidate)
                if confidence > max_confidence:
                    max_confidence = confidence
                    prediction = candidate
        elif self.policy == 'average':
            prediction = np.mean(inputs, axis=0)
        else:
            raise ValueError('policy must be "highest", "average" or "learned". Got {}'.format(self.policy))
        return prediction

    def test_t6(self, featurizer):
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
                x = featurizer.featurize(user_text=turn['human'], prev_bot_text='' if i == 0 else story[i - 1]['bot'],
                                         turn=i)
                prediction = self.ensemble_predict(x)

                turn_results = dict()
                turn_results['human'] = turn['human']
                turn_results['target'] = turn['bot']
                actual_da = featurizer.get_bot_act(turn['bot'])
                predicted_da = featurizer.id2act(argmax(prediction))
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
            for m in self.models:
                m.reset_conversation_state()
        with open('fabot/custom/tst_t6_ensemble_offline_results_{policy}_{ent}.json'.format(
                policy=self.policy, ent=args.entities), 'w') as fh:
            json.dump(results, fh, indent=2)
        logging.info('test act match results:\n'
                     'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_act_matches, total_turns,
                                                                                    total_act_matches / total_turns,
                                                                                    perfect_act_dialogs, total_dialogs,
                                                                                    perfect_act_dialogs / total_dialogs)
                     )
        logging.info('test literal match results:\n'
                     'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.
                     format(total_literal_matches, total_turns, total_literal_matches / total_turns,
                            perfect_literal_dialogs, total_dialogs, perfect_literal_dialogs / total_dialogs))


def get_args():
    parser = argparse.ArgumentParser(
        description='train or test an ensemble with a MemNet and an LSTM for bAbI tasks 5 or 6')
    parser.add_argument('--job', choices=['train', 'test'], required=True,
                        help='train the ensemble or test an already trained one. Mandatory')
    parser.add_argument('--task', choices=['5', '6'], required=True, help='bAbI task, must be t5 or t6. Mandatory')
    parser.add_argument('--policy', choices=['average', 'highest', 'learned'], help='ensemble policy. "average" to use '
                                                                                    'average distribution of all '
                                                                                    'models, "highest" to use the '
                                                                                    'distribution with highest '
                                                                                    'confidence and "learned" to use '
                                                                                    'a model trained on the '
                                                                                    'distributions of the ensemble')
    parser.add_argument('--entities', choices=['regex', 'nlu'], required=True,
                        help='regex if you want to use basic pattern match to find entities. nlu if you want to use '
                             'Rasa NLU instead. Mandatory')
    parser.add_argument('--features', choices=['williams', 'rasa'], required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.features == 'williams':
        features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True, 'use_embeddings': True,
                    'use_intent': False, 'use_nlu_entity_extractor': args.entities == 'nlu', 'use_entities': True,
                    'use_context': True}
    else:  # Rasa
        features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': True, 'use_embeddings': False,
                    'use_intent': True, 'use_nlu_entity_extractor': args.entities == 'nlu', 'use_entities': True,
                    'use_context': True}
    if args.task == '6':
        if args.job == 'train':
            featurizer = T6Featurizer(**features)
            num_actions = T6Featurizer.num_actions()
            memnet = MemoryNetwork.load(PERSISTED_T6_MEMNET_OFFLINE_PATH.format(ent=args.entities, feats=args.features))
            lstm = CustomLSTM.load(PERSISTED_LSTM_OFFLINE_PATH.format(task=args.task, ent=args.entities,
                                                                      feats=args.features))
            ensemble = CustomEnsemble(models=[memnet, lstm], num_actions=num_actions, policy='learned')
            ensemble.train_t6(trn_filename=BABI_T6_TRN_FILE, featurizer=featurizer, epochs=35,
                              dev_filename=BABI_T6_DEV_FILE)
        if args.job == 'test':
            featurizer = T6Featurizer(**features)
            memnet = MemoryNetwork.load(PERSISTED_T6_MEMNET_OFFLINE_PATH.format(ent=args.entities, feats=args.features))
            lstm = CustomLSTM.load(PERSISTED_LSTM_OFFLINE_PATH.format(task=args.task, ent=args.entities, feats=args.features))
            ensemble = CustomEnsemble(models=[memnet, lstm], num_actions=T6Featurizer.num_actions(),
                                      policy=args.policy)
            ensemble.load(PERSISTED_ENSEMBLE_T6.format(ent=args.entities, feats=args.features))
            ensemble.test_t6(featurizer)
    if args.task == '5':
        raise NotImplementedError
