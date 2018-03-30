from unittest import TestCase
from data.test import babi_reader
from main import BABI_PATH
from os.path import join


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
