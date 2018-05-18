from data.database import BabiDB
from data.babi_reader import BabiT6Reader
from numpy import mean
from globals import BABI_T6_KB_FILE, W2VEC_MODEL_PATH, NLU_T6_MODEL_PATH
import gensim
from rasa_core.interpreter import RasaNLUInterpreter


class T6Featurizer(object):
    """
    Produces features for the bAbI task 6
    """

    def __init__(self, use_bow=True, use_turn=True, use_bot_utter=True, use_embeddings=True, use_intent=False,
                 use_nlu_entity_extractor=False, use_context=True):
        """
        :param use_bow: if True, BoW features will be used
        :param use_turn: if True, conversation turn will be added to the features
        :param use_bot_utter: if True, the featurized previous bot utterance will be added to the features
        :param use_embeddings: if True, word embedding features will be added
        :param use_intent: if True, use Rasa NLU to classify user utterances by intent and add that to the features
        :param use_nlu_entity_extractor: if True, the Rasa NLU model saved at this location will be used to extract
        entities. Else, simple pattern match will be used to detect entities
        :param use_context: use the context features from Williams
        """
        self._use_bow = use_bow
        self._use_turn = use_turn
        self._use_bot_utter = use_bot_utter
        self._use_embeddings = use_embeddings
        self._use_intent = use_intent
        self._use_nlu_entity_extractor = use_nlu_entity_extractor
        self._use_context = use_context

        if use_embeddings:
            self.w2vec_model = gensim.models.KeyedVectors.load_word2vec_format(W2VEC_MODEL_PATH, binary=True)
        if use_nlu_entity_extractor or use_intent:
            self.nlu = RasaNLUInterpreter(NLU_T6_MODEL_PATH)
        if use_context:  # should be set independently of bot_features being used
            self.context = {'empty_results': 0, 'non-empty_results': 1, 'results_offered': 0,
                            'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}
            self.db = BabiDB(BABI_T6_KB_FILE)
            self.pending_results = self.db.num_results()
        # slot_values keep current entity values at every point in a conversation
        self.slot_values = {e: None for e in BabiT6Reader.entity2id}

    def reset(self):
        """
        Sets the context features to the right initial values. Should be called if starting to featurize a new
        conversation
        """
        self.context = {'empty_results': 0, 'non-empty_results': 1, 'results_offered': 0,
                        'results_exhausted': 0, 'results_available': 1, 'unknown_cuisine': 0}
        self.slot_values = self.slot_values = {e: None for e in BabiT6Reader.entity2id}
        self.pending_results = self.db.num_results()

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
            return {e['name']: e['value'] for e in parse_data.entites}
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
                    for value, synonyms in BabiT6Reader.prices_syns.values():
                        if word in synonyms:
                            entities['price'] = word
                            break
                    for value, synonyms in BabiT6Reader.location_syns.values():
                        if word in synonyms:
                            entities['location'] = word
                            break
            return entities

    def context_features(self):
        entities = [0] * len(BabiT6Reader.entity2id)
        for entity in self.slot_values:
            if self.slot_values[entity]:
                entities[BabiT6Reader.entity2id[entity]] = 1
        return [v for v in self.context.values()] + entities

    @staticmethod
    def bot_features(bot_act):
        bot_vec = [0] * len(BabiT6Reader.bot_das)
        if bot_act:
            bot_vec[BabiT6Reader.act2id[bot_act]] = 1
        return bot_vec

    def embedding_features(self, text):
        embs = [self.w2vec_model[word] for word in text.split(' ') if word and word in self.w2vec_model]
        # average of embeddings
        if len(embs):
            return list(mean(embs, axis=0))
        else:
            return [0] * self.w2vec_model.vector_size

    @staticmethod
    def bow_features(text):
        bow = [0] * len(BabiT6Reader.w2id)
        for word in text.split():
            if word in BabiT6Reader.w2id:
                bow[BabiT6Reader.w2id[word]] = 1
        return bow

    def featurize(self, user_text, prev_bot_text=None, turn=None):
        """
        Featurizes a data point
        :param user_text: user text
        :param prev_bot_text: bot text of previous turn. If use_bot_utter was set to True at constructor, this argument
        should be provided
        :param turn: conversation turn corresponding to the data point. If use_turn was set to True at constructor, this
        argument should be provided
        :return: List of features
        """
        pass # jeje
        # prev_bot_act_feats = t6_featurize_bot_act(prev_bot_text) if prev_bot_text else []
        # turn_feat = [turn] if turn else []
        # bow_feats = bow_features(user_text, vocab) if vocab else []
        #
        # self.extract_entities(user_text)
        #
        # bow = # TODO dammit

    def feature_len(self):
        turn = 1 if self._use_turn else 0
        intent = len(BabiT6Reader.intents) if self._use_intent else 0
        bow = len(BabiT6Reader.w2id) if self._use_bow else 0
        embeddings = self.w2vec_model.vector_size if self._use_embeddings else 0
        context = len(self.context) + len(self.slot_values) if self._use_context else 0
        bot = len(BabiT6Reader.das) if self._use_bot_utter else 0
        return turn + intent + bow + embeddings + context + bot
    # def bot_features(self, bot_text):
    #     """
    #     Featurizes a bot message
    #     :param bot_act: str indicating the bot action. Can come with or without the 'utter_' prefix
    #     :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
    #     :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have
    #     same length
    #     :return: a vector consisting of a 1 (to indicate this is a bot message and tell it apart from user messages),
    #     concatenated with an integer value indicating the turn in the conversation (using binary is tempting to avoid
    #     learning bias towards higher numbered turns, but perhaps this is exactly what you want to do: more recent turns to
    #     influence learning more), concatenated with a 1 hot vector indicating the bot action, concatenated with padding 0's:
    #     [1, turn, 0, ... action, 0..., 0...]
    #     """
    #     bot_vec = [0] * len(t6_act2id)
    #     bot_vec[self.act2id[bot_act.replace("utter_", "")]] = 1  # just in case they include the utter_ rasa prefix
    #     _bot_act = bot_act.replace("utter_", "")
    #     if _bot_act == 'api_call':
    #         self.context_features['db_queried'] = 1
    #     if _bot_act[:5] == 'offer':
    #         self.context_features['results_offered'] = 1
    #         self.pending_results -= 1
    #         self.context_features['results_exhausted'] = 1 if self.pending_results == 0 else 1
    #         self.context_features['results_available'] = 1 - self.context_features['results_exhausted']
    #
    #     return [turn] + bot_vec + [0] * padding
