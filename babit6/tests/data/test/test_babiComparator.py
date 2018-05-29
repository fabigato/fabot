from unittest import TestCase
from data.test import babi_reader
from globals import BABI_PATH
from os.path import join
from json import load as json_load
from collections import Counter

COMPARATOR_FILENAME = 'tests/data/test/babi_test2_results.json'


class TestBabiComparatorBasic(TestCase):
    def test_bot(self):
        results = babi_reader.BabiComparatorBasic.test_bot(
            test_conversation_filename=join(BABI_PATH, 'dialog-babi-task6-dstc2-tst.txt'),
            nlu_model_path='models/nlu/fabot/current', dialogue_model_path='models/dialogue',
            output_filename='tests/data/test/babi_test_results100.json'
        )
        print('processing results')
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
            print('Dialogue {i}: matches: {conversation_matches}/{total_conversation} total: {total_matches}/{total}'
                  ' perfect conversations: {perfect}/{conversations}'.format(i=i,
                                                                             conversation_matches=conversation_matches,
                                                                             total_conversation=len(conversation),
                                                                             total_matches=total_matches,
                                                                             total=total,
                                                                             perfect=perfect,
                                                                             conversations=len(results)))


class TestBabiComparatorV2(TestCase):
    def test_bot(self):
        results = babi_reader.BabiComparatorV2.test_bot(
            test_conversation_filename=join(BABI_PATH, 'dialog-babi-task6-dstc2-tst.txt'),
            nlu_model_path='models/nlu/fabot/current', dialogue_model_path='models/dialogue',
            output_filename=COMPARATOR_FILENAME
        )
        print('processing results')
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
            print('Dialogue {i}: matches: {conversation_matches}/{total_conversation} total: {total_matches}/{total}'
                  ' perfect conversations: {perfect}/{conversations}'.format(i=i,
                                                                             conversation_matches=conversation_matches,
                                                                             total_conversation=len(conversation),
                                                                             total_matches=total_matches,
                                                                             total=total,
                                                                             perfect=perfect,
                                                                             conversations=len(results)))

    def test_analise_comparator_file(self):
        with open(COMPARATOR_FILENAME, 'r') as file_handler:
            comparison_data = json_load(file_handler)
            fn_misses = [babi_reader.BabiComparatorV2.get_da(turn['target']) for conversation in comparison_data
                         for turn in conversation if not turn['match']]
            fn_misses = Counter(fn_misses)
            print('false negatives: {}'.format(fn_misses.most_common()))
            print(sum(fn_misses.values()))

            fp_misses = [babi_reader.BabiComparatorV2.get_da(turn['bot']) for conversation in comparison_data
                         for turn in conversation if not turn['match']]
            fp_misses = Counter(fp_misses)
            print('false positives: {}'.format(fp_misses.most_common()))
            print(sum(fp_misses.values()))
