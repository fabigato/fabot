from unittest import TestCase
from data.database import BabiDB, BABI_MESSAGES
from globals import BABI_PATH
from os.path import join
import re


class TestDatabase(TestCase):
    def test_find_restaurant(self):
        db = BabiDB(join(BABI_PATH, 'dialog-babi-task6-dstc2-kb.txt'))
        results = db.find_restaurant(pricerange='moderate', area='west')
        print(results.iloc[0]['name'])

    def test_babi_messages(self):
        from progressbar import ProgressBar
        for da in BABI_MESSAGES:
            BABI_MESSAGES[da] = [re.compile(pattern) for pattern in BABI_MESSAGES[da]]
        with open(join(BABI_PATH, 'dialog-babi-task6-dstc2-candidates.txt'), 'r') as babi_kb_handler:
            lines = babi_kb_handler.readlines()
            bar = ProgressBar()
            for line in bar(lines):
                line = line[2:-1]
                matched = False
                for da in BABI_MESSAGES:
                    for pattern in BABI_MESSAGES[da]:
                        if pattern.match(line):
                            matched = True
                            continue
                if not matched:
                    print('troublesome utterance: {}'.format(line))
