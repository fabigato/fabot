from data.babi_reader import BabiT5Reader, BabiT6Reader, BabiReader
from data.database import BabiDB
from copy import copy
from rasa_core.events import ActionExecuted, UserUttered
from rasa_core.actions.action import ACTION_LISTEN_NAME, ACTION_RESTART_NAME
import re


class MemNetDataAdapter(object):
    """
    Class to format bAbI data to a format appropriate for the Memory Network. It must be inherited by bAbI task-specific
    sub classes
    """
    def __init__(self, parser):
        self.parser = parser
        self.ignored_actions = [ACTION_RESTART_NAME, ACTION_LISTEN_NAME]  # necessary to encode in rasa format
        self.bot_padding = max(0, self.len_user_featurized_vec() - self.len_bot_featurized_vec())
        self.user_padding = max(0, self.len_bot_featurized_vec() - self.len_user_featurized_vec())

    def _reset(self):
        """
        gets called after processing each story. Child classes can do any clean up/reset related tasks here
        :return:
        """
        raise NotImplementedError

    def featurize_user_act(self, intent, entities, turn, padding=0):
        """
        Featurizes a user message
        :param intent: str indicating the user intent
        :param entities: iterable of entities in the user message, each one a dictionary with the name of the entity
        under key 'entity'
        :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
        :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have
        same length
        :return: a vector representing the featurized user act
        """
        raise NotImplementedError

    def featurize_bot_act(self, bot_act, turn, padding=0):
        """
        Featurizes a bot message
        :param bot_act: str indicating the bot action. Can come with or without the 'utter_' prefix
        :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
        :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have same
        length
        :return: a vector representing the featurized bot act
        """
        raise NotImplementedError

    # def featurize_query(self, intent, entities):
    #     """
    #     produces a vector of features representing the query in the MemNet
    #     :param intent: user intent, as a string
    #     :param entities: List of entities in the user utterance. Each entity represented as a Dictionary with at least a
    #     'entity' key with the name of the entity as value
    #     :return: List[int] representing the featurized user utterance. It is a 1-hot encoding of the user intent
    #     concatenated with the entities mentioned in the utterance (i.e. a 4-dimensional binary vector, bits representing
    #     cuisine, location, number and price)
    #     """
    #     entity_vec = [0] * len(self.entity2id)
    #     for e in entities:
    #         entity_vec[self.entity2id[e['entity']]] = 1
    #     intent_vec = [0] * len(self.intent2id)
    #     if intent:  # user might say literally '', in that case we don't set a 1 in the query/utterance
    #         intent_vec[self.intent2id[intent]] = 1
    #     return intent_vec + entity_vec + [0]

    def len_user_featurized_vec(self):
        raise NotImplementedError

    def len_bot_featurized_vec(self):
        raise NotImplementedError

    def utterance_len(self):
        return max(self.len_bot_featurized_vec(), self.len_user_featurized_vec())

    @staticmethod
    def build_batches(data, utterance_length, batch_size=32, max_memory_size=8):
        """
        Produces batch indexes of points with similar length of history and adds padding so that the history component of
        all points in a batch have the same length
        :param data: List of data points. Each one a Dictionary with keys 'history', 'query' and 'label'. history is a List
        with all utterances in a conversation prior to the current turn, alternating between user and bot. The first one is
        always from the user and the last one is always from the bot (therefore, it has always even length). The utterances
        are List[int] representations, and are always the same length (i.e. bot and user utterances are padded to have
        the same length, and as a consequence this length is also the same in all histories in the data.
        data must be sorted in decreasing order of history length. The memory size for each batch is length of the history
        of the first data point (i.e. the longest) in a batch (up to max_memory_size). The padding occurs on this object
        directly, so it gets modified by this function
        :param batch_size: number of elements in a batch, unless there are not enough elements, then a batch will have the
        remaining points, with len < batch_size
        :param max_memory_size: max number of previous utterances (bot and user alike) to keep in history for a single
        data point
        :param utterance_length: length of user/bot utterances (they must have same length in any case). Short histories
        will be padded by adding uterrances made of utterance_length 0s so that every history has max_memory_size
        :return: data (modified by sorting it by decreasing length of history and adding padding so all histories in a batch
        have the same length), batch_indexes (an iterable of Tuple[start, end]), where end is not part of the current batch
        but of the next only (i.e. end_i = end_i+1 for all i except the last). Do note the end index of the last batch is
        not checked against the number of elements in the data, therefore this number can be higher. This should not be a
        problem if data is split using the data[start:end] slicing format
        """
        max_memory_size = min(max_memory_size, max(len(x['history']) for x in data))  # no point in max_mem > longest h
        batch_size = min(batch_size, len(data))
        data.sort(key=lambda x: len(x['history']), reverse=True)
        history, query, label = [], [], []
        for i, x in enumerate(data):
            h, q, l = x.values()
            if i % batch_size == 0:  # new batch. history length of this first point in the batch determines memory_size
                memory_size = max(1, min(max_memory_size, len(h)))  # memory in [1, max_memory_size]
            h = h[::-1][:memory_size][::-1]  # take only last memory_size sentences (flip, cut at mem size, flip back)
            pad_size = max(0, memory_size - len(h))  # pad h
            for _ in range(pad_size):  # empty histories will thus consist of 1 0 padded memory
                h.append([0] * utterance_length)
            history.append(h)
            query.append(q)
            label.append(l)
            # TODO you might want to do the memory padding in format_babi_data so you can easily compare vs how encode
            # featurizes. Also, as sukhbataar, you might want to keep memory of a fixed size, padding as necessary.
            # Check the other TODOs and your small_format_babi.txt and small_encode.txt to compare, the TODOs point to
            # where they are created
        batch_indexes = zip(range(0, len(data) - batch_size, batch_size), range(batch_size, len(data), batch_size))
        return history, query, label, batch_indexes

    def _format_label(self, bot_act):
        """
        Produces a 1-hot encoding of the bot target action
        :param bot_act: bot action, as a string
        :return: List[int], a 1-hot encoding of the action
        """
        bot_vec = [0] * len(self.act2id)
        bot_vec[self.act2id[bot_act]] = 1
        return bot_vec

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
        # TODO restore botsaid
        turns = [int(t / 2) for t in range(0, len(h))]  # [0, 0, 1, 1, 2, 2, .... floor((len(h)-1)/2)]
        h = [(t, ev) for t, ev in zip(turns, h)]  # adding the turn now that non-relevant events are out
        # h = [(t, ev) for t, ev in enumerate(h)]
        h = h[::-1][:memory_size*2][::-1]  # TODO restore botsaid, that *2 is because we're not keeping bot acts
        memory = []
        for t, u in h:
            if isinstance(u, ActionExecuted):
                # TODO restore botsaid
                # memory.append(self.featurize_bot_act(u.action_name, t, self.bot_padding))
                # self.featurize_bot_act(u.action_name, t, self.bot_padding)  # just to calculate context features
                pass
            elif isinstance(u, UserUttered):
                memory.append(self.featurize_user_act(u.intent['name'], u.entities, t, self.user_padding))
        query = memory.pop()  # remove the last one, since that one is query
        memory = [[0] * self.utterance_len()] if not memory else memory
        # TODO delete this crap
        # with open('small_encode.txt', 'a') as fh:
        #     fh.write(str(query) + '\n')
        #     fh.write(str(memory) + '\n')
        return query, memory

    @property
    def act2id(self):
        """
        :return: Dictionary[str, int] mapping each valid bot dialog act in the domain to a unique consecutive id from 0
        """
        raise NotImplementedError

    @property
    def intent2id(self):
        """
        :return: Dictionary[str, int] mapping each valid bot dialog act in the domain to a unique consecutive id from 0
        """
        raise NotImplementedError

    @property
    def entity2id(self):
        """
        :return: Dictionary[str, int] mapping each valid bot dialog act in the domain to a unique consecutive id from 0
        """
        raise NotImplementedError

    @staticmethod
    def _turn_to_binary(turn, bits):
        """
        Convert an integer number to a binary representation of a given number of bits. Any number higher than the max value
        representable with the given number of bits is converted to that maximum (e.g. for a maximum of 4 bits, 64 will be
        represented as 1111)
        :param turn: integer to convert
        :param bits: number of bits to use
        :return: a List with the binary conversion of turn
        """
        max_possible = int(''.join(['1'] * bits), 2)
        turn = min(max_possible, turn)
        format_string = '#0' + str(bits) + 'b'  # fill with 0, use at least bits digits, binary codification
        return list(map(lambda x: int(x), list(format(turn, format_string)[2:])))

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
                user_said = self.featurize_user_act(*self.parser.get_user_act(turn['human']), i, user_padding)
                # bot_said = self.featurize_bot_act(self.parser.get_bot_act(turn['bot']), i, bot_padding)  # just to calculate context features
                data.append({'history': copy(h), 'query': user_said,
                             'label': self._format_label(self.parser.get_bot_act(turn['bot']))})
                h.append(user_said)
                # h.append(bot_said)  TODO restore botsaid
                # TODO delete this crap
                # with open('small_format_babi.txt', 'a') as fh:
                #     fh.write(str(data[-1]['query']) + '\n')
                #     fh.write(str(data[-1]['history']) + '\n')
            self._reset()
        return data


class MemNetT5DataAdapter(MemNetDataAdapter):
    _act2id = {'greet': 0,
              'on_it': 1,
              'announce_search': 2,
              'api_call': 3,
              'suggest_restaurant': 4,
              'reserve': 5,
              'announce_keep_searching': 6,
              'request_updates': 7,
              'give_phone': 8,
              'give_address': 9,
              'ask_location': 10,
              'ask_number_of_people': 11,
              'ask_price': 12,
              'ask_cuisine': 13,
              'ask_anything_else': 14,
              'bye': 15
              }
    _entity2id = {
        'cuisine': 0,
        'location': 1,
        'number': 2,
        'price': 3
    }
    _intent2id = {
        'greet': 0,
        'inform': 1,
        'deny': 2,
        'affirm': 3,
        'request_phone': 4,
        'request_address': 5,
        'thankyou': 6,
        'bye': 7,
        'silence': 8
    }

    def __init__(self):
        parser = BabiT5Reader()
        super(MemNetT5DataAdapter, self).__init__(parser)

    def _reset(self):
        pass  # nothing to reset for task 5

    @property
    def act2id(self):
        return self._act2id

    @property
    def intent2id(self):
        return self._intent2id

    @property
    def entity2id(self):
        return self._entity2id

    def featurize_user_act(self, intent, entities, turn, padding=0):
        """
        Featurizes a user message
        :param intent: str indicating the user intent
        :param entities: iterable of entities in the user message, each one a dictionary with the name of the entity
        under key 'entity'
        :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
        :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have
        same length
        :return: a vector consisting of a 0 (to indicate this is a user message and tell it apart from bot messages)
        concatenated with an integer value indicating the turn in the conversation (using binary is tempting to avoid
        learning bias towards higher numbered turns, but perhaps this is exactly what you want to do: more recent turns
        to influence learning more), concatenated with a 1-hot vector indicating user intent concatenated with a binary
        vector of size 4 indicating which entities have a value (cuisine, location, number, price) concatenated with
        padding 0s: [0, turn, 0 ..., intent, 0 ..., location, number, price, cuisine, 0...]
        """
        entity_vec = [0] * len(self.entity2id)
        for e in entities:
            entity_vec[self.entity2id[e['entity']]] = 1
        intent_vec = [0] * len(self.intent2id)
        if intent:  # user might say literally nothing, then we keep intent vector fully off
            intent_vec[self.intent2id[intent]] = 1
        return [0] + [turn] + intent_vec + entity_vec + [0] * padding

    def featurize_bot_act(self, bot_act, turn, padding=0):
        """
        Featurizes a bot message
        :param bot_act: str indicating the bot action. Can come with or without the 'utter_' prefix
        :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
        :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have same
        length
        :return: a vector consisting of a 1 (to indicate this is a bot message and tell it apart from user messages),
        concatenated with an integer value indicating the turn in the conversation (using binary is tempting to avoid
        learning bias towards higher numbered turns, but perhaps this is exactly what you want to do: more recent turns to
        influence learning more), concatenated with a 1 hot vector indicating the bot action, concatenated with padding 0's:
        [1, turn, 0, ... action, 0..., 0...]
        """
        bot_vec = [0] * len(self.act2id)
        bot_vec[self.act2id[bot_act.replace("utter_", "")]] = 1  # just in case they include the utter_ rasa prefix
        return [1] + [turn] + bot_vec + [0] * padding

    def len_user_featurized_vec(self):
        return len(self.entity2id) + len(self.intent2id) + 2

    def len_bot_featurized_vec(self):
        return len(self.act2id) + 2

    def utterance_len(self):
        return max(self.len_bot_featurized_vec(), self.len_user_featurized_vec())


class MemNetT6DataAdapter(MemNetDataAdapter):
    _act2id = {
        'greet': 0,
        'api_call': 1,
        'offer_rest_area_price': 2,
        'offer_rest_area_food': 3,
        'offer_rest_area_food_price': 4,
        'offer_rest_area': 5,
        'offer_rest_food_price': 6,
        'offer_rest_food': 7,
        'offer_rest_price': 8,
        'offer_rest_price_postcode': 9,
        'offer_rest': 10,
        'confirm_food_dontcare': 11,
        'confirm_price': 12,
        'confirm_price_dontcare': 13,
        'confirm_area': 14,
        'confirm_area_dontcare': 15,
        'bye': 16,
        'ask_food': 17,
        'ask_area': 18,
        'ask_price': 19,
        'canthelp_food': 20,
        'canthelp_food2': 21,
        'canthelp_food_price': 22,
        'canthelp_food_area': 23,
        'canthelp_price_area': 24,
        'canthelp_food_price_area': 25,
        'canthelp_food_area2': 26,
        'canthelp_price_food': 27,
        'canthelp_food_area_price': 28,
        'repeat': 29,
        'canthear': 30,
        'confirm_food_area_ask_price': 31,
        'confirm_food_price_ask_area': 32,
        'confirm_food_price_dontcare_ask_area': 33,
        'confirm_area_food_dontcare_ask_price': 34,
        'confirm_price_area_ask_food': 35,
        'confirm_food_ask_area': 36,
        'confirm_food_area_dontcare_ask_price': 37,
        'confirm_food_ask_price': 38,
        'confirm_area_ask_food': 39,
        'confirm_price_ask_food': 40,
        'confirm_price_ask_area': 41,
        'confirm_area_dontcare_ask_price': 42,
        'confirm_food_dontcare_ask_area': 43,
        'confirm_food_dontcare_ask_price': 44,
        'confirm_area_dontcare_food_dontcare_ask_price': 45,
        'confirm_food_dontcare_price_ask_area': 46,
        'confirm_area_dontcare_ask_food': 47,
        'confirm_food': 48,
        'give_phone': 49,
        'give_phone2': 50,
        'give_postcode': 51,
        'give_address': 52,
        'give_area': 53,
        'give_address2': 54,
        'askmore': 55,
    }

    _entity2id = {
        'cuisine': 0,
        'location': 1,
        'price': 2
    }
    _intent2id = {
        'affirm': 0,
        'bye': 1,
        'dontcare': 2,
        'inform': 3,
        'negate': 4,
        'reqalts': 5,
        'request_address': 6,
        'request_food': 7,
        'request_location': 8,
        'request_phone': 9,
        'request_postcode': 10,
        'request_price': 11,
        'silence': 12
    }

    def __init__(self, nlu_model_path, kb_filename):
        """
        :param nlu_model_path: path of the persisted Rasa NLU model to parse user text
        :param kb_filename: bAbI t6 knowledge base file
        """
        parser = BabiT6Reader(nlu_model_path, babit6_kb_filename=None)
        self.db = BabiDB(kb_filename)
        self.path = nlu_model_path
        self.kb_filename = kb_filename
        self.slot_values = {'cuisine': None, 'location': None, 'price': None}
        self.cuisine_types = []
        with open(self.kb_filename) as kb_fh:
            for line in kb_fh:
                match = re.search('R_cuisine (?P<value>\w+)', line)
                if match:
                    self.cuisine_types.append(match.group('value'))
        self.cuisine_types = list(set(self.cuisine_types))

        # context feature flags
        self.pending_results = None
        self.num_reqalts = None
        self.context_features = None
        self._reset()

        super(MemNetT6DataAdapter, self).__init__(parser)

    def _reset(self):
        """
        Sets the context features to the right initial values. Should be call if starting to featurize a new
        conversation
        """
        self.slot_values = {'cuisine': None, 'location': None, 'price': None}
        self.pending_results = self.db.num_results()
        self.num_reqalts = 0
        # self.context_features = {'db_queried': 0, 'empty_results': 0, 'non-empty_results': 1, 'results_offered': 0,
        #                          'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}
        # TODO restore botsaid
        self.context_features = {'empty_results': 0, 'non-empty_results': 1,
                                 'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}

    @property
    def act2id(self):
        return self._act2id

    @property
    def intent2id(self):
        return self._intent2id

    @property
    def entity2id(self):
        return self._entity2id

    def _context_features(self):
        return [v for v in self.context_features.values()]

    def featurize_user_act(self, intent, entities, turn, padding=0):
        """
        Featurizes a user message
        :param intent: str indicating the user intent
        :param entities: iterable of entities in the user message, each one a dictionary with the name of the entity
        under key 'entity'
        :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
        :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have
        same length
        :return: a vector consisting of a 0 (to indicate this is a user message and tell it apart from bot messages)
        concatenated with an integer value indicating the turn in the conversation (using binary is tempting to avoid
        learning bias towards higher numbered turns, but perhaps this is exactly what you want to do: more recent turns
        to influence learning more), concatenated with a 1-hot vector indicating user intent concatenated with a binary
        vector of size 3 indicating which entities have a value (cuisine, location, price) concatenated with
        padding 0s: [0, turn, 0 ..., intent, 0 ..., location, number, price, cuisine, 0...]
        """
        entity_vec = [0] * len(self.entity2id)
        for e in entities:
            entity_vec[self.entity2id[e['entity']]] = 1
            self.slot_values[e['entity']] = e['value']  # keep track of currently filled slots
        num_results = self.db.num_results(**{k: v for k, v in self.slot_values.items() if v})
        self.context_features['empty_results'] = 1 if num_results == 0 else 0
        self.context_features['non-empty_results'] = 1 - self.context_features['empty_results']
        if entities:  # providing new entitites means new query, so pending results is reset
            self.pending_results = num_results
            self.num_reqalts = 0
        if self.slot_values['cuisine']:
            self.context_features['unknown_cuisine'] = 1 if self.slot_values['cuisine'] not in self.cuisine_types else 0

        intent_vec = [0] * len(self.intent2id)
        if intent == 'reqalts':
            self.num_reqalts += 1
            self.context_features['results_exhausted'] = 1 if self.num_reqalts + 1 == self.pending_results else 0
            self.context_features['results_available'] = 1 - self.context_features['results_exhausted']
        if intent:  # user might say literally nothing, then we keep intent vector fully off
            intent_vec[self.intent2id[intent]] = 1
        return [turn] + intent_vec + entity_vec + self._context_features()

    def featurize_bot_act(self, bot_act, turn, padding=0):
        """
        Featurizes a bot message
        :param bot_act: str indicating the bot action. Can come with or without the 'utter_' prefix
        :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
        :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have same
        length
        :return: a vector consisting of a 1 (to indicate this is a bot message and tell it apart from user messages),
        concatenated with an integer value indicating the turn in the conversation (using binary is tempting to avoid
        learning bias towards higher numbered turns, but perhaps this is exactly what you want to do: more recent turns to
        influence learning more), concatenated with a 1 hot vector indicating the bot action, concatenated with padding 0's:
        [1, turn, 0, ... action, 0..., 0...]
        """
        bot_vec = [0] * len(self.act2id)
        bot_vec[self.act2id[bot_act.replace("utter_", "")]] = 1  # just in case they include the utter_ rasa prefix

        # if bot_act.replace("utter_", "") == 'api_call':
        #     self.context_features['db_queried'] = 1
        # if bot_act.replace("utter_", "")[:5] == 'offer':
        #     self.context_features['results_offered'] = 1
        #     self.pending_results -= 1
        #     self.context_features['results_exhausted'] = 1 if self.pending_results == 0 else 1
        #     self.context_features['results_available'] = 1 - self.context_features['results_exhausted']

        return [turn] + bot_vec

    def len_user_featurized_vec(self):
        return len(self.intent2id) + len(self.entity2id) + len(self.context_features) + 1

    def len_bot_featurized_vec(self):
        return len(self.act2id) + 1  # 2 bits for sender flag + int for turn

    def utterance_len(self):
        return self.len_user_featurized_vec()
