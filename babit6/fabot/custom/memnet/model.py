import tensorflow as tf
from fabot.custom.memnet.data_utils import MemNetT5DataAdapter, MemNetT6DataAdapter
from data.feature_factory import T6Featurizer, T5Featurizer
from data.database import BabiDB
from globals import BABI_T6_KB_FILE, BABI_T6_TRN_FILE, BABI_T6_DEV_FILE, BABI_T6_TST_FILE, \
    PERSISTED_MEMNET_PATH, BABI_T5_TRN_FILE, BABI_T5_DEV_FILE, \
    BABI_T5_TST_FILE, BABI_T5_TST_OOV_FILE
from rasa_core.policies import Policy
from rasa_core.events import ActionExecuted
from rasa_core.actions.action import ACTION_LISTEN_NAME
from numpy import mean, exp, argmax
from os.path import join, isfile, exists
from os import mkdir
import logging
import pickle
import argparse
from data.babi_reader import BabiReader
from copy import copy
import re
import json

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def softmax(z):
    e_x = exp(z - max(z))
    return list(e_x / e_x.sum())


def batch_matmul(x, A):
    """
    Apply tf.matmul with a matrix on a tensor with rank higher than 2
    This can be done with scan, but this performs better
    (https://stackoverflow.com/questions/38235555/tensorflow-matmul-of-input-matrix-with-batch-data/43829731#43829731)
    :param x: first tensor in the dot product
    :param A: matrix (second element in the dot product). Its first dimension must be equal to the last dimension of x
    :return: a tensor that preserves all of x' dimensions except the last. Dot product with A is applied to each element
    in the last dimension of x. Every other dimension is preserved
    """
    prod = tf.reshape(x, [-1, x.shape[-1]])
    prod = tf.matmul(prod, A)
    final_shape = tf.shape(x)[:-1]
    final_shape = tf.concat([final_shape, [tf.shape(A)[-1]]], 0)
    return tf.reshape(prod, final_shape)


class MemoryNetwork(object):

    def __init__(self,
                 num_actions,
                 utterance_len,
                 embedding_size,
                 mem_size=10,
                 hops=3,
                 var_init=tf.random_normal_initializer(stddev=0.1),
                 model_name="MemoryNetwork",
                 optimizer=tf.train.AdamOptimizer(learning_rate=1e-4, epsilon=1e-8),
                 clip_norm=15.,
                 keep_prob=1.):
        self.h = [[0] * utterance_len]  # used during online test
        self.hops = hops
        self.mem_size = mem_size
        self.h_len = utterance_len
        # placeholders
        # [batch, mem_size, utter_len]
        self.history = tf.placeholder(tf.float32, [None, None, utterance_len], name="history")
        self.queries = tf.placeholder(tf.float32, [None, utterance_len], name="queries")  # [batch, query_len]
        self.labels = tf.placeholder(tf.float32, [None, num_actions], name="labels")  # [batch, num_actions]
        self.keep_prob = tf.placeholder(tf.float32, [], name='keep_probability')
        self.train_keep_prob = keep_prob

        # model parameters
        with tf.variable_scope(model_name):
            self.A = [tf.Variable(initial_value=var_init([utterance_len, embedding_size]), name="A" + str(i))
                      for i in range(hops+1)]
            # self.C = tf.Variable(initial_value=var_init([h_utterance_len, embedding_size]), name="C")
            self.W = tf.Variable(initial_value=var_init([embedding_size, num_actions]), name="W")
            self.H = tf.Variable(initial_value=var_init([embedding_size, embedding_size]), name="H")
            self.embedding_size = embedding_size

            # define graph
            u = tf.matmul(self.queries, self.A[0])  # [batch, embedding_size]
            for i in range(hops):
                """we need a matmul on each [mem_size, utter_len] element of history with A. scan takes each element
                (across 0th dim) of history and applies the lambda function (matmul) to it. Argument x is the element
                currently processed of history and a is the result of the previous call (the first time, a equals
                initializer, or history[0] if no initializer present). Since the final value is a concatenation of
                each call, then each must return a value of same shape. Hence, not providing the initializer causes
                an exception since result[0] = history[0] which has different shape than matmul(history[i], A).
                For result[0] to be lambda(_, history[0]), there must be an initializer, even if not used, so giving a
                z ero matrix with the right dimensions. These are two other ways to achieve the same:
                m = batch_matmul(self.history, self.A)  # [batch, mem_size, embedding_size]  # more efficient but ugly
                m = tf.scan(lambda a, x: tf.matmul(x, self.A), self.history,
                            initializer=tf.matmul(self.history[0], self.A))  # crashes with empty batches
                m = tf.scan(lambda a, x: tf.matmul(x, self.A), self.history,  # won't crash with empty batches
                            initializer=tf.matmul(tf.zeros(shape=tf.gather(tf.shape(self.history), [1, 2])), self.A))
                Finally, decided to do it the cleanest way possible: with matmul, so long as dimensions are compatible:
                for A*B, A[-1] = B[-2] (i.e. the inner-most dimensions of A and B must be valid for matrix 
                multiplication). The rest of the dimensions, must be identical (since in the end, we are just 
                multiplying a bunch of matrices, each dimension besides the inner most is just one more bag of such 
                matrices into the bunch) A having rank [20, 30, 10, 15] * B having rank [20, 30, 15, 50] produces A*B 
                having rank [20, 30, 10, 50]. Hence, only the last dimension of A is lost, as this operation can be 
                understood as embedding that last dimension to the space of the last dimension of B (size 50).
                Since A is missing a dimension equal to mem_size, we just add it with expand_dims and use tile to repeat
                A across mem_size rows (tile requires number of times each dimension gets repeated, hence the 1's) 
                """
                # [batch, mem_size, embedding_size]
                m = tf.matmul(self.history, tf.tile(tf.expand_dims(self.A[i], 0), [tf.shape(self.history)[0], 1, 1]))
                """This is like doing softmax in np like this:
                    soft = np.exp(p)  # where p is a matrix
                    sum = np.sum(soft, axis=1)  # sum across columns, you get a vector
                    soft /= sum[:, None]  # divide matrix by vector. The None dim is shorthand to add expanded dim in np
                    so that the / broadcasts automatically (just like *)
                """
                # the extra dim added to u causes a broadcast at m * u. reduce_sum just cause no easy dot product in tf
                p = tf.nn.softmax(tf.reduce_sum(m * tf.expand_dims(u, 1), -1))  # [batch, mem]
                c = tf.matmul(self.history, tf.tile(tf.expand_dims(self.A[i+1], 0), [tf.shape(self.history)[0], 1, 1]))
                # c = tf.matmul(self.history, tf.tile(tf.expand_dims(self.C, 0), [tf.shape(self.history)[0], 1, 1]))
                # multiply each of the [batch, mem] c embeddings by scalar p to get weighted average output embedding
                o = tf.reduce_sum(tf.expand_dims(p, -1) * c, axis=1)  # [batch, embedding_size]
                u = o + tf.matmul(u, self.H)
                tf.summary.tensor_summary('my_tensor_summary', p)
            self.logits = tf.nn.dropout(tf.matmul((o + u), self.W), self.keep_prob)  # [batch, actions]
            self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=self.labels, logits=self.logits))
            self.output_p = tf.nn.softmax(self.logits)
            self.pred_action = tf.arg_max(self.output_p, dimension=0)
            self.accuracy = tf.reduce_mean(tf.cast(
                tf.equal(tf.argmax(self.logits, axis=1), tf.argmax(self.labels, axis=1)),
                tf.float32))

            grads, vars = zip(*optimizer.compute_gradients(self.loss))
            grads_clipped, _ = tf.clip_by_global_norm(grads, clip_norm=clip_norm)
            self.train_op = optimizer.apply_gradients(zip(grads_clipped, vars))

            self.sess = tf.Session()
            self.summary = tf.summary.merge_all()
            self.summary_writer = tf.summary.FileWriter('misc_experiments/logs/', self.sess.graph)
            self.sess.run(tf.global_variables_initializer())
            self.step = 0
            self.p = p

    def prediction(self, history, query):
        summary_str, prediction = self.sess.run([self.summary, self.output_p], feed_dict={self.history: [history],
                                                                                          self.queries: [query],
                                                                                          self.keep_prob: 1})
        self.summary_writer.add_summary(summary_str, self.step)
        self.step += 1
        self.summary_writer.flush()
        return prediction

    def train_step(self, history_batch, query_batch, label_batch):
        pred, loss, _ = self.sess.run([self.pred_action, self.loss, self.train_op],
                                      feed_dict={self.history: history_batch,
                                                 self.queries: query_batch,
                                                 self.labels: label_batch,
                                                 self.keep_prob: self.train_keep_prob})
        return pred, loss

    def predict_turn(self, x):
        """predicts given one turn, keeping track of history
        :param x: featurized turn"""
        prediction = self.sess.run(self.output_p, feed_dict={self.history: [self.h if len(self.h) > 0 else
                                                                            [[0] * self.h_len]],
                                                             self.queries: [x],
                                                             self.keep_prob: 1})
        self.h.append(x)
        # if len(self.h) > self.mem_size:
        #     self.h = self.h[::-1][:self.mem_size][::-1]
        return prediction.squeeze()

    def reset_conversation_state(self):
        self.h = []

    def persist(self, path):
        config = {'hops': self.hops, 'num_actions': int(self.labels.shape[-1]), 'mem_size': self.mem_size,
                  'train_dropout': self.train_keep_prob, 'input_dim': int(self.queries.shape[-1]),
                  'embedding_size': self.embedding_size}
        if not exists(path):
            mkdir(path)
        with open(join(path, 'config.json'), 'w') as fh:
            json.dump(config, indent=2, fp=fh)
        saver = tf.train.Saver()
        saver.save(self.sess, path, global_step=0)
        logging.info('successfully persisted the model at {}'.format(path))

    @staticmethod
    def load(path):
        with open(join(path, 'config.json')) as fh:
            config = json.load(fh)
        model = MemoryNetwork(num_actions=config['num_actions'], utterance_len=config['input_dim'],
                              embedding_size=config['embedding_size'], mem_size=config['mem_size'], hops=config['hops'],
                              keep_prob=config['train_dropout'])
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(path)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(model.sess, ckpt.model_checkpoint_path)
            logging.info('successfully restored Memory Network model from {}'.format(path))
        else:
            logging.error('persisted model not found')
        return model


class MemNetPolicy(Policy):
    """
    Rasa wrapper around the memory network
    """
    def __init__(self, history, query, label, batch_indexes, encoder, model=None, embedding_size=10, hops=3,
                 var_init=tf.random_normal_initializer(stddev=0.1), model_name='MemoryNetwork'):
        """
        Sets or creates a model and sets the training data
        :param history: Iterable[List[List[float]]]. Training data history component. A list where each element refers
        to a data point. Each element is a list of memories, each one a list of numbers comprising the featurization of
        a memory. All such featurizations must have identical length and there can't be empty lists (an empty history
        should be comprised of at least 1 fully 0-padded memory). History can't be empty.
        :param query: Iterable[List[float]]. Training data query component. A list where each element refers to a data
        point. Each element is a list of numbers comprising the featurization of a memory. All such featurizations must
        have identical length. query can't be empty and should have same length as history.
        :param label: Iterable[List[float]]. Training data label component. A list where each element refers to a data
        point. Each element is a list of numbers comprising the 1-hot encoding of a label. All such encodings must have
        length equal to total number of actions. label can't be empty and should have same length as history and query.
        :param batch_indexes: Iterable[Tuple[int, int]]. Indexes of start and end elements of each batch. Training data
        will be split in batches according to these indexes, so the ith batch goes from data[batch_indexes[i][0]] to
        data[batch_indexes[i][1]] (non inclusive)
        :param encoder: MemNetDataAdapter object. It's encode function will be called during inference to featurize
        user input
        :param model: a MemoryNetwork object, compatible with the dimensions of the training data (e.g. length of
        memories, number of actions). If not provided, one will be instantiated, inferring the length of each memory,
        length of queries and number of actions from the provided training data.
        :param embedding_size: int, size of memory and query embeddings for the Memory Network
        :param hops: int, number of hops (i.e. memory checks) of the Memory Network
        :param var_init: tf.keras.initializers.Initializer, model variable initializer
        :param model_name: str, name of the model. It identifies the variable scope
        """
        super(MemNetPolicy, self).__init__(None, None)  # rasa crap
        assert len(history) > 0, 'Memory network received empty training data'
        assert len(history) == len(query) and len(query) == len(label), 'Different sizes of history ({}), queries ' \
                                                                        '({}) and labels ({}) provided to the ' \
                                                                        'MemoryNetwork'.format(len(history),
                                                                                               len(query),
                                                                                               len(label))
        self.history = history
        self.queries = query
        self.labels = label
        self.batch_indexes = list(batch_indexes)
        self.current_epoch = 0
        self.model_name = model_name
        self.sess = tf.Session()
        self.mem_size = max(len(h) for h in self.history)
        self.encoder = encoder
        num_actions = len(label[0])  # trn data can't be empty
        utterance_len = len(history[0][0])  # at least 1 padded memory is in history, always
        if model:
            assert isinstance(model, MemoryNetwork), 'expected a MemoryNetwork as model. Got {}'.format(type(model))
            MemNetPolicy._check_data_model_compatibility(model, num_actions, utterance_len)
            self.model = model
        else:
            self.model = MemoryNetwork(num_actions=num_actions, utterance_len=utterance_len,
                                       embedding_size=embedding_size, mem_size=self.mem_size, hops=hops,
                                       var_init=var_init, model_name=model_name)

    @staticmethod
    def _check_data_model_compatibility(model, num_actions, h_utterance_len):
        model_num_actions = int(model.labels.shape[-1])
        model_utterance_len = int(model.history.shape[-1])
        model_query_len = int(model.queries.shape[-1])
        assert model_num_actions == num_actions, 'number of actions defined in training data ({}) differs from ' \
                                                 'the one defined in the model ({})'.format(num_actions,
                                                                                            model_num_actions)
        assert model_utterance_len == h_utterance_len, 'length of history utterances defined in training data ' \
                                                         '({}) differs from the one defined in the model ({})'. \
            format(h_utterance_len, model_utterance_len)
        assert model_query_len == model_utterance_len, 'length of queries defined in training data ({}) differs from ' \
                                                       'the one defined in the model ({})'.format(model_utterance_len,
                                                                                                  model_query_len)

    def reset(self):
        self.encoder._reset()

    def predict_action_probabilities(self, tracker, domain):
        if isinstance(tracker.events[-1], ActionExecuted):
            # dead simple patch to force a listen after every action, cause fuck rasa
            p = [0.0] * len(domain.action_names)
            p[domain.action_map[ACTION_LISTEN_NAME][0]] = 1
            return p
        query, history = self.encoder.encode(tracker, self.mem_size)
        predictions = self.sess.run(self.model.output_p, feed_dict={self.model.history: [history],
                                                                    self.model.queries: [query],
                                                                    self.model.keep_prob: 1})
        predictions = [0.0, 0.0] + list(predictions[0])  # leading 0s due to action_listen and action_restart
        # hardcoded rules
        predictions = self.apply_domain_rules(predictions, tracker, domain)
        return predictions

    def apply_domain_rules(self, p, tracker, domain):
        """
        Called after the Memory Network made its prediction. Subclasses can override this method to apply domain
        specific rules to this vector before, potentially redifining the predicted action
        :param p: probability vector over actions
        :param tracker: rasa tracker object
        :param domain: rasa domain object
        :return: probability vector after applying the domain specific rules
        """
        return p

    def train(self, training_data, domain, **kwargs):
        """
        Creates the model (only if it is not created yet) and trains it.
        :param training_data: not used, kept only for Rasa compatibility
        :param domain: rasa Domain object
        :param kwargs: Following keys are optional, along with their default values:
        mn_training_data: training data. If provided, it overrides the current training data of the policy.
        Dictionary with the keys 'history', 'query' and 'label' (for the respective components of the training data) and
        'batch_indexes' (see __init__ documentation). Their dimensions (history utterance length, query length and
        number of actions) must match those defined in the model.
        mn_dev_data: development data. If provided, development data accuracy and loss will be printed along with
        training statistics. It must follow the same conditions applicable for mn_training_data
        mn_keep_prob: keep probability for dropout, defaults to 1
        mn_epochs: training epochs of the memory network, defaults to 50
        mn_clip_norm: maximum allowed norm of the gradients during training, defaults to 25
        mn_print_cycle: number of batches to process before each print of training statistics, defaults to 100
        """
        keep_prob = kwargs['mn_keep_prob'] if 'mn_keep_prob' in kwargs else 1
        epochs = kwargs['mn_epochs'] if 'mn_epochs' in kwargs else 50
        clip_norm = kwargs['mn_clip_norm'] if 'mn_clip_norm' in kwargs else 25
        print_cycle = kwargs['mn_print_cycle'] if 'mn_print_cycle' in kwargs else 100
        if 'mn_training_data' in kwargs:
            assert 'history' in kwargs['mn_training_data'], 'no history in the mn_training_data dictionary'
            assert 'query' in kwargs['mn_training_data'], 'no queries in the mn_training_data dictionary'
            assert 'label' in kwargs['mn_training_data'], 'no labels in the mn_training_data dictionary'
            assert 'batch_indexes' in kwargs['mn_training_data'], 'no batch indexes in the mn_training_data dictionary'
            num_actions = len(kwargs['mn_training_data']['label'][0])
            h_utterance_len = len(kwargs['mn_training_data']['history'][0][0])
            query_len = len(kwargs['mn_training_data']['query'][0])
            MemNetPolicy._check_data_model_compatibility(self.model, num_actions, h_utterance_len, query_len)
            self.history = kwargs['mn_training_data']['history']
            self.queries = kwargs['mn_training_data']['query']
            self.labels = kwargs['mn_training_data']['label']
            self.batch_indexes = list(kwargs['mn_training_data']['batch_indexes'])
        if 'mn_dev_data' in kwargs:
            assert 'history' in kwargs['mn_dev_data'], 'no history in the mn_dev_data dictionary'
            assert 'query' in kwargs['mn_dev_data'], 'no queries in the mn_dev_data dictionary'
            assert 'label' in kwargs['mn_dev_data'], 'no labels in the mn_dev_data dictionary'
            if 'batch_indexes' not in kwargs['mn_dev_data']:
                logger.info('no batch indexes in dev data. Using a single batch')
                dev_batch_indexes = [(0, len(kwargs['mn_dev_data']['query']))]
            else:
                dev_batch_indexes = list(kwargs['mn_dev_data']['batch_indexes'])
            num_actions_dev = len(kwargs['mn_dev_data']['label'][0])
            h_utterance_len_dev = len(kwargs['mn_dev_data']['history'][0][0])
            MemNetPolicy._check_data_model_compatibility(self.model, num_actions_dev, h_utterance_len_dev)
        # all set. Aan de slag
        logging.info(
            'starting training\nConfig:\nhops: {}\nactions: {}\nhistory utterance length: {}\nquery length: {}\n'
            'embedding size: {}\nbatch size: {}\nmax memory: {}\nkeep prob: {}\nepochs: {}\n'
            'gradient clip norm: {}\n'.format(
                self.model.hops, int(self.model.labels.shape[-1]), int(self.model.history.shape[-1]),
                int(self.model.queries.shape[-1]), self.model.embedding_size, len(self.batch_indexes),
                max(len(h) for h in self.history), keep_prob, epochs, clip_norm))
        optimizer = tf.train.AdamOptimizer(learning_rate=1e-4, epsilon=1e-8)
        loss_op = self.model.loss
        grads, vars = zip(*optimizer.compute_gradients(loss_op))
        grads_clipped, _ = tf.clip_by_global_norm(grads, clip_norm=clip_norm)
        train_op = optimizer.apply_gradients(zip(grads_clipped, vars))
        self.sess.run(tf.global_variables_initializer())
        for epoch in range(epochs):
            trn_accuracies = []
            for i, (b_start, b_end) in enumerate(self.batch_indexes):
                feed_dict = {self.model.history: self.history[b_start:b_end],
                             self.model.queries: self.queries[b_start:b_end],
                             self.model.labels: self.labels[b_start:b_end],
                             self.model.keep_prob: keep_prob
                             }
                loss, _ = self.sess.run([loss_op, train_op], feed_dict=feed_dict)
                feed_dict[self.model.keep_prob] = 1
                accuracy = self.sess.run(self.model.accuracy, feed_dict=feed_dict)
                if i % print_cycle == 0:
                    logging.info('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
                trn_accuracies.append(accuracy)
            if 'mn_dev_data' in kwargs:
                dev_accuracies, dev_losses = [], []
                for i, (b_start, b_end) in enumerate(dev_batch_indexes):
                    dev_accuracy, dev_loss = self.sess.run(
                        [self.model.accuracy, loss_op],
                        feed_dict={
                            self.model.history: kwargs['mn_dev_data']['history'][b_start:b_end],
                            self.model.queries: kwargs['mn_dev_data']['query'][b_start:b_end],
                            self.model.labels: kwargs['mn_dev_data']['label'][b_start:b_end],
                            self.model.keep_prob: 1})
                    dev_accuracies.append(dev_accuracy)
                    dev_losses.append(dev_loss)
                logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(
                    epoch,
                    mean(dev_losses),
                    mean(dev_accuracies),
                    mean(trn_accuracies)
                ))
            else:
                logging.info('epoch: {}\ttrain accuracy: {}'.format(epoch, mean(trn_accuracies)))
            self.current_epoch += epochs + 1

    def persist(self, path):
        raise NotImplementedError

    @classmethod
    def load(cls, path, featurizer, max_history):
        raise NotImplementedError


class MemNetT5Policy(MemNetPolicy):
    def persist(self, path):
        # persist metadata
        if not exists(path):
            mkdir(path)
        with open(join(path, 'MemoryNetwork_metadata.pickle'), 'wb') as metadata_fh:
            pickle.dump((self.history, self.queries, self.labels, self.batch_indexes, self.model.hops,
                         self.model.embedding_size, self.current_epoch, self.model_name), metadata_fh)
        # persist model variables
        saver = tf.train.Saver()
        saver.save(self.sess, join(path, "MemoryNetwork"))

    @classmethod
    def load(cls, path, featurizer, max_history):
        # restore metadata
        with open(join(path, 'MemoryNetwork_metadata.pickle'), 'rb') as metadata_fh:
            history, queries, labels, batch_indexes, hops, embedding_size, current_epoch, model_name = \
                pickle.load(metadata_fh)
        num_actions = len(labels[0])
        utterance_len = len(history[0][0])
        mem_size = max(len(h) for h in history)

        # restore model
        tf.reset_default_graph()
        model = MemoryNetwork(num_actions, utterance_len, embedding_size, mem_size, hops=hops)
        mem_net_policy = cls(history, queries, labels, batch_indexes, model=model,
                             embedding_size=embedding_size, hops=hops, encoder=MemNetT5DataAdapter())
        mem_net_policy.current_epoch = current_epoch

        saver = tf.train.Saver()
        saver.restore(mem_net_policy.sess, join(path, "MemoryNetwork"))
        logger.info('successfully restored model')
        return mem_net_policy


class MemNetT6Policy(MemNetPolicy):

    def __init__(self, *args, **kwargs):
        self.db = BabiDB(BABI_T6_KB_FILE)
        super(MemNetT6Policy, self).__init__(*args, **kwargs)

    def persist(self, path):
        # persist metadata
        if not exists(path):
            mkdir(path)
        with open(join(path, 'MemoryNetwork_metadata.pickle'), 'wb') as metadata_fh:
            pickle.dump((self.history, self.queries, self.labels, self.batch_indexes, self.model.hops,
                         self.model.embedding_size, self.current_epoch, self.model_name, self.encoder.path,
                         self.encoder.kb_filename, self.encoder.vocab_filename, self.encoder.w2v_model_filename),
                        metadata_fh)
        # persist model variables
        saver = tf.train.Saver()
        saver.save(self.sess, join(path, "MemoryNetwork"))

    @classmethod
    def load(cls, path, featurizer, max_history):
        # restore metadata
        with open(join(path, 'MemoryNetwork_metadata.pickle'), 'rb') as metadata_fh:
            history, queries, labels, batch_indexes, hops, embedding_size, current_epoch, model_name, nlu_path, \
            kb_filename, vocab_filename, w2v_model_filename = pickle.load(metadata_fh)
        num_actions = len(labels[0])
        utterance_len = len(history[0][0])
        mem_size = max(len(h) for h in history)
        # restore model
        tf.reset_default_graph()
        model = MemoryNetwork(num_actions, utterance_len, embedding_size, mem_size, hops=hops)
        mem_net_policy = cls(history, queries, labels, batch_indexes, model=model,
                             embedding_size=embedding_size, hops=hops, encoder=MemNetT6DataAdapter(nlu_path,
                                                                                                   kb_filename,
                                                                                                   vocab_filename,
                                                                                                   w2v_model_filename))
        mem_net_policy.current_epoch = current_epoch

        saver = tf.train.Saver()
        saver.restore(mem_net_policy.sess, join(path, "MemoryNetwork"))
        logger.info('successfully restored model')
        return mem_net_policy

    def apply_domain_rules(self, p, tracker, domain):
        """
        Called after the Memory Network made its prediction. Subclasses can override this method to apply domain
        specific rules to this vector before, potentially redifining the predicted action
        :param p: probability vector over actions
        :param tracker: rasa tracker object
        :param domain: rasa domain object
        :return: probability vector after applying the domain specific rules
        """
        # action = domain.action_for_index(argmax(p)).name()
        # entities = {e: v for e, v in tracker.current_slot_values().items() if v}
        # if action == 'api_call':
        #     num_results = self.db.num_results(**entities)
        #     if num_results == 0:  # don't issue api_call
        #         p[domain.index_for_action(action)] = 0
        #         p = softmax(p)
        return p


def get_args():
    parser = argparse.ArgumentParser(
        description='train or test a MemoryNetwork for bAbI tasks 5 or 6')
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


def format_babi_data(filename, featurizer):
    """
    produces bAbI data in a format suitable for the memory network. Each conversation provides as many training examples
    as turns. Turn i produces a training example that contains the conversation history up to turn i-1, the user
    utterance from turn i and the bot action at turn i
    :param filename: bAbI conversation filename
    :param featurizer: featurizer object
    :return: List of training examples with labels. Each element is a Dictionary['history': h, 'query': q, 'label': l,
    'entities': e]
    h: List, h[i] is the featurized data point at turn i in the conversation
    q: vector of features representing the current turn (in the same format as the elements of h)
    l: 1 hot vector indicating the bot action at the current turn
    e: Dictionary with the value of each entity at that point in the conversation (None, for those with no value set)
    """
    data = []

    def prev_bot_utter():
        return '' if i == 0 else story[i-1]['bot']
    for si, story in enumerate(BabiReader.babi_dialogue_iterator(filename)):
        logger.info('featurizing story {}'.format(si))
        h = []
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text=prev_bot_utter(), turn=i)
            data.append({'history': copy(h), 'query': x, 'label': featurizer.bot_features(turn['bot']),
                         'entities': copy(featurizer.slot_values)})
            h.append(x)
        featurizer.reset()
    return data


def build_batches(filename, featurizer, batch_size=32, max_memory_size=8):
    """
    Produces batch indexes of points with similar length of history and adds padding so that the history component of
    all points in a batch have the same length
    :param filename: bAbI conversation filename
    :param featurizer: featurizer object
    :param batch_size: number of elements in a batch, unless there are not enough elements, then a batch will have the
    remaining points, with len < batch_size
    :param max_memory_size: max number of previous utterances (bot and user alike) to keep in history for a single
    data point
    :return: history, query, label, entities, batch_indexes. Each one is a list. The ith element of all lists is refers
    to one data point. The lists are sorted by decreasing length of history and adding padding so that all histories in
    the same batch have equal length. batch_indexes is an iterable of Tuple[start, end], where end is not part of the
    current batch but of the next only (i.e. end_i = start_i+1 for all i except the last). Do note the end index of the
    last batch is not checked against the number of elements in the data, therefore this number can be higher.
    This should not be a problem if data is split using the data[start:end] slicing format
    """
    data = format_babi_data(filename=filename, featurizer=featurizer)
    max_memory_size = min(max_memory_size, max(len(x['history']) for x in data))  # no point in max_mem > longest h
    batch_size = min(batch_size, len(data))
    data.sort(key=lambda x: len(x['history']), reverse=True)
    history, query, label, entities = [], [], [], []
    batch_memory_size = max_memory_size  # redundant, just to comply with PEP8 (batch_mem could be reference before bla)
    for i, x in enumerate(data):
        h, q, l, e = x.values()
        if i % batch_size == 0:  # new batch. history length of this first point in the batch determines memory_size
            batch_memory_size = max(1, min(max_memory_size, len(h)))  # memory in [1, max_memory_size]
        h = h[::-1][:batch_memory_size][::-1]  # take only last memory_size sentences (flip, cut at mem size, flip back)
        pad_size = max(0, batch_memory_size - len(h))  # pad h
        for _ in range(pad_size):  # empty histories will thus consist of 1 0 padded memory
            h.append([0] * featurizer.feature_len())
        history.append(h)
        query.append(q)
        label.append(l)
        entities.append(e)
    batch_indexes = list(zip(range(0, len(data) - batch_size, batch_size), range(batch_size, len(data), batch_size)))
    return history, query, label, entities, batch_indexes


def train_t6():
    logging.info(
        'starting training\nConfig:\nhops: {}\nactions: {}\nhistory utterance length: {}\n'
        'embedding size: {}\nbatch size: {}\nmemory size: {}\nepochs: {}\ngradient clip norm: {}\n'
        'keep prob: {}\n'.format(hops, num_actions, h_len, embedding_size, batch, mem_size, epochs,
                                 clip_norm,
                                 keep_prob))
    saved_batches = 'fabot/custom/memnet/saved_data/t6_trn_memnet_{bot_prev}_{ent}_{feats}_data.pickle'.format(
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline', ent=args.entities, feats=args.features)
    if isfile(saved_batches):
        with open(saved_batches, 'rb') as batches_fh:
            trn_history, trn_query, trn_label, trn_entities, batch_indexes = pickle.load(batches_fh)
    else:
        print('train batches data not found, now recreating it')
        trn_history, trn_query, trn_label, trn_entities, batch_indexes = build_batches(filename=BABI_T6_TRN_FILE,
                                                                                       featurizer=featurizer,
                                                                                       batch_size=batch,
                                                                                       max_memory_size=mem_size)
        print('saving data')
        with open(saved_batches, 'wb') as batches_fh:
            pickle.dump((trn_history, trn_query, trn_label, trn_entities, batch_indexes), batches_fh)
        print('saved')
    saved_batches = 'fabot/custom/memnet/saved_data/t6_dev_memnet_{bot_prev}_{ent}_{feats}_data.pickle'.format(
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline', ent=args.entities, feats=args.features)
    if isfile(saved_batches):
        with open(saved_batches, 'rb') as batches_fh:
            dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes = pickle.load(batches_fh)
    else:
        print('dev batches data not found, now recreating it')
        dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes = build_batches(
            filename=BABI_T6_DEV_FILE, featurizer=featurizer, batch_size=100, max_memory_size=mem_size)
        print('saving data')
        with open(saved_batches, 'wb') as batches_fh:
            pickle.dump((dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes), batches_fh)
        print('saved')

    model = MemoryNetwork(num_actions=num_actions, utterance_len=h_len,
                          embedding_size=embedding_size, mem_size=mem_size, hops=hops, keep_prob=keep_prob,
                          clip_norm=clip_norm)
    highest_dev_acc = 0
    chances2improve = 5
    stop = False
    for epoch in range(epochs):
        if stop:
            break
        batch_indexes = list(batch_indexes)
        trn_accuracies = []
        for i, (b_start, b_end) in enumerate(batch_indexes):
            pred, loss = model.train_step(history_batch=trn_history[b_start:b_end],
                                          query_batch=trn_query[b_start:b_end],
                                          label_batch=trn_label[b_start:b_end])
            accuracy = model.sess.run(model.accuracy, feed_dict={model.history: trn_history[b_start:b_end],
                                                                 model.queries: trn_query[b_start:b_end],
                                                                 model.labels: trn_label[b_start:b_end],
                                                                 model.keep_prob: 1})
            if i % print_cycle == 0:
                logging.info('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
            trn_accuracies.append(accuracy)
        dev_accuracies, dev_losses = [], []
        for i, (b_start, b_end) in enumerate(dev_batch_indexes):
            _, dev_loss = model.train_step(history_batch=dev_history[b_start:b_end],
                                           query_batch=dev_query[b_start:b_end],
                                           label_batch=dev_label[b_start:b_end])
            dev_accuracy = model.sess.run(model.accuracy, feed_dict={model.history: dev_history[b_start:b_end],
                                                                     model.queries: dev_query[b_start:b_end],
                                                                     model.labels: dev_label[b_start:b_end],
                                                                     model.keep_prob: 1})
            dev_accuracies.append(dev_accuracy)
            dev_losses.append(dev_loss)
        dev_acc = mean(dev_accuracies)
        if dev_acc >= highest_dev_acc:
            highest_dev_acc = dev_acc
            chances2improve = 5
            model.persist(persisted_path)
        else:
            chances2improve -= 1
            if chances2improve == 0:
                logger.info('no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                stop = True
        logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(
            epoch,
            mean(dev_losses),
            dev_acc,
            mean(trn_accuracies)
        ))


def train(task='5'):
    if task == '5':
        trn_file = BABI_T5_TRN_FILE
        dev_file = BABI_T5_DEV_FILE
    else:
        trn_file = BABI_T6_TRN_FILE
        dev_file = BABI_T6_DEV_FILE
    logging.info(
        'starting training\nConfig:\nhops: {}\nactions: {}\nhistory utterance length: {}\n'
        'embedding size: {}\nbatch size: {}\nmemory size: {}\nepochs: {}\ngradient clip norm: {}\n'
        'keep prob: {}\n'.format(hops, num_actions, h_len, embedding_size, batch, mem_size, epochs,
                                 clip_norm,
                                 keep_prob))
    saved_batches = 'fabot/custom/memnet/saved_data/t{task}_trn_memnet_{bot_prev}_{ent}_{feats}_data.pickle'.format(
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline', task=task, ent=args.entities,
        feats=args.features)
    if isfile(saved_batches):
        with open(saved_batches, 'rb') as batches_fh:
            trn_history, trn_query, trn_label, trn_entities, batch_indexes = pickle.load(batches_fh)
    else:
        print('train batches data not found, now recreating it')
        trn_history, trn_query, trn_label, trn_entities, batch_indexes = build_batches(filename=trn_file,
                                                                                       featurizer=featurizer,
                                                                                       batch_size=batch,
                                                                                       max_memory_size=mem_size)
        print('saving data')
        with open(saved_batches, 'wb') as batches_fh:
            pickle.dump((trn_history, trn_query, trn_label, trn_entities, batch_indexes), batches_fh)
        print('saved')
    saved_batches = 'fabot/custom/memnet/saved_data/t{task}_dev_memnet_{bot_prev}_{ent}_{feats}_data.pickle'.format(
        bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline', task=task, ent=args.entities,
        feats=args.features)
    if isfile(saved_batches):
        with open(saved_batches, 'rb') as batches_fh:
            dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes = pickle.load(batches_fh)
    else:
        print('dev batches data not found, now recreating it')
        dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes = build_batches(
            filename=dev_file, featurizer=featurizer, batch_size=100, max_memory_size=mem_size)
        print('saving data')
        with open(saved_batches, 'wb') as batches_fh:
            pickle.dump((dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes), batches_fh)
        print('saved')

    model = MemoryNetwork(num_actions=num_actions, utterance_len=h_len,
                          embedding_size=embedding_size, mem_size=mem_size, hops=hops, keep_prob=keep_prob,
                          clip_norm=clip_norm)
    highest_dev_acc = 0
    chances2improve = 5
    stop = False
    for epoch in range(epochs):
        if stop:
            break
        batch_indexes = list(batch_indexes)
        trn_accuracies = []
        for i, (b_start, b_end) in enumerate(batch_indexes):
            pred, loss = model.train_step(history_batch=trn_history[b_start:b_end],
                                          query_batch=trn_query[b_start:b_end],
                                          label_batch=trn_label[b_start:b_end])
            accuracy = model.sess.run(model.accuracy, feed_dict={model.history: trn_history[b_start:b_end],
                                                                 model.queries: trn_query[b_start:b_end],
                                                                 model.labels: trn_label[b_start:b_end],
                                                                 model.keep_prob: 1})
            if i % print_cycle == 0:
                logging.info('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
            trn_accuracies.append(accuracy)
        dev_accuracies, dev_losses = [], []
        for i, (b_start, b_end) in enumerate(dev_batch_indexes):
            _, dev_loss = model.train_step(history_batch=dev_history[b_start:b_end],
                                           query_batch=dev_query[b_start:b_end],
                                           label_batch=dev_label[b_start:b_end])
            dev_accuracy = model.sess.run(model.accuracy, feed_dict={model.history: dev_history[b_start:b_end],
                                                                     model.queries: dev_query[b_start:b_end],
                                                                     model.labels: dev_label[b_start:b_end],
                                                                     model.keep_prob: 1})
            dev_accuracies.append(dev_accuracy)
            dev_losses.append(dev_loss)
        dev_acc = mean(dev_accuracies)
        if dev_acc > highest_dev_acc:
            highest_dev_acc = dev_acc
            chances2improve = 5
            model.persist(persisted_path)
        else:
            chances2improve -= 1
            if chances2improve == 0:
                logger.info('no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                stop = True
        logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(
            epoch,
            mean(dev_losses),
            dev_acc,
            mean(trn_accuracies)
        ))


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


def test(task='6'):
    model = MemoryNetwork.load(persisted_path)
    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    if task == '6':
        tst_file = BABI_T6_TST_FILE
        total_turns = 11237
        total_dialogs = 1117
    else:  # i.e. 5
        tst_file = BABI_T5_TST_FILE if not args.oov else BABI_T5_TST_OOV_FILE
        total_turns = 18398 if not args.oov else 18368
        total_dialogs = 1000
    for story in BabiReader.babi_dialogue_iterator(tst_file):
        featurizer.reset()
        story_results = []
        dialog_act_matches, dialog_literal_matches = 0, 0
        h = []
        prev_pred = ''  # initial value for the previous prediction
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text=bot_prev_utter(story, i, prev_pred), turn=i)
            prediction = model.prediction(history=h if len(h) > 0 else [[0] * featurizer.feature_len()], query=x)

            turn_results = dict()
            turn_results['human'] = turn['human']
            turn_results['target'] = turn['bot']
            actual_da = featurizer.get_bot_act(turn['bot'])
            predicted_da = featurizer.id2act(argmax(prediction))
            prev_pred = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
            turn_results['actual'] = prev_pred
            turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                     string=turn_results['target']) is not None
            turn_results['act_match'] = actual_da == predicted_da
            story_results.append(turn_results)

            h.append(x)
            # if len(h) > mem_size:
            #     h = h[::-1][:mem_size][::-1]

            dialog_act_matches += int(turn_results['act_match'])
            dialog_literal_matches += int(turn_results['literal_match'])
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
        results.append(story_results)
    with open('fabot/custom/memnet/results/tst_t{task}_memnet_{bot_prev}_{ent}_{feats}_{oov}results.json'.format(
            task=task, ent=args.entities, feats=args.features, bot_prev=args.bot_prev, oov='oov_' if args.oov else ''),
            'w') as fh:
        json.dump(results, fh, indent=2)
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_act_matches, total_turns, total_act_matches / total_turns, perfect_act_dialogs, total_dialogs,
                                        perfect_act_dialogs / total_dialogs))
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_literal_matches, total_turns, total_literal_matches / total_turns, perfect_literal_dialogs, total_dialogs,
                                            perfect_literal_dialogs / total_dialogs))


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
        persisted_path = PERSISTED_MEMNET_PATH.format(
            bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline', task=args.task, ent=args.entities,
            feats=args.features)
        featurizer = T6Featurizer(**features)
        num_actions = T6Featurizer.num_actions()
        h_len = featurizer.feature_len()

        print_cycle = 100
        hops = 2
        embedding_size = 100
        batch = 32
        mem_size = 9
        epochs = 35
        clip_norm = 1.
        keep_prob = 0.8
        if args.job == 'train':
            train(task=args.task)
        if args.job == 'test':
            test(args.task)
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
        persisted_path = PERSISTED_MEMNET_PATH.format(
            bot_prev=args.bot_prev if args.bot_prev != 'online' else 'offline', task=args.task, ent=args.entities,
            feats=args.features)
        num_actions = T5Featurizer.num_actions()
        h_len = featurizer.feature_len()

        print_cycle = 100
        hops = 2
        embedding_size = 100
        batch = 32
        mem_size = 9
        epochs = 35
        clip_norm = 1.
        keep_prob = 0.8
        if args.job == 'train':
            train(task=args.task)
        if args.job == 'test':
            test(args.task)

