from unittest import TestCase
from custom.memnet.model import MemoryNetwork
import tensorflow as tf
from globals import BABI_TRN_DIALOG_FILE, BABI_DEV_DIALOG_FILE, BABI_TST_DIALOG_FILE
from custom.memnet.data_utils import format_babi_data, build_batches, utterance_len, query_len
from numpy import mean
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class TestMemoryNetwork(TestCase):
    def test_model(self):
        hops = 2
        actions = 16
        h_len = utterance_len()
        q_len = query_len()
        embedding_size = 10
        batch = 32
        mem_size = 8
        epochs = 40
        clip_norm = 25
        print_cycle = 100
        keep_prob = 0.95
        logging.info(
            'starting training\nConfig:\nhops: {}\nactions: {}\nhistory utterance length: {}\nquery length: {}\n'
            'embedding size: {}\nbatch size: {}\nmemory size: {}\nepochs: {}\ngradient clip norm: {}\n'
            'keep prob: {}\n'.format(hops, actions, h_len, q_len, embedding_size, batch, mem_size, epochs, clip_norm,
                                     keep_prob))

        trn_history, trn_query, trn_label, batch_indexes = build_batches(format_babi_data(BABI_TRN_DIALOG_FILE),
                                                                         batch_size=batch, max_memory_size=mem_size,
                                                                         utterance_length=h_len)
        dev_data = format_babi_data(BABI_TST_DIALOG_FILE)
        dev_history, dev_query, dev_label, _ = build_batches(dev_data, batch_size=len(dev_data),
                                                             max_memory_size=mem_size,
                                                             utterance_length=h_len)

        model = MemoryNetwork(num_actions=actions, h_utterance_len=h_len, query_len=q_len,
                              embedding_size=embedding_size,
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
                             model.labels: trn_label[b_start:b_end],
                             model.keep_prob: keep_prob}
                loss, _ = sess.run([loss_op, train_op], feed_dict=feed_dict)
                feed_dict[model.keep_prob] = 1
                accuracy = sess.run(model.accuracy, feed_dict=feed_dict)
                if i % print_cycle == 0:
                    logging.info('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
                trn_accuracies.append(accuracy)
            dev_accuracy, dev_loss = sess.run([model.accuracy, loss_op], feed_dict={model.history: dev_history,
                                                                                    model.queries: dev_query,
                                                                                    model.labels: dev_label,
                                                                                    model.keep_prob: 1})
            logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(epoch, dev_loss,
                                                                                                dev_accuracy,
                                                                                                mean(trn_accuracies)
                                                                                                ))
