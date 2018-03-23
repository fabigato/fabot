from unittest import TestCase
from data.database import BabiDB
from main import BABI_PATH
from os.path import join


class TestDatabase(TestCase):
    def test_find_restaurant(self):
        db = BabiDB(join(BABI_PATH, 'dialog-babi-task6-dstc2-kb.txt'))
        results = db.find_restaurant(food='british', pricerange='cheap')
        print(results.iloc[0]['name'])

