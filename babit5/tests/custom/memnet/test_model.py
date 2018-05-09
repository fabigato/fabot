from unittest import TestCase
from custom.memnet.model import MemoryNetwork
import tensorflow as tf
from globals import BABI_TRN_DIALOG_FILE, BABI_DEV_DIALOG_FILE, BABI_TST_DIALOG_FILE, PERSISTED_NLU_PATH, \
    PERSISTED_DIALOG_UTTERS_PATH, NLU_T5_MODEL_NAME, BABI_TST_OOV_DIALOG_FILE
from custom.memnet.data_utils import format_babi_data, build_batches, utterance_len, query_len
from data.babi_reader import babi_dialogue_iterator, get_bot_act
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.direct import CollectingOutputChannel
from os.path import join
import json
from numpy import mean
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


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
        dev_data = format_babi_data(BABI_DEV_DIALOG_FILE)
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

    def test_model_with_nlu(self):
        interpreter = RasaNLUInterpreter(join(PERSISTED_NLU_PATH, NLU_T5_MODEL_NAME))
        agent = Agent.load(PERSISTED_DIALOG_UTTERS_PATH, interpreter=interpreter)
        output_channel = CollectingOutputChannel()

        def do_test(input_filename, output_filename):
            results = []
            for story in babi_dialogue_iterator(input_filename):
                conversation = []
                output_channel.messages.clear()
                for human_says in [turn['human'] for turn in story]:
                    bot_said = agent.handle_message(human_says, output_channel=output_channel)
                agent.tracker_store = Agent.create_tracker_store(store=None, domain=agent.domain)  # reset agent
                for human, target, actual in zip([turn['human'] for turn in story],
                                                 [turn['bot'] for turn in story],
                                                 bot_said):
                    target_act = get_bot_act(target)
                    actual_act = get_bot_act(actual)
                    if target_act in ['give_phone', 'give_address', 'suggest_restaurant']:
                        match = actual_act == target_act  # just check the act, won't check restaurant names
                    else:
                        match = target == actual  # for all other cases, require perfect string match
                    act_match = target_act == actual_act
                    conversation.append({'human': human, 'bot': actual, 'target': target, 'match': match,
                                         'act_match': act_match})
                results.append(conversation)
                with open(output_filename, 'w') as result_output:
                    json.dump(results, result_output, indent=2)
        do_test(BABI_TST_DIALOG_FILE, 'tests/custom/memnet/results.json')
        do_test(BABI_TST_OOV_DIALOG_FILE, 'tests/custom/memnet/results_oov.json')

    def test_compute_memnet_test_stats(self):
        def do_test(results_filename):
            with open(results_filename, 'r') as fh:
                results = json.load(fh)
                total_matches, perfect, total = 0, 0, 0
                for i, conversation in enumerate(results):
                    conversation_matches = 0
                    for turn in conversation:
                        if turn['match']:
                            conversation_matches += 1
                        total += 1
                    total_matches += conversation_matches
                    if conversation_matches == len(conversation):
                        perfect += 1
                    print(
                        'Dialogue {i}: matches: {conversation_matches}/{total_conversation} total: '
                        '{total_matches}/{total} ({total_percent:.2%}) perfect conversations: '
                        '{perfect}/{conversations} ({dialog_total_percent:.2%})'
                        '\n\n'.format(
                            i=i,
                            conversation_matches=conversation_matches,
                            total_conversation=len(conversation),
                            total_matches=total_matches,
                            total=total,
                            total_percent=total_matches/total,
                            perfect=perfect,
                            conversations=len(results),
                            dialog_total_percent=perfect/len(results)
                        ))
        print('test results:\n')
        do_test('tests/custom/memnet/results.json')
        print('OOV test results:\n')
        do_test('tests/custom/memnet/results_oov.json')
