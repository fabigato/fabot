from copy import deepcopy
from data.database import BABI_MESSAGES
from data.dialogue_processor import BOT_DAS
import re
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.direct import CollectingOutputChannel
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
        output_channel = CollectingOutputChannel()
        bar = progressbar.ProgressBar(max_value=1117)
        for story in bar(babi_dialogue_iterator(test_conversation_filename)):
            conversation = []
            clean_story = cls.story_cleaner(story)
            output_channel.messages.clear()
            for human_says in [turn['human'] for turn in clean_story]:
                bot_said = agent.handle_message(human_says, output_channel=output_channel)
            agent.tracker_store = Agent.create_tracker_store(store=None, domain=agent.domain)
            for human, target, actual in zip([turn['human'] for turn in clean_story],
                                             [turn['bot'] for turn in clean_story],
                                             bot_said):
                match = cls.sentence_match(target, actual)
                conversation.append({'human': human, 'bot': actual, 'target': target, 'match': match})
            results.append(conversation)
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


class BabiComparatorV2(BabiComparator):

    @classmethod
    def story_cleaner(cls, story):
        """
        story cleaner meant to be as comparable as possible with other authors like Bordes (E2E MN) and Williams (HCN)
        -removes first (<SILENCE> - Welcome) pair (this is a trivial task for this bot that can be hardcoded, therefore
        we will simply add 1/(len(coversation)+1) points to each conversation at the end
        -does not remove the 'repeat' utterances. We'll take the hit on them, as other authors did
        -if the bot side of pair i is an api call, removes next turn (which is necessarily comprised of a silence from
        the user and an unpredictable offer from the bot. Other authors score the match of this offer, but don't score
        matching the api call. We do the other way around by scoring the correct api call but not the randomly picked
        result
        -removes pairs where user said nothing (i.e. <SILENCE>) (only after processing the above rules). Other authors
        take these hits, so we might consider retraining the bot from scratch with these none sense silences
        """
        cleaned_story = []
        skip_next = False
        for pair in story[1:]:
            if skip_next:
                skip_next = False
                continue
            elif pair['human'] == '<SILENCE>':
                continue
            elif pair['bot'].startswith('api_call '):
                skip_next = True
            cleaned_story.append(pair)
        if '<SILENCE>' in [turn['human'] for turn in cleaned_story]:
            print('missed this motherfucker')
        return cleaned_story

    @staticmethod
    def get_da(utterance):
        """Returns the da associated to a bot utterance, or None if no match exists"""
        for da in BOT_DAS:
            for pattern in BOT_DAS[da]:
                match = pattern.match(utterance)
                if match:
                    return da
        return None


    @classmethod
    def sentence_match(cls, target, prediction):
        for da in BOT_DAS:
            for pattern in BOT_DAS[da]:
                match_target = pattern.match(target)
                if match_target:
                    if da == 'api_call':  # if api_call, then we require perfect match
                        return target == prediction
                    for other_pattern in BOT_DAS[da]:
                        match_pred = other_pattern.match(prediction)
                        if match_pred:
                            return True
                    return False
        raise ValueError('No template could match target: {}'.format(target))
