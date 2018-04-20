from json import load
from os.path import join

BABI_TASKS_PATH = 'data/dialog-bAbI-tasks'
PERSISTED_DIALOG_PATH = 'persisted_model/dialog'
PERSISTED_DIALOG_UTTERS_PATH = 'persisted_model/dialog_utters'
DIALOG_TRAINING_DATA_FILE = 'data/rasa/dialog_trn.md'
DIALOG_TRAINING_DATA_UTTER_FILE = 'data/rasa/dialog_trn_utter.md'
NLU_CONFIG_FILE = 'nlu_config.json'
NLU_DEV_CONFIG_FILE = 'tests/data/nlu_dev_config.json'

with open(NLU_CONFIG_FILE) as ncf:
    nlu_config_data = load(ncf)
NLU_TRAINING_DATA_FILE = nlu_config_data['data']
PERSISTED_NLU_PATH = nlu_config_data['path']
NLU_MODEL_NAME = 'rasa'
DOMAIN_TEMPLATES_FILE = 'domain_templates.yml'
DOMAIN_CODE_FILE = 'domain_code.yml'

BABI_CANDIDATES_FILE = join(BABI_TASKS_PATH, 'dialog-babi-candidates.txt')
BABI_KB_FILE = join(BABI_TASKS_PATH, 'dialog-babi-kb-all.txt')
BABI_TRN_DIALOG_FILE, BABI_DEV_DIALOG_FILE, BABI_TST_DIALOG_FILE, BABI_TST_OOV_DIALOG_FILE = \
    (join(BABI_TASKS_PATH, file) for file in
     ['dialog-babi-task5-full-dialogs-trn.txt', 'dialog-babi-task5-full-dialogs-dev.txt',
      'dialog-babi-task5-full-dialogs-tst.txt', 'dialog-babi-task5-full-dialogs-tst-OOV.txt'])
