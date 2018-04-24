from data.babi_reader import babi_dialogue_iterator, get_user_act, get_bot_act
from copy import copy

act2id = {'greet': 0,
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
entity2id = {
    'cuisine': 0,
    'location': 1,
    'number': 2,
    'price': 3
}
intent2id = {
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


def featurize_bot_act(bot_act, turn, padding=0):
    """
    Featurizes a bot message
    :param bot_act: str indicating the bot action
    :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
    :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have same
    length
    :return: a vector consisting of a 1 (to indicate this is a bot message and tell it apart from user messages),
    concatenated with an integer value indicating the turn in the conversation (using binary is tempting to avoid
    learning bias towards higher numbered turns, but perhaps this is exactly what you want to do: more recent turns to
    influence learning more), concatenated with a 1 hot vector indicating the bot action, concatenated with padding 0's:
    [1, turn, 0, ... action, 0..., 0...]
    """
    bot_vec = [0] * len(act2id)
    bot_vec[act2id[bot_act.replace("utter_", "")]] = 1  # just in case they include the utter_ rasa prefix
    return [1] + [turn] + bot_vec + [0] * padding


def featurize_user_act(intent, entities, turn, padding=0):
    """
    Featurizes a user message
    :param intent: str indicating the user intent
    :param entities: iterable of entities in the user message, each one a dictionary with the name of the entity under
    key 'entity'
    :param turn: turn of the utterance in the conversation, int. This feature is used by Bordes
    :param padding: number of 0s to add at the end of the vector, to enforce user messages and bot messages have same
    length
    :return: a vector consisting of a 0 (to indicate this is a user message and tell it apart from bot messages)
    concatenated with an integer value indicating the turn in the conversation (using binary is tempting to avoid
    learning bias towards higher numbered turns, but perhaps this is exactly what you want to do: more recent turns to
    influence learning more), concatenated with a 1-hot vector
    indicating user intent concatenated with a binary vector of size 4 indicating which entities have a value (cuisine,
    location, number, price) concatenated with padding 0s:
    [0, turn, 0 ..., intent, 0 ..., location, number, price, cuisine, 0...]
    """
    entity_vec = [0] * len(entity2id)
    for e in entities:
        entity_vec[entity2id[e['entity']]] = 1
    intent_vec = [0] * len(intent2id)
    intent_vec[intent2id[intent]] = 1
    return [0] + [turn] + intent_vec + entity_vec + [0] * padding


def featurize_query(intent, entities):
    """
    produces a vector of features representing the query in the MemNet
    :param intent: user intent, as a string
    :param entities: List of entities in the user utterance. Each entity represented as a Dictionary with at least a
    'entity' key with the name of the entity as value
    :return: List[int] representing the featurized user utterance. It is a 1-hot encoding of the user intent
    concatenated with the entities mentioned in the utterance (i.e. a 4-dimensional binary vector, bits representing
    cuisine, location, number and price)
    """
    entity_vec = [0] * len(entity2id)
    for e in entities:
        entity_vec[entity2id[e['entity']]] = 1
    intent_vec = [0] * len(intent2id)
    intent_vec[intent2id[intent]] = 1
    return intent_vec + entity_vec + [0]


def _format_label(bot_act):
    """
    Produces a 1-hot encoding of the bot target action
    :param bot_act: bot action, as a string
    :return: List[int], a 1-hot encoding of the action
    """
    bot_vec = [0] * len(act2id)
    bot_vec[act2id[bot_act]] = 1
    return bot_vec


def len_user_featurized_vec():
    return len(entity2id) + len(intent2id) + 2


def len_bot_featurized_vec():
    return len(act2id) + 2


def query_len():
    return len(entity2id) + len(intent2id) + 1


def format_babi_data(filename):
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
    bot_padding = max(0, len_user_featurized_vec() - len_bot_featurized_vec())
    user_padding = max(0, len_bot_featurized_vec() - len_user_featurized_vec())
    for story in babi_dialogue_iterator(filename):
        h = []
        for i, turn in enumerate(story):
            bot_said = featurize_bot_act(get_bot_act(turn['bot']), i, bot_padding)
            user_said = featurize_user_act(*get_user_act(turn['human']), i, user_padding)
            data.append({'history': copy(h), 'query': featurize_query(*get_user_act(turn['human'])),
                         'label': _format_label(get_bot_act(turn['bot']))})
            h.append(user_said)
            h.append(bot_said)
    return data


def utterance_len():
    return max(len_bot_featurized_vec(), len_user_featurized_vec())


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
        h = h[::-1][:memory_size][::-1]  # take only the last memory_size sentences (flip, cut at mem size, flip back)
        pad_size = max(0, memory_size - len(h))  # pad h
        for _ in range(pad_size):
            h.append([0] * utterance_length)
        history.append(h)
        query.append(q)
        label.append(l)
        #data[i]['history'] = h
    batch_indexes = zip(range(0, len(data) - batch_size, batch_size), range(batch_size, len(data), batch_size))
    return history, query, label, batch_indexes
