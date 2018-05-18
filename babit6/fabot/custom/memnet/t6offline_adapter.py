from data import t6_bot_das, t6_act2id, t6_extract_entities, t6_featurize_bot_act, bow_features
from data.database import BabiDB
from os.path import isfile

from data.babi_reader import BabiReader
import logging
import gensim
from rasa_core.actions.action import ACTION_LISTEN_NAME, ACTION_RESTART_NAME
from copy import copy

logger = logging.getLogger(__name__)




def format_babi_data(self, filename):
    """
    produces bAbI data in a format suitable for the memory network. Each conversation provides as many training examples
    as turns. Turn i produces a training example that contains the conversation history up to turn i-1, the user
    utterance from turn i and the bot action at turn i
    :param filename: bAbI conversation filename
    :return: List of training examples with labels. Each element is a Dictionary['history': h, 'query': q, 'label': l]
    h: List, so that h[i] is either user_said or bot_said. user_said is a vector featurizing the user sentence, as
    returned by _featurize_user_act, padded so that it is always the same length as bot_said. bot_said is a vector
    featurizing the bot action, as returned by _featurize_bot_act, padded so that it is always the same length as
    user_said
    q: vector indicating the user utterance at the current turn (in the same format as user_said from h)
    l: 1 hot vector indicating the bot action at the current turn
    """
    data = []
    bot_padding = max(0, self.len_user_featurized_vec() - self.len_bot_featurized_vec())
    user_padding = max(0, self.len_bot_featurized_vec() - self.len_user_featurized_vec())
    for story in BabiReader.babi_dialogue_iterator(filename):
        h = []
        for i, turn in enumerate(story):
            # EXTREMELY important to calculate user feats before bot's, cause both affect context_features and
            # whatever the bot replies in a turn, should not affect the featurization of the user utterance
            user_said = self.featurize_user_act(*self.parser.get_user_act(turn['human']), i, user_padding,
                                                turn['human'])
            bot_said = self.featurize_bot_act(self.parser.get_bot_act(turn['bot']), i, bot_padding)  # just to calculate context features
            data.append({'history': copy(h), 'query': user_said,
                         'label': self._format_label(self.parser.get_bot_act(turn['bot']))})
            h.append(user_said)
            h.append(bot_said)
        self._reset()
    return data

def encode(self, tracker, memory_size):
    """
    Encondes the current user utterance as a MemoryNetwork formatted data point
    :param tracker: Rasa tracker object with the state of the conversation
    :param memory_size: number of previous utterances to consider in the history. For best results, use the same
    value the MemoryNetwork was trained with
    :return: query, memory. Query is a vector representing the featurized user message; memory is a list of vectors
    representing the last memory_size utterances in the history
    """
    # build history
    h = [ev for ev in tracker.events if (isinstance(ev, ActionExecuted) and
                                         ev.action_name not in self.ignored_actions) or
         isinstance(ev, UserUttered)]
    turns = [int(t / 2) for t in range(0, len(h))]  # [0, 0, 1, 1, 2, 2, .... floor((len(h)-1)/2)]
    h = [(t, ev) for t, ev in zip(turns, h)]  # adding the turn now that non-relevant events are out
    # h = [(t, ev) for t, ev in enumerate(h)]
    h = h[::-1][:memory_size][::-1]
    memory = []
    for t, u in h:
        if isinstance(u, ActionExecuted):
            memory.append(self.featurize_bot_act(u.action_name, t, self.bot_padding))
        elif isinstance(u, UserUttered):
            memory.append(self.featurize_user_act(u.intent['name'], u.entities, t, self.user_padding, u.text))
    query = memory.pop()  # remove the last one, since that one is query
    memory = [[0] * self.utterance_len()] if not memory else memory
    return query, memory
