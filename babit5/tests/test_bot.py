from unittest import TestCase
from globals import NLU_DEV_CONFIG_FILE, PERSISTED_NLU_PATH, NLU_MODEL_NAME, BABI_TST_DIALOG_FILE, \
    PERSISTED_DIALOG_UTTERS_PATH, BABI_TST_OOV_DIALOG_FILE
from data.babi_reader import babi_dialogue_iterator, get_bot_act
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.direct import CollectingOutputChannel
from os.path import join
import logging
import json


class TestBabiReader(TestCase):
    def test_nlu(self):
        logging.basicConfig(level=logging.INFO)
        from rasa_nlu.evaluate import run_evaluation
        from rasa_nlu.config import RasaNLUConfig
        run_evaluation(config=RasaNLUConfig(NLU_DEV_CONFIG_FILE), model_path=join(PERSISTED_NLU_PATH, NLU_MODEL_NAME))

    def test_entities(self):
        logging.basicConfig(level=logging.INFO)
        from rasa_nlu.config import RasaNLUConfig
        from rasa_nlu.converters import load_data
        from rasa_nlu.model import Interpreter
        from rasa_nlu.evaluate import get_targets, get_predictions, get_entity_extractors, evaluate_entities
        config = RasaNLUConfig(NLU_DEV_CONFIG_FILE)
        model_path = join(PERSISTED_NLU_PATH, NLU_MODEL_NAME)
        # get the metadata config from the package data
        test_data = load_data(config['data'], config['language'])
        interpreter = Interpreter.load(model_path, config, None)
        intent_targets, entity_targets = get_targets(test_data)
        intent_predictions, entity_predictions, tokens = get_predictions(interpreter, test_data)
        extractors = get_entity_extractors(interpreter)

        evaluate_entities(entity_targets, entity_predictions, tokens, extractors)

    def test_bot_template_based(self):
        logging.basicConfig(level=logging.DEBUG)
        results = []
        interpreter = RasaNLUInterpreter(join(PERSISTED_NLU_PATH, NLU_MODEL_NAME))
        agent = Agent.load(PERSISTED_DIALOG_UTTERS_PATH, interpreter=interpreter)
        output = CollectingOutputChannel()
        # counter = 0
        for story in babi_dialogue_iterator(BABI_TST_OOV_DIALOG_FILE):
            # counter += 1
            output.messages.clear()
            for turn in story:
                bot_said = agent.handle_message(turn['human'], output_channel=output)
            agent.tracker_store = Agent.create_tracker_store(store=None, domain=agent.domain)
            results.append([
                {'human': human, 'label': label, 'bot': bot, 'match': get_bot_act(bot) == get_bot_act(label)}
                for human, label, bot in zip(*list(zip(*[turn.values() for turn in story])), bot_said)
            ])
            # if counter == 50:
            #     break
        with open('tests/result_logs/results_template_based_oov.json', 'w') as output_fh:
            json.dump(results, output_fh, indent=2)
        total_matches = len([turn for conversation in results for turn in conversation if turn['match']])
        total_perfect_conversations = len([c for c in results if all([turn['match'] for turn in c])])
        total_turns = len([turn for conversation in results for turn in conversation])
        total_conversations = len(results)
        print('Turn accuracy: {}/{} = {:.2}'.format(total_matches, total_turns, total_matches/total_turns))
        print('Dialog accuracy: {}/{} = {:.2}'.format(total_perfect_conversations, total_conversations,
                                                      total_perfect_conversations/total_conversations))
