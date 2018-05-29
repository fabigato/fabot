from unittest import TestCase
from fabot.custom.lstm.model import CustomLSTM


class TestCustomLSTM(TestCase):
    def test_tmp(self):
        lstm = CustomLSTM(hidden_size=50, num_actions=56, input_dim=856)
        print('done')
