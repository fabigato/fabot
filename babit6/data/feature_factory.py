from data.database import BabiDB
from data.babi_reader import BabiT6Reader, BabiT5Reader
from numpy import mean
from globals import BABI_T6_KB_FILE, W2VEC_MODEL_PATH, NLU_T6_MODEL_PATH, BABI_T5_KB_FILE, NLU_T5_MODEL_PATH, \
    BABI_T5_KB_OOV_FILE
import gensim
from rasa_core.interpreter import RasaNLUInterpreter


class T6Featurizer(object):
    """
    Produces features for the bAbI task 6
    """

    def __init__(self, use_bow=True, use_turn=True, use_bot_utter=True, use_embeddings=True, use_intent=False,
                 use_nlu_entity_extractor=False, use_entities=True, use_context=True):
        """
        :param use_bow: if True, BoW features will be used
        :param use_turn: if True, conversation turn will be added to the features
        :param use_bot_utter: if True, the featurized previous bot utterance will be added to the features
        :param use_embeddings: if True, word embedding features will be added
        :param use_intent: if True, use Rasa NLU to classify user utterances by intent and add that to the features
        :param use_nlu_entity_extractor: if True, the Rasa NLU model saved at this location will be used to extract
        entities. Else, simple pattern match will be used to detect entities
        :param use_entities: if True, use a binary feature vector for entities mentioned in the current utterance
        :param use_context: use the context features from Williams (this includes entities currently set in the
        conversation state, which is different from just having the entities in the current utterance, which you get
        by setting use_entities=True)
        """
        self._use_bow = use_bow
        self._use_turn = use_turn
        self._use_bot_utter = use_bot_utter
        self._use_embeddings = use_embeddings
        self._use_intent = use_intent
        self._use_nlu_entity_extractor = use_nlu_entity_extractor
        self._use_entities = use_entities
        self._use_context = use_context

        if use_embeddings:
            self.w2vec_model = gensim.models.KeyedVectors.load_word2vec_format(W2VEC_MODEL_PATH, binary=True)
        if use_nlu_entity_extractor or use_intent:
            self.nlu = RasaNLUInterpreter(NLU_T6_MODEL_PATH)
        if use_context:  # should be set independently of bot_features being used
            self.context = {'empty_results': 0, 'non-empty_results': 1, 'results_offered': 0,
                            'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}
            self.db = BabiDB(BABI_T6_KB_FILE, task=6)
            self.num_results = self.db.num_results()
            self.num_offered = 0
        # slot_values keep current entity values at every point in a conversation
        self.slot_values = {e: None for e in BabiT6Reader.entity2id}

    def reset(self):
        """
        Sets the context features to the right initial values. Should be called if starting to featurize a new
        conversation
        """
        if self._use_context:
            self.context = {'empty_results': 0, 'non-empty_results': 1, 'results_offered': 0,
                            'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}
            self.slot_values = self.slot_values = {e: None for e in BabiT6Reader.entity2id}
            self.num_results = self.db.num_results()
            self.num_offered = 0

    @staticmethod
    def get_bot_act(text):
        """
        Extracts the dialog act of a given bot utterance
        :param text: bot utterance
        :return: bot dialog act as str, or None if no matching act found
        """
        for da, (pattern, _) in BabiT6Reader.das.items():
            if pattern.match(text):
                return da
        return None

    def extract_entities(self, user_text):
        """
        extracts entities from a user text, either using Rasa NLU or simple pattern matching, see class constructor
        :param user_text: text to extract entities from
        :param nlu: RasaNLUINterpreter object. If provided, it will be used to get the entities. Else, simple pattern
        matching will be used
        :return: dictionary with extracted entities
        """
        if self._use_nlu_entity_extractor:  # use rasa nlu
            parse_data = self.nlu.parse(user_text)
            return {e['entity']: e['value'] for e in parse_data['entities']}
        else:  # use simple pattern matching
            entities = {}
            for word in user_text.strip().lower().split():
                if word in BabiT6Reader.cuisine_types:
                    entities['cuisine'] = word
                elif word in BabiT6Reader.prices:
                    entities['price'] = word
                elif word in BabiT6Reader.locations:
                    entities['location'] = word
                else:
                    for value, synonyms in BabiT6Reader.prices_syns.items():
                        if word in synonyms:
                            entities['price'] = value  # we save the canonical value, not the synonym
                            break
                    for value, synonyms in BabiT6Reader.location_syns.items():
                        if word in synonyms:
                            entities['location'] = value
                            break
            return entities

    def entity_features(self, entities):
        """Produces features to track entities mentioned in current utterance, not in the converstion state. For those
        use context features instead
        :param entities: dictionary of entities to featurize"""
        entity_vec = [0] * len(BabiT6Reader.entity2id)
        for entity in entities:
            entity_vec[BabiT6Reader.entity2id[entity]] = 1
        return entity_vec

    def context_features(self, prev_bot_text):
        entities = [0] * len(BabiT6Reader.entity2id)  # not entities in current utterance, but in the conversation state
        for entity in self.slot_values:
            if self.slot_values[entity]:
                entities[BabiT6Reader.entity2id[entity]] = 1
        bot_act = T6Featurizer.get_bot_act(prev_bot_text)

        self.num_results = self.db.num_results(**{e: v for e, v in self.slot_values.items() if v})
        self.context['unknown_cuisine'] = 1 \
            if self.slot_values['cuisine'] and self.slot_values['cuisine'] not in BabiT6Reader.cuisine_types else 0
        if bot_act in ['offer_rest_area_price', 'offer_rest_area_food', 'offer_rest_area_food_price', 'offer_rest_area',
                       'offer_rest_food_price', 'offer_rest_food', 'offer_rest_price', 'offer_rest']:
            self.context['results_offered'] = 1
            self.num_offered += 1
            self.context['results_exhausted'] = 1 if self.num_offered >= self.num_results else 0
            self.context['results_available'] = 1 if self.num_offered < self.num_results else 0

        if bot_act == 'api_call':
            self.context['results_offered'] = 0
            self.num_offered = 0
        self.context['empty_results'] = 1 if self.num_results == 0 else 0
        self.context['non-empty_results'] = 1 if self.num_results > 0 else 0

        return [v for v in self.context.values()] + entities

    @staticmethod
    def bot_features(bot_text):
        bot_act = T6Featurizer.get_bot_act(bot_text)
        bot_vec = [0] * len(BabiT6Reader.das)
        if bot_act:
            bot_vec[BabiT6Reader.act2id[bot_act]] = 1
        return bot_vec

    def slots(self):
        return {e: v if v else 'R_' + e for e, v in self.slot_values.items()}

    def embedding_features(self, text):
        embs = [self.w2vec_model[word] for word in text.split(' ') if word and word in self.w2vec_model]
        # average of embeddings
        if len(embs):
            return list(mean(embs, axis=0))
        else:
            return [0] * self.w2vec_model.vector_size

    @staticmethod
    def num_actions():
        return len(BabiT6Reader.das)

    @staticmethod
    def bow_features(text):
        bow = [0] * len(BabiT6Reader.w2id)
        for word in text.split():
            if word in BabiT6Reader.w2id:
                bow[BabiT6Reader.w2id[word]] = 1
        return bow

    @staticmethod
    def intent_features(intent_act):
        intent = [0] * len(BabiT6Reader.intents)
        if intent_act:
            intent[BabiT6Reader.intents[intent_act]] = 1
        return intent

    def featurize(self, user_text, prev_bot_text=None, turn=None):
        """
        Featurizes a data point
        :param user_text: user text
        :param prev_bot_text: bot text of previous turn. If use_bot_utter or use_context were set to True at
        constructor, this argument should be provided
        :param turn: conversation turn corresponding to the data point. If use_turn was set to True at constructor, this
        argument should be provided
        :return: List of features
        """
        entities = self.extract_entities(user_text)
        for e, v in entities.items():
            self.slot_values[e] = v

        turn = [turn] if self._use_turn else []
        intent = self.intent_features(self.nlu.parse(user_text)['intent']['name']) if self._use_intent else []
        bot = T6Featurizer.bot_features(prev_bot_text) if self._use_bot_utter else []
        entities = self.entity_features(entities) if self._use_entities else []
        bow = T6Featurizer.bow_features(user_text) if self._use_bow else []
        embeddings = self.embedding_features(user_text) if self._use_embeddings else []
        context = self.context_features(prev_bot_text) if self._use_context else []
        return turn + intent + bot + entities + bow + embeddings + context

    def feature_len(self):
        turn = 1 if self._use_turn else 0
        intent = len(BabiT6Reader.intents) if self._use_intent else 0
        bot = len(BabiT6Reader.das) if self._use_bot_utter else 0
        entities = len(self.slot_values) if self._use_entities else 0
        bow = len(BabiT6Reader.w2id) if self._use_bow else 0
        embeddings = self.w2vec_model.vector_size if self._use_embeddings else 0
        context = len(self.context) + len(self.slot_values) if self._use_context else 0
        return turn + intent + bot + entities + bow + embeddings + context

    def get_bot_utterance_act_id(self, bot_text):
        bot_act = self.get_bot_act(bot_text)
        assert bot_act or not bot_text
        return BabiT6Reader.act2id[bot_act]

    @staticmethod
    def id2act(actid):
        return BabiT6Reader.id2act[actid]

    @staticmethod
    def act2pattern(bot_act):
        return BabiT6Reader.das[bot_act]


class T5Featurizer(object):
    """
    Produces features for the bAbI task 5
    """

    def __init__(self, use_bow=True, use_turn=True, use_bot_utter=True, use_embeddings=True, use_intent=False,
                 use_nlu_entity_extractor=False, use_entities=True, use_context=True, use_oov=False):
        """
        :param use_bow: if True, BoW features will be used
        :param use_turn: if True, conversation turn will be added to the features
        :param use_bot_utter: if True, the featurized previous bot utterance will be added to the features
        :param use_embeddings: if True, word embedding features will be added
        :param use_intent: if True, use Rasa NLU to classify user utterances by intent and add that to the features
        :param use_nlu_entity_extractor: if True, the Rasa NLU model saved at this location will be used to extract
        entities. Else, simple pattern match will be used to detect entities
        :param use_entities: if True, use a binary feature vector for entities mentioned in the current utterance
        :param use_context: use the context features from Williams (this includes entities currently set in the
        conversation state, which is different from just having the entities in the current utterance, which you get
        by setting use_entities=True)
        """
        self._use_bow = use_bow
        self._use_turn = use_turn
        self._use_bot_utter = use_bot_utter
        self._use_embeddings = use_embeddings
        self._use_intent = use_intent
        self._use_nlu_entity_extractor = use_nlu_entity_extractor
        self._use_entities = use_entities
        self._use_context = use_context

        self.db = BabiDB(BABI_T5_KB_FILE if not use_oov else BABI_T5_KB_OOV_FILE, task=5)
        self.current_rests = None
        self.current_rest_idx = 0

        if use_embeddings:
            self.w2vec_model = gensim.models.KeyedVectors.load_word2vec_format(W2VEC_MODEL_PATH, binary=True)
        if use_nlu_entity_extractor or use_intent:
            self.nlu = RasaNLUInterpreter(NLU_T5_MODEL_PATH)
        if use_context:  # should be set independently of bot_features being used
            self.context = {'empty_results': 0, 'non-empty_results': 1, 'results_offered': 0,
                            'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}
            self.num_results = self.db.num_results()
            self.num_offered = 0
        # slot_values keep current entity values at every point in a conversation
        self.slot_values = {e: None for e in BabiT5Reader.entity2id}

    def reset(self):
        """
        Sets the context features to the right initial values. Should be called if starting to featurize a new
        conversation
        """
        if self._use_context:
            self.context = {'empty_results': 0, 'non-empty_results': 1, 'results_offered': 0,
                            'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}
            self.slot_values = self.slot_values = {e: None for e in BabiT5Reader.entity2id}
            self.num_results = self.db.num_results()
            self.num_offered = 0

    @staticmethod
    def get_bot_act(text):
        """
        Extracts the dialog act of a given bot utterance
        :param text: bot utterance
        :return: bot dialog act as str, or None if no matching act found
        """
        for da, (pattern, _) in BabiT5Reader.bot_das_.items():
            if pattern.match(text):
                return da
        return None

    def extract_entities(self, user_text):
        """
        extracts entities from a user text, either using Rasa NLU or simple pattern matching, see class constructor
        :param user_text: text to extract entities from
        :param nlu: RasaNLUINterpreter object. If provided, it will be used to get the entities. Else, simple pattern
        matching will be used
        :return: dictionary with extracted entities
        """
        if self._use_nlu_entity_extractor:  # use rasa nlu
            parse_data = self.nlu.parse(user_text)
            return {e['entity']: e['value'] for e in parse_data['entities']}
        else:  # use simple pattern matching
            entities = {}
            for word in user_text.strip().lower().split():
                if word in BabiT5Reader.cuisine_types:
                    entities['cuisine'] = word
                elif word in BabiT5Reader.prices:
                    entities['price'] = word
                elif word in BabiT5Reader.locations:
                    entities['location'] = word
                elif word in BabiT5Reader.numbers:
                    entities['number'] = word
            return entities

    def entity_features(self, entities):
        """Produces features to track entities mentioned in current utterance, not in the converstion state. For those
        use context features instead
        :param entities: dictionary of entities to featurize"""
        entity_vec = [0] * len(BabiT5Reader.entity2id)
        for entity in entities:
            entity_vec[BabiT5Reader.entity2id[entity]] = 1
        return entity_vec

    def context_features(self, prev_bot_text):
        entities = [0] * len(BabiT5Reader.entity2id)  # not entities in current utterance, but in the conversation state
        for entity in self.slot_values:
            if self.slot_values[entity]:
                entities[BabiT5Reader.entity2id[entity]] = 1
        bot_act = T5Featurizer.get_bot_act(prev_bot_text)

        self.num_results = self.db.num_results(**{e: v for e, v in self.slot_values.items() if v})
        self.context['unknown_cuisine'] = 1 \
            if self.slot_values['cuisine'] and self.slot_values['cuisine'] not in BabiT5Reader.cuisine_types else 0
        if bot_act in ['offer_rest_area_price', 'offer_rest_area_food', 'offer_rest_area_food_price', 'offer_rest_area',
                       'offer_rest_food_price', 'offer_rest_food', 'offer_rest_price', 'offer_rest']:
            self.context['results_offered'] = 1
            self.num_offered += 1
            self.context['results_exhausted'] = 1 if self.num_offered >= self.num_results else 0
            self.context['results_available'] = 1 if self.num_offered < self.num_results else 0

        if bot_act == 'api_call':
            self.context['results_offered'] = 0
            self.num_offered = 0
        self.context['empty_results'] = 1 if self.num_results == 0 else 0
        self.context['non-empty_results'] = 1 if self.num_results > 0 else 0

        return [v for v in self.context.values()] + entities

    def update_current_rest(self, prev_bot_text):
        bot_act = T5Featurizer.get_bot_act(prev_bot_text)
        if bot_act == 'api_call':
            self.current_rests = self.db.find_restaurant(**{k: v for k, v in self.slot_values.items() if v})
            self.current_rest_idx = 0
        if bot_act == 'announce_keep_searching':
            self.current_rest_idx += 1  # in t5 users never exhaust available options

    @staticmethod
    def bot_features(bot_text):
        bot_act = T5Featurizer.get_bot_act(bot_text)
        bot_vec = [0] * len(BabiT5Reader.bot_das_)
        if bot_act:
            bot_vec[BabiT5Reader.act2id[bot_act]] = 1
        return bot_vec

    def slots(self):
        converted_slots = {e: v if v else 'R_' + e for e, v in self.slot_values.items()}
        # try:
        rest = self.current_rests.iloc[self.current_rest_idx][['name', 'phone', 'address']].to_dict() \
            if self.current_rests is not None and not self.current_rests.empty and \
               self.current_rest_idx < len(self.current_rests) else {'name': None, 'phone': None,
                                                                     'address': None}
        # except IndexError:
        #     print('time to backtrack')
        return {**converted_slots, **rest}

    def embedding_features(self, text):
        embs = [self.w2vec_model[word] for word in text.split(' ') if word and word in self.w2vec_model]
        # average of embeddings
        if len(embs):
            return list(mean(embs, axis=0))
        else:
            return [0] * self.w2vec_model.vector_size

    @staticmethod
    def num_actions():
        return len(BabiT5Reader.bot_das_)

    @staticmethod
    def bow_features(text):
        bow = [0] * len(BabiT5Reader.w2id)
        for word in text.split():
            if word in BabiT5Reader.w2id:
                bow[BabiT5Reader.w2id[word]] = 1
        return bow

    @staticmethod
    def intent_features(intent_act):
        intent = [0] * len(BabiT5Reader.intents)
        if intent_act:
            intent[BabiT5Reader.intents[intent_act]] = 1
        return intent

    def featurize(self, user_text, prev_bot_text=None, turn=None):
        """
        Featurizes a data point
        :param user_text: user text
        :param prev_bot_text: bot text of previous turn. If use_bot_utter or use_context were set to True at
        constructor, this argument should be provided
        :param turn: conversation turn corresponding to the data point. If use_turn was set to True at constructor, this
        argument should be provided
        :return: List of features
        """
        self.update_current_rest(prev_bot_text)
        entities = self.extract_entities(user_text)
        for e, v in entities.items():
            self.slot_values[e] = v
        turn = [turn] if self._use_turn else []
        intent = self.intent_features(self.nlu.parse(user_text)['intent']['name']) if self._use_intent else []
        bot = T5Featurizer.bot_features(prev_bot_text) if self._use_bot_utter else []
        entities = self.entity_features(entities) if self._use_entities else []
        bow = T5Featurizer.bow_features(user_text) if self._use_bow else []
        embeddings = self.embedding_features(user_text) if self._use_embeddings else []
        context = self.context_features(prev_bot_text) if self._use_context else []
        return turn + intent + bot + entities + bow + embeddings + context

    def feature_len(self):
        turn = 1 if self._use_turn else 0
        intent = len(BabiT5Reader.intents) if self._use_intent else 0
        bot = len(BabiT5Reader.bot_das_) if self._use_bot_utter else 0
        entities = len(self.slot_values) if self._use_entities else 0
        bow = len(BabiT5Reader.w2id) if self._use_bow else 0
        embeddings = self.w2vec_model.vector_size if self._use_embeddings else 0
        context = len(self.context) + len(self.slot_values) if self._use_context else 0
        return turn + intent + bot + entities + bow + embeddings + context

    def get_bot_utterance_act_id(self, bot_text):
        bot_act = self.get_bot_act(bot_text)
        assert bot_act or not bot_text
        return BabiT5Reader.act2id[bot_act]

    @staticmethod
    def id2act(actid):
        return BabiT5Reader.id2act[actid]

    @staticmethod
    def act2pattern(bot_act):
        return BabiT5Reader.bot_das_[bot_act]
