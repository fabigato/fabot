from unittest import TestCase
from data.babi_reader import babi_dialogue_iterator, get_user_act, get_bot_act
from globals import BABI_TRN_DIALOG_FILE, BABI_DEV_DIALOG_FILE, BABI_TST_DIALOG_FILE, BABI_TST_OOV_DIALOG_FILE


class TestBabiReader(TestCase):
    def test_classify_user_das(self):
        unclassified = 0
        for babi_file in [BABI_TRN_DIALOG_FILE, BABI_DEV_DIALOG_FILE, BABI_TST_DIALOG_FILE, BABI_TST_OOV_DIALOG_FILE]:
            print('checking {}:'.format(babi_file))
            for story in babi_dialogue_iterator(babi_file):
                for turn in story:
                    text = turn['human']
                    act, _ = get_user_act(text)
                    if act is None:
                        unclassified += 1
                        print('unknown da: {}'.format(text))
            print('unclassified: {}'.format(unclassified))

    def test_classify_bot_das(self):
        unclassified = 0
        for babi_file in [BABI_TRN_DIALOG_FILE, BABI_DEV_DIALOG_FILE, BABI_TST_DIALOG_FILE, BABI_TST_OOV_DIALOG_FILE]:
            print('checking {}:'.format(babi_file))
            for story in babi_dialogue_iterator(babi_file):
                for turn in story:
                    text = turn['bot']
                    act = get_bot_act(text)
                    if act is None:
                        unclassified += 1
                        print('unknown da: {}'.format(text))
            print('unclassified: {}'.format(unclassified))
