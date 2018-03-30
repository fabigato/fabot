from copy import deepcopy
from data.database import BABI_MESSAGES
import re
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.channels import UserMessage
from rasa_core.events import Restarted
import json
import progressbar

for da in BABI_MESSAGES:
    BABI_MESSAGES[da] = [re.compile(pattern) for pattern in BABI_MESSAGES[da]]


def babi_dialogue_iterator(babi_filename):
    """
    Generator for bAbI stories. Skips api call results
    :param babi_filename: bAbI file name
    :return: list of message exchanges, as dictionaries with 'human', 'bot' pairs
    """
    story = []
    with open(babi_filename, 'r') as babi_file:
        for line in babi_file:
            if line == '\n':  # end of story
                _story = deepcopy(story)
                story = []
                yield _story
            chunks = line.split('\t')
            chunks[0] = ' '.join(chunks[0].split(' ')[1:])  # rid of initial number
            if len(chunks) == 1:  # api call results, garbage
                continue
            elif len(chunks) == 2:  # normal line
                human, bot = chunks
                story.append({'human': human, 'bot': bot[:-1]})  # removing final \n
            else:
                raise Exception('Unknown formatted line: {}'.format(line))


class BabiComparator(object):

    @classmethod
    def story_cleaner(cls, story):
        """
        Cleans a story. Must be overriden by child class
        :param story: story to clean, as an ordered iterable of dictionaries with 'human' and 'bot' keys
        :return: cleaned story, same format as original story
        """
        raise NotImplementedError

    @classmethod
    def sentence_match(cls, target, prediction):
        """
        Determines if two bot sentences are equivalent. Since bAbI bot replies are not completely deterministic, it
        may be preferable to infer the dialogue act from grammar hints
        :param target: bAbI ground truth
        :param prediction: bot prediction to compare
        :return: True if target and prediction are equivalent, else False
        """
        raise NotImplementedError

    @classmethod
    def test_bot(cls, test_conversation_filename, nlu_model_path, dialogue_model_path, output_filename=None):
        import numpy as np
        np.random.seed(42)
        interpreter = RasaNLUInterpreter(nlu_model_path)
        agent = Agent.load(dialogue_model_path, interpreter=interpreter)
        results = []
        counter = 0
        output_channel = CollectingOutputChannel()
        bar = progressbar.ProgressBar(max_value=1117)
        for story in bar(babi_dialogue_iterator(test_conversation_filename)):
            counter += 1
            conversation = []
            clean_story = cls.story_cleaner(story)
            output_channel.messages.clear()
            for human_says in [turn['human'] for turn in clean_story]:
                bot_said = agent.handle_message(human_says, output_channel=output_channel)
            tracker = agent.tracker_store.get_or_create_tracker(UserMessage.DEFAULT_SENDER_ID)
            tracker.update(Restarted())
            agent.tracker_store.save(tracker)
            # agent = Agent.load(dialogue_model_path, interpreter=interpreter)
            for human, target, actual in zip([turn['human'] for turn in clean_story],
                                             [turn['bot'] for turn in clean_story],
                                             bot_said):
                match = cls.sentence_match(target, actual)
                conversation.append({'human': human, 'bot': actual, 'target': target, 'match': match})
            results.append(conversation)
            if counter == 100:
                break
            if output_filename:
                with open(output_filename, 'w') as result_output:
                    json.dump(results, result_output, indent=2)
        return results


class BabiComparatorBasic(BabiComparator):

    @classmethod
    def story_cleaner(cls, story):
        """
        Basic story cleaner.
        -removes first (<SILENCE> - Welcome) pair
        -removes pairs where bot said 'Could you please repeat that?'
        -if the bot side of pair i is an api call, replaces it with the bot side of pair i+1 (the result of the
        api call), then deletes pair i+1
        -removes pairs where user said nothing (i.e. <SILENCE>) (only after processing the above rules)
        """
        cleaned_story = []
        replace_last_bot = False
        for pair in story[1:]:
            if replace_last_bot:
                replace_last_bot = False
                cleaned_story[-1]['bot'] = pair['bot']
                continue
            if pair['bot'] == 'Could you please repeat that?':
                continue
            elif pair['bot'].startswith('api_call '):
                replace_last_bot = True
            elif pair['human'] == '<SILENCE>':
                continue
            cleaned_story.append(pair)

        return cleaned_story

    @classmethod
    def sentence_match(cls, target, prediction):
        for da in BABI_MESSAGES:
            for pattern in BABI_MESSAGES[da]:
                match_target = pattern.match(target)
                if match_target:
                    for other_pattern in BABI_MESSAGES[da]:
                        match_pred = other_pattern.match(prediction)
                        if match_pred:
                            return True
                    return False
        raise ValueError('No template could match target: {}'.format(target))
