import tensorflow as tf
from rasa_core.policies import Policy
from globals import BABI_TRN_DIALOG_FILE, BABI_DEV_DIALOG_FILE
from custom.memnet.data_utils import format_babi_data, build_batches, utterance_len, query_len
from numpy import mean
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


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
                 h_utterance_len,
                 query_len,
                 embedding_size,
                 hops=3,
                 var_init=tf.random_normal_initializer(stddev=0.1),
                 model_name="MemoryNetwork"):

        # placeholders
        # [batch, mem_size, utter_len]
        self.history = tf.placeholder(tf.float32, [None, None, h_utterance_len], name="history")
        self.queries = tf.placeholder(tf.float32, [None, query_len], name="queries")  # [batch, query_len]
        self.labels = tf.placeholder(tf.float32, [None, num_actions], name="labels")  # [batch, num_actions]

        # model parameters
        with tf.variable_scope(model_name):
            self.A = tf.Variable(initial_value=var_init([h_utterance_len, embedding_size]), name="A")
            self.B = tf.Variable(initial_value=var_init([query_len, embedding_size]), name="B")
            self.C = tf.Variable(initial_value=var_init([h_utterance_len, embedding_size]), name="C")
            self.W = tf.Variable(initial_value=var_init([embedding_size, num_actions]), name="W")
            self.H = tf.Variable(initial_value=var_init([query_len, query_len]), name="H")

            # define graph
            u = tf.matmul(self.queries, self.B)  # [batch, embedding_size]
            for _ in range(hops):
                """we need a matmul on each [mem_size, utter_len] element of history with A. scan takes each element
                # (across 0th dim) of history and applies the lambda function (matmul) to it. Argument x is the element
                # currently processed of history and a is the result of the previous call (the first time, a equals
                # initializer, or history[0] if no initializer present). Since the final value is a concatenation of
                # each call, then each must return a value of same shape. Hence, not providing the initializer causes
                # an exception since result[0] = history[0] which has different shape than matmul(history[i], A).
                # If initializer = None, result[0] is history[0], which is undesired. For result[0] to be 
                # lambda(_, history[0]), there must be an initializer, even if not used, so giving a zero matrix with
                # the right dimensions. These are two other ways to achieve the same:
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
                Since A is missing a dimension to equal mem_size, we just add it with expand_dims and use tile to repeat
                A across mem_size rows (tile requires number of times each dimension gets repeated, hence the 1's) 
                """
                # [batch, mem_size, embedding_size]
                m = tf.matmul(self.history, tf.tile(tf.expand_dims(self.A, 0), [tf.shape(self.history)[0], 1, 1]))
                """This is like doing softmax in np like this:
                    soft = np.exp(p)  # where p is a matrix
                    sum = np.sum(soft, axis=1)  # sum across columns, you get a vector
                    soft /= sum[:, None]  # divide matrix by vector. The None dim is shorthand to add expanded dim in np
                    so that the / broadcasts automatically (just like *)
                """
                # the extra dim added to u causes a broadcast at m * u. reduce_sum just cause no easy dot product in tf
                p = tf.nn.softmax(tf.reduce_sum(m * tf.expand_dims(u, 1), -1))  # [batch, mem]
                c = tf.matmul(self.history, tf.tile(tf.expand_dims(self.C, 0), [tf.shape(self.history)[0], 1, 1]))
                # multiply each of the [batch, mem] c embeddings by scalar p to get weighted average output embedding
                o = tf.reduce_sum(tf.expand_dims(p, -1) * c, axis=1)  # [batch, embedding_size]
            self.logits = tf.matmul((o + u), self.W)  # [batch, actions]
            self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=self.labels, logits=self.logits))
            self.accuracy = tf.reduce_mean(tf.cast(
                tf.equal(tf.argmax(self.logits, axis=1), tf.argmax(self.labels, axis=1)),
                tf.float32))


class MemNetPolicy(Policy):
    def predict_action_probabilities(self, tracker, domain):
        # TODO implement
        pass

    def persist(self, path):
        # TODO implement
        pass

    def train(self, training_data, domain, **kwargs):
        # TODO implement
        pass

    @classmethod
    def load(cls, path, featurizer, max_history):
        raise NotImplementedError


if __name__ == '__main__':
    hops: 1
    actions = 16
    h_len = utterance_len()
    q_len = query_len()
    embedding_size = 10
    batch = 32
    mem_size = 40
    epochs = 60
    clip_norm = 40
    print_cycle = 100
    logging.info('starting training\nConfig:\nhops: {}\nactions: {}\nhistory utterance length: {}\nquery length: {}\n'
                 'embedding size: {}\nbatch size: {}\nmemory size: {}\nepochs: {}\ngradient clip norm: {}\n'.format(
                  actions, h_len, q_len, hops, embedding_size, batch, mem_size, epochs, clip_norm)
    )

    trn_history, trn_query, trn_label, batch_indexes = build_batches(format_babi_data(BABI_TRN_DIALOG_FILE),
                                                                     batch_size=batch, max_memory_size=mem_size,
                                                                     utterance_length=h_len)
    dev_data = format_babi_data(BABI_DEV_DIALOG_FILE)
    dev_history, dev_query, dev_label, _ = build_batches(dev_data, batch_size=len(dev_data), max_memory_size=mem_size,
                                                         utterance_length=h_len)

    model = MemoryNetwork(num_actions=actions, h_utterance_len=h_len, query_len=q_len, embedding_size=embedding_size,
                          hops=1)
    optimizer = tf.train.AdamOptimizer(learning_rate=1e-3, epsilon=1e-8)
    loss_op = model.loss
    grads, vars = zip(*optimizer.compute_gradients(loss_op))
    grads_clipped, _ = tf.clip_by_global_norm(grads, clip_norm=clip_norm)
    train_op = optimizer.apply_gradients(zip(grads_clipped, vars))
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    for epoch in range(epochs):
        batch_indexes = list(batch_indexes)
        trn_accuracies = []
        for i, (b_start, b_end) in enumerate(batch_indexes):
            feed_dict = {model.history: trn_history[b_start:b_end],
                         model.queries: trn_query[b_start:b_end],
                         model.labels: trn_label[b_start:b_end]}
            loss, accuracy, _ = sess.run([loss_op, model.accuracy, train_op], feed_dict=feed_dict)
            if i % print_cycle == 0:
                print('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
            trn_accuracies.append(accuracy)
        dev_accuracy, dev_loss = sess.run([model.accuracy, loss_op], feed_dict={model.history: dev_history,
                                                                                model.queries: dev_query,
                                                                                model.labels: dev_label})
        print('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(epoch, dev_loss, dev_accuracy,
                                                                                     mean(trn_accuracies)))
