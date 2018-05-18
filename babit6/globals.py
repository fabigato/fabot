from os.path import join, expanduser

RASA_TRAIN_PATH = 'data/rasa/'
RASA_TST_PATH = 'data/test/rasa/'
NLU_TRAIN_CONFIG_FILE = "nlu_model_config.json"
NLU_MODEL_PATH = 'saved_models/nlu/'
DIALOGUE_T5_MODEL_PATH = 'saved_models/dialogue_t5/'
DIALOGUE_T6_MODEL_PATH = 'saved_models/dialogue_t6/'
NLU_TEST_CONFIG_FILE = 'tests/data/nlu_model_test_config.json'
DSTC2_DATA_PATH = 'data/dstc2/data/'
DSTC2_ONTOLOGY_FILE = 'data/dstc2/config/ontology_dstc2.json'
DSTCT2_TRN_LIST_FILE = 'data/dstc2/config/dstc2_train.flist'
DSTCT2_DEV_LIST_FILE = 'data/dstc2/config/dstc2_dev.flist'
DSTCT2_TST_LIST_FILE = 'data/dstc2/config/dstc2_test.flist'
DOMAIN_T6_FILE = 'fabot_t6_domain.yml'
DOMAIN_T5_FILE = 'fabot_t5_domain.yml'
BABI_PATH = 'data/dialog-bAbI-tasks/'
BABI_T6_TRN_FILE = join(BABI_PATH, 'dialog-babi-task6-dstc2-trn.txt')
BABI_T6_DEV_FILE = join(BABI_PATH, 'dialog-babi-task6-dstc2-dev.txt')
BABI_T6_TST_FILE = join(BABI_PATH, 'dialog-babi-task6-dstc2-tst.txt')
BABI_T6_KB_FILE = join(BABI_PATH, 'dialog-babi-task6-dstc2-kb.txt')
BABI_T5_TRN_FILE = join(BABI_PATH, 'dialog-babi-task5-full-dialogs-trn.txt')
BABI_T5_DEV_FILE = join(BABI_PATH, 'dialog-babi-task5-full-dialogs-dev.txt')
BABI_T5_TST_FILE = join(BABI_PATH, 'dialog-babi-task5-full-dialogs-tst.txt')
BABI_T5_KB_FILE = join(BABI_PATH, 'dialog-babi-kb-all.txt')
NLU_T5_MODEL_NAME = 'babi_t5'
NLU_T6_MODEL_NAME = 't6new'
W2VEC_MODEL_PATH = expanduser('~/GoogleNews-vectors-negative300.bin')
NLU_T6_MODEL_PATH = join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME)
NLU_T6_MODEL_PATH = join(NLU_MODEL_PATH, NLU_T5_MODEL_NAME)
