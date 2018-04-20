from unittest import TestCase
from custom.memnet import data_utils
from globals import BABI_TRN_DIALOG_FILE, BABI_TST_DIALOG_FILE
import matplotlib.pyplot as plt


class TestData(TestCase):
    def test_format_data(self):
        trn_data = data_utils.format_babi_data(BABI_TRN_DIALOG_FILE)

        # plot story len histogram
        h_lens = [len(x['history']) for x in trn_data]
        plt.hist(h_lens, 50, density=False, facecolor='g', alpha=0.75)
        plt.xlabel('history len')
        plt.ylabel('frequency')
        plt.title('Histogram of frequencies')
        # plt.axis([40, 160, 0, 0.03])
        plt.grid(True)
        plt.show()

        history, query, label, batches = data_utils.build_batches(data=trn_data, batch_size=64, max_memory_size=40,
                                                                  utterance_length=data_utils.utterance_len())
        tst_data = data_utils.format_babi_data(BABI_TST_DIALOG_FILE)
