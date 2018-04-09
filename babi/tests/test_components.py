from unittest import TestCase
from globals import RASA_TRAIN_PATH, NLU_TRAIN_CONFIG_FILE, NLU_MODEL_PATH, NLU_TEST_CONFIG_FILE


class TestNLU(TestCase):

    def test_nlu_with_train(self):
        from rasa_nlu.converters import load_data
        from rasa_nlu.config import RasaNLUConfig
        from rasa_nlu.model import Trainer
        from rasa_nlu.evaluate import run_evaluation

        # train
        training_data = load_data(RASA_TRAIN_PATH + 'dstc2_nlu_train.json')
        trainer = Trainer(RasaNLUConfig(NLU_TRAIN_CONFIG_FILE))
        trainer.train(training_data)
        model_directory = trainer.persist(NLU_MODEL_PATH, project_name='fabot', fixed_model_name="current")

        # evaluate
        run_evaluation(config=RasaNLUConfig(NLU_TEST_CONFIG_FILE), model_path=model_directory)

    def test_nlu(self):
        from rasa_nlu.evaluate import run_evaluation
        from rasa_nlu.config import RasaNLUConfig
        run_evaluation(config=RasaNLUConfig(NLU_TEST_CONFIG_FILE), model_path='models/nlu/fabot/current')

    def test_entities(self):
        from rasa_nlu.config import RasaNLUConfig
        from rasa_nlu.converters import load_data
        from rasa_nlu.model import Interpreter
        from rasa_nlu.evaluate import get_targets, get_predictions, get_entity_extractors, evaluate_entities
        config = RasaNLUConfig(NLU_TEST_CONFIG_FILE)
        model_path = NLU_MODEL_PATH
        # get the metadata config from the package data
        test_data = load_data(config['data'], config['language'])
        interpreter = Interpreter.load(model_path, config, None)
        intent_targets, entity_targets = get_targets(test_data)
        intent_predictions, entity_predictions, tokens = get_predictions(interpreter, test_data)
        extractors = get_entity_extractors(interpreter)

        evaluate_entities(entity_targets, entity_predictions, tokens, extractors)
