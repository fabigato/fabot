from unittest import TestCase
import logging
from fabot.custom.memnet.data_utils import MemNetDataAdapter, MemNetT5DataAdapter, MemNetT6DataAdapter
from globals import BABI_T5_TRN_FILE, BABI_T5_DEV_FILE, BABI_T6_TRN_FILE, BABI_T6_DEV_FILE, NLU_MODEL_PATH, \
    NLU_T6_MODEL_NAME, DIALOGUE_T6_MODEL_PATH, BABI_T6_TST_FILE
from os.path import join, isfile
import tensorflow as tf
from fabot.custom.memnet.model import MemoryNetwork
from numpy import mean
import pickle
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.direct import CollectingOutputChannel
from data.babi_reader import BabiReader, BabiT6Reader
import json


class TestMemoryNetwork(TestCase):
    def test_model_t5(self):
        data_adapter = MemNetT5DataAdapter()
        hops = 2
        actions = len(data_adapter.act2id)
        h_len = data_adapter.utterance_len()
        q_len = data_adapter.query_len()
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

        trn_history, trn_query, trn_label, batch_indexes = MemNetDataAdapter.build_batches(
            data=data_adapter.format_babi_data(filename=BABI_T5_TRN_FILE),
            batch_size=batch, max_memory_size=mem_size,
            utterance_length=h_len)
        dev_data = data_adapter.format_babi_data(filename=BABI_T5_DEV_FILE)
        dev_history, dev_query, dev_label, _ = data_adapter.build_batches(dev_data, batch_size=len(dev_data),
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

    def test_model_t6(self):
        data_adapter = MemNetT6DataAdapter(join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME))
        actions = len(data_adapter.act2id)
        h_len = data_adapter.utterance_len()
        q_len = data_adapter.query_len()

        print_cycle = 100
        hops = 1
        embedding_size = 20
        batch = 32
        mem_size = 8
        epochs = 40
        clip_norm = 25
        keep_prob = 0.86
        logging.info(
            'starting training\nConfig:\nhops: {}\nactions: {}\nhistory utterance length: {}\nquery length: {}\n'
            'embedding size: {}\nbatch size: {}\nmemory size: {}\nepochs: {}\ngradient clip norm: {}\n'
            'keep prob: {}\n'.format(hops, actions, h_len, q_len, embedding_size, batch, mem_size, epochs,
                                     clip_norm,
                                     keep_prob))
        saved_batches = 'tests/fabot/custom/memnet/trn_t6_batches.pickle'
        if isfile(saved_batches):
            with open(saved_batches, 'rb') as batches_fh:
                trn_history, trn_query, trn_label, batch_indexes = pickle.load(batches_fh)
        else:
            print('train batches data not found, now recreating it')
            trn_history, trn_query, trn_label, batch_indexes = MemNetDataAdapter.build_batches(
                data=data_adapter.format_babi_data(filename=BABI_T6_TRN_FILE),
                batch_size=batch, max_memory_size=mem_size,
                utterance_length=h_len)
            print('saving data')
            with open(saved_batches, 'wb') as batches_fh:
                pickle.dump((trn_history, trn_query, trn_label, batch_indexes), batches_fh)
            print('saved')
        saved_batches = 'tests/fabot/custom/memnet/dev_t6_batches.pickle'
        if isfile(saved_batches):
            with open(saved_batches, 'rb') as batches_fh:
                dev_history, dev_query, dev_label = pickle.load(batches_fh)
        else:
            print('dev batches data not found, now recreating it')
            dev_data = data_adapter.format_babi_data(filename=BABI_T6_DEV_FILE)
            dev_history, dev_query, dev_label, _ = data_adapter.build_batches(dev_data, batch_size=len(dev_data),
                                                                              max_memory_size=mem_size,
                                                                              utterance_length=h_len)
            print('saving data')
            with open(saved_batches, 'wb') as batches_fh:
                pickle.dump((dev_history, dev_query, dev_label), batches_fh)
            print('saved')

        model = MemoryNetwork(num_actions=actions, h_utterance_len=h_len, query_len=q_len,
                              embedding_size=embedding_size,
                              hops=hops)
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

    def test_full_bot_memnet_t6(self):
        interpreter = RasaNLUInterpreter(join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME))
        agent = Agent.load(DIALOGUE_T6_MODEL_PATH, interpreter=interpreter)
        output_channel = CollectingOutputChannel()
        babi_reader = BabiT6Reader(join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME), None)
        results = []
        for story in BabiReader.babi_dialogue_iterator(BABI_T6_TST_FILE):
            conversation = []
            output_channel.messages.clear()
            for human_says in [turn['human'] for turn in story]:
                bot_said = agent.handle_message(human_says, output_channel=output_channel)
            agent.tracker_store = Agent.create_tracker_store(store=None, domain=agent.domain)  # reset agent
            for human, target, actual in zip([turn['human'] for turn in story],
                                             [turn['bot'] for turn in story],
                                             bot_said):
                target_act = babi_reader.get_bot_act(target)
                actual_act = babi_reader.get_bot_act(actual)
                if target_act in ['offer_rest_area_price', 'offer_rest_area_food', 'offer_rest_area_food_price',
                                  'offer_rest_area', 'offer_rest_food_price', 'offer_rest_food', 'offer_rest_price',
                                  'offer_rest_price_postcode', 'offer_rest', 'give_phone', 'give_phone2',
                                  'give_postcode', 'give_address', 'give_area', 'give_address2']:
                    match = actual_act == target_act  # just check the act, won't check restaurant names
                else:
                    match = target == actual  # for all other cases, require perfect string match
                act_match = target_act == actual_act
                conversation.append({'human': human, 'bot': actual, 'target': target, 'match': match,
                                     'act_match': act_match})
            results.append(conversation)
            with open('tests/fabot/custom/memnet/tst_t6_results.json', 'w') as result_output:
                json.dump(results, result_output, indent=2)

    def test_compute_memnet_t6_test_stats(self):
        with open('tests/fabot/custom/memnet/tst_t6_results.json', 'r') as fh:
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
