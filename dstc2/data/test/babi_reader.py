from main import BABI_PATH
from os.path import join
from copy import deepcopy


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

    @staticmethod
    def story_cleaner(story):
        """
        Cleans a story. Must be overriden by child class
        :param story: story to clean, as an ordered iterable of dictionaries with 'human' and 'bot' keys
        :return: cleaned story, same format as original story
        """
        raise NotImplementedError

    @staticmethod
    def sentence_match(target, prediction):
        """
        Determines if two bot sentences are equivalent. Since bAbI bot replies are not completely deterministic, it
        may be preferable to infer the dialogue act from grammar hints
        :param target: bAbI ground truth
        :param prediction: bot prediction to compare
        :return: True if target and prediction are equivalent, else False
        """
        raise NotImplementedError


class BabiComparatorBasic(BabiComparator):

    @staticmethod
    def story_cleaner(story):
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

    @staticmethod
    def sentence_match(target, prediction):
        pass#if target


if __name__ == '__main__':
    for story in babi_dialogue_iterator(join(BABI_PATH, 'dialog-babi-task6-dstc2-tst.txt')):
        cleaned = BabiComparatorBasic.story_cleaner(story)
