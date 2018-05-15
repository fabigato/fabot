import tensorflow as tf
from fabot.custom.memnet.data_utils import MemNetT5DataAdapter, MemNetT6DataAdapter
from data.database import BabiDB
from globals import BABI_T6_KB_FILE
from rasa_core.policies import Policy
from rasa_core.events import ActionExecuted, UserUttered
from rasa_core.actions.action import ACTION_LISTEN_NAME, ACTION_RESTART_NAME
from numpy import mean, argmax, exp
from os.path import join
import logging
import pickle

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


# TODO another improvement: maybe it is good to keep fixed size memory, starting with all null memories, then adding
# actual memories every turn
class MemoryNetwork(object):

    def __init__(self,
                 num_actions,
                 utterance_len,
                 embedding_size,
                 hops=3,
                 var_init=tf.random_normal_initializer(stddev=0.1),
                 model_name="MemoryNetwork"):
        # placeholders
        # [batch, mem_size, utter_len]
        self.history = tf.placeholder(tf.float32, [None, None, utterance_len], name="history")
        self.queries = tf.placeholder(tf.float32, [None, utterance_len], name="queries")  # [batch, query_len]
        self.labels = tf.placeholder(tf.float32, [None, num_actions], name="labels")  # [batch, num_actions]
        self.keep_prob = tf.placeholder(tf.float32, [], name='keep_probability')

        # model parameters
        with tf.variable_scope(model_name):
            self.A = [tf.Variable(initial_value=var_init([utterance_len, embedding_size]), name="A" + str(i))
                      for i in range(hops+1)]
            # self.C = tf.Variable(initial_value=var_init([h_utterance_len, embedding_size]), name="C")
            self.W = tf.Variable(initial_value=var_init([embedding_size, num_actions]), name="W")
            self.H = tf.Variable(initial_value=var_init([embedding_size, embedding_size]), name="H")
            self.hops = hops
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
            self.logits = tf.nn.dropout(tf.matmul((o + u), self.W), self.keep_prob)  # [batch, actions]
            self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=self.labels, logits=self.logits))
            self.output_p = tf.nn.softmax(self.logits)
            self.accuracy = tf.reduce_mean(tf.cast(
                tf.equal(tf.argmax(self.logits, axis=1), tf.argmax(self.labels, axis=1)),
                tf.float32))


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
        num_actions = len(label[0])  # trn data can't be empty
        utterance_len = len(history[0][0])  # at least 1 padded memory is in history, always
        if model:
            assert isinstance(model, MemoryNetwork), 'expected a MemoryNetwork as model. Got {}'.format(type(model))
            MemNetPolicy._check_data_model_compatibility(model, num_actions, utterance_len)
            self.model = model
        else:
            self.model = MemoryNetwork(num_actions, utterance_len, embedding_size, hops, var_init,
                                       model_name)
        self.history = history
        self.queries = query
        self.labels = label
        self.batch_indexes = list(batch_indexes)
        self.current_epoch = 0
        self.model_name = model_name
        self.sess = tf.Session()
        self.mem_size = max(len(h) for h in self.history)
        self.encoder = encoder

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
            self.batch_indexes = kwargs['mn_training_data']['batch_indexes']
        if 'mn_dev_data' in kwargs:
            assert 'history' in kwargs['mn_dev_data'], 'no history in the mn_dev_data dictionary'
            assert 'query' in kwargs['mn_dev_data'], 'no queries in the mn_dev_data dictionary'
            assert 'label' in kwargs['mn_dev_data'], 'no labels in the mn_dev_data dictionary'
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
                dev_accuracy, dev_loss = self.sess.run([self.model.accuracy, loss_op],
                                                       feed_dict={self.model.history: kwargs['mn_dev_data']['history'],
                                                                  self.model.queries: kwargs['mn_dev_data']['query'],
                                                                  self.model.labels: kwargs['mn_dev_data']['label'],
                                                                  self.model.keep_prob: 1})
                logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(epoch, dev_loss,
                                                                                                    dev_accuracy,
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

        # restore model
        tf.reset_default_graph()
        model = MemoryNetwork(num_actions, utterance_len, embedding_size, hops=hops)
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
        with open(join(path, 'MemoryNetwork_metadata.pickle'), 'wb') as metadata_fh:
            pickle.dump((self.history, self.queries, self.labels, self.batch_indexes, self.model.hops,
                         self.model.embedding_size, self.current_epoch, self.model_name, self.encoder.path,
                         self.encoder.kb_filename, self.encoder.vocab_filename), metadata_fh)
        # persist model variables
        saver = tf.train.Saver()
        saver.save(self.sess, join(path, "MemoryNetwork"))

    @classmethod
    def load(cls, path, featurizer, max_history):
        # restore metadata
        with open(join(path, 'MemoryNetwork_metadata.pickle'), 'rb') as metadata_fh:
            history, queries, labels, batch_indexes, hops, embedding_size, current_epoch, model_name, nlu_path, \
            kb_filename, vocab_filename = pickle.load(metadata_fh)
        num_actions = len(labels[0])
        utterance_len = len(history[0][0])

        # restore model
        tf.reset_default_graph()
        model = MemoryNetwork(num_actions, utterance_len, embedding_size, hops=hops)
        mem_net_policy = cls(history, queries, labels, batch_indexes, model=model,
                             embedding_size=embedding_size, hops=hops, encoder=MemNetT6DataAdapter(nlu_path,
                                                                                                   kb_filename,
                                                                                                   vocab_filename))
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


# class Featurizer(object):
#
#     def encode(self, tracker, memory_size):
#         raise NotImplementedError
#
#
# class BabiT5Featurizer(Featurizer):
#     def __init__(self, memory_size=8):
#         self.ignored_actions = [ACTION_RESTART_NAME, ACTION_LISTEN_NAME]
#         self.memory_size = memory_size
#         self.data_adapter = MemNetT5DataAdapter()
#
#     def encode(self, tracker, memory_size):
#         query = self.data_adapter.featurize_query(tracker.latest_message.intent['name'],
#                                                   tracker.latest_message.entities)
#         # build history
#         h = [ev for ev in tracker.events if (isinstance(ev, ActionExecuted) and
#                                              ev.action_name not in self.ignored_actions) or
#              isinstance(ev, UserUttered)]
#         for i, e in zip(range(len(h)-1, -1, -1), h[::-1]):  # remove the last UserUttered, since that is the query
#             if isinstance(e, UserUttered):  # this could simply be h.pop(len(h)-1), dunno why I'm so complicated
#                 h.pop(i)
#                 break
#         turns = [int(t / 2) for t in range(0, len(h))]  # [0, 0, 1, 1, 2, 2, .... floor((len(h)-1)/2)]
#         h = [(t, ev) for t, ev in zip(turns, h)]  # adding the turn now that non-relevant events are out
#         h = h[::-1][:memory_size][::-1]
#         memory = []
#         bot_padding = max(0, self.data_adapter.len_user_featurized_vec() - self.data_adapter.len_bot_featurized_vec())
#         user_padding = max(0, self.data_adapter.len_bot_featurized_vec() - self.data_adapter.len_user_featurized_vec())
#         for t, u in h:
#             if isinstance(u, ActionExecuted):
#                 memory.append(self.data_adapter.featurize_bot_act(u.action_name, t, bot_padding))
#             elif isinstance(u, UserUttered):
#                 memory.append(self.data_adapter.featurize_user_act(u.intent['name'], u.entities, t, user_padding))
#         memory = [[0] * self.data_adapter.utterance_len()] if not memory else memory
#         # empty memories will have just 1 0-padded cell
#         return query, memory

