from globals import NLU_MODEL_PATH, NLU_T6_MODEL_NAME, BABI_T6_KB_FILE, BABI_T6_TST_FILE, BABI_T5_TRN_FILE, \
    BABI_T6_TRN_FILE, BABI_T5_TST_FILE, DSTC2_DATA_PATH, DSTCT2_TRN_LIST_FILE, DSTC2_ONTOLOGY_FILE, \
    DSTCT2_TST_LIST_FILE, BABI_T6_DEV_FILE
from data.babi_reader import BabiReader, BabiT6Reader, BabiT5Reader
from data import dstc2_reader
from os.path import join
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import entropy
import re
import json
from itertools import chain, product
from collections import defaultdict, Counter
import logging
from copy import copy

logger = logging.getLogger(__name__)

values = {'cuisine': [], 'location': [], 'price': []}
with open(DSTC2_ONTOLOGY_FILE) as kb_fh:
    values = json.load(kb_fh)['informable']
new_names = {'food': 'cuisine', 'area': 'location', 'pricerange': 'price'}
del values['name']
for slot in new_names:
    values[new_names[slot]] = values.pop(slot)
# food values not in the kb, but asked by users on train data (only if the bot detected it as food type)
values['cuisine'] += ['canapes', 'kosher', 'creative', 'caribbean', 'tuscan', 'traditional', 'austrian',
                      'swedish', 'christmas', 'australian', 'cantonese', 'irish', 'welsh', 'polynesian',
                      'romanian', 'german', 'greek', 'afghan', 'moroccan', 'belgian', 'hungarian', 'unusual',
                      'halal', 'english', 'swiss', 'world', 'vegetarian']
# remove duplicates
for slot in values:
    values[slot] = list(set(values[slot]))
# add synonyms for each value of each entity
synonyms = {slot: {value: [] for value in values[slot]} for slot in values}
synonyms['location']['centre'] = ['center']
synonyms['cuisine']['north_american'] = ['american']
synonyms['price']['moderate'] = ['moderately']


def get_freqs(task=6, trn=True):
    from collections import Counter
    counter = []
    if task == 6:
        reader = BabiT6Reader(join(NLU_MODEL_PATH, NLU_T6_MODEL_NAME), BABI_T6_KB_FILE)
        file = BABI_T6_TRN_FILE if trn else BABI_T6_TST_FILE
    else:
        reader = BabiT5Reader()
        file = BABI_T5_TRN_FILE if trn else BABI_T5_TST_FILE
    for i, story in enumerate(BabiReader.babi_dialogue_iterator(file)):
        for t, turn in enumerate(story):
            counter.append(reader.get_bot_act(turn['bot']))
    counter = Counter(counter)
    # labels, values = zip(*counter.items())
    # return labels, values
    return counter


def display_babi_bot_freqs():
    # labels, values_t6_tst = get_freqs(task=6, trn=False)
    # _, values_t6_trn = get_freqs(task=6, trn=True)
    counter_t6_tst = get_freqs(task=5, trn=False)
    counter_t6_trn = get_freqs(task=5, trn=True)
    labels = list(set(counter_t6_trn.keys()) | set(counter_t6_tst.keys()))
    values_t6_tst = [counter_t6_tst[l] for l in labels]
    values_t6_trn = [counter_t6_trn[l] for l in labels]
    values_t6_trn = np.array(values_t6_trn) / sum(values_t6_trn)
    values_t6_tst = np.array(values_t6_tst) / sum(values_t6_tst)
    print('kl divergence: {}'.format(entropy(values_t6_trn, values_t6_tst, base=2)))
    x = np.arange(len(labels))
    plt.bar(x - 0.2, values_t6_tst, color='b', align='center', width=0.4, label='test set')
    plt.bar(x + .2, values_t6_trn, color='r', align='center', width=0.4, label='train set')
    plt.legend()
    plt.xticks(x, labels, rotation='vertical')
    plt.tight_layout()
    plt.show()


def keyword_classify(human_says):
    values = {'cuisine': [], 'location': [], 'price': []}
    with open(DSTC2_ONTOLOGY_FILE) as kb_fh:
        values = json.load(kb_fh)['informable']
    new_names = {'food': 'cuisine', 'area': 'location', 'pricerange': 'price'}
    del values['name']
    for slot in new_names:
        values[new_names[slot]] = values.pop(slot)
    # food values not in the kb, but asked by users on train data (only if the bot detected it as food type)
    values['cuisine'] += ['canapes', 'kosher', 'creative', 'caribbean', 'tuscan', 'traditional', 'austrian',
                          'swedish', 'christmas', 'australian', 'cantonese', 'irish', 'welsh', 'polynesian',
                          'romanian', 'german', 'greek', 'afghan', 'moroccan', 'belgian', 'hungarian', 'unusual',
                          'halal', 'english', 'swiss', 'world', 'vegetarian']
    # remove duplicates
    for slot in values:
        values[slot] = list(set(values[slot]))
    # add synonyms for each value of each entity
    synonyms = {slot: {value: [] for value in values[slot]} for slot in values}
    synonyms['location']['centre'] = ['center']
    synonyms['cuisine']['north_american'] = ['american']
    synonyms['price']['moderate'] = ['moderately']
    all_values = {entity: sorted(values[entity] + list(chain(*[synonyms[entity][syn]
                                                               for syn in synonyms[entity]])), reverse=True)
                  for entity in values}
    # make sure to capture only full words, not subwords, i.e. 'italian' is ok, 'kitalian' is not ok. Without this
    # 'north_american would be matched as location=north, cuisine=north_american
    all_values = {entity: ['(?<!\w)' + value + '(?!\w)' for value in all_values[entity]] for entity in all_values}

    human_templates = {
        'silence': [
            '<SILENCE>'
        ],
        'inform': [  # will take anything that mentions an entity, should be checked only after request_food etc
            # with the 3 entities
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine location price
                     for entity in ['cuisine', 'location', 'price']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine price location
                     for entity in ['cuisine', 'price', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location cuisine price
                     for entity in ['location', 'cuisine', 'price']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location price cuisine
                     for entity in ['location', 'price', 'cuisine']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price cuisine location
                     for entity in ['price', 'cuisine', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price location cuisine
                     for entity in ['price', 'location', 'cuisine']]) + '.*',
            # with 2 entities
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine location
                     for entity in ['cuisine', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location cuisine
                     for entity in ['location', 'cuisine']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine price
                     for entity in ['cuisine', 'price']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price cuisine
                     for entity in ['price', 'cuisine']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price location
                     for entity in ['price', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location price
                     for entity in ['location', 'price']]) + '.*',
            # with 1 entity
            '.*(?P<cuisine>(' + '|'.join(all_values['cuisine']) + ')).*',  # cuisine
            '.*(?P<location>(' + '|'.join(all_values['location']) + ')).*',  # location
            '.*(?P<price>(' + '|'.join(all_values['price']) + ')).*',  # price

            # not prividing any entities, still inform (only after the previous ones where discarded):
            'find a restaurant'
            # '.*(' + '|'.join(['(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'
            # for entity in all_values]) + ')+.*'
        ],
        'bye': [
            '\s*(good)?bye\s*'
        ],
        'dontcare': [
            'dont care',
            'it doesnt matter',
            '^any (part|area)',
            '^any price range$',
            '^doesnt matter$',
            '^any$',
            '^anything$',
            '^any kind$'
        ],
        'reqalts': [
            'anything else',
            'give me a different restaurant',
            '^what else$',
            'other (restaurant|choice)'
        ],
        'request_phone': [
            'what is the phone number',
            'phone( number)?( please)?( of the venue)?$',  # often bots answer only last request in a sentence
            # 'phone number and ((the )?area)|((the )?price range)'
            'phone number and (?!address)'
        ],
        'request_address': [
            'what is the address',
            'address( of the venue)?( please)?( there)?$',
            'where is it$',
            'address and the price range',
            'address and (the )?(?!phone)'
        ],
        'request_postcode': [
            'post ?code( of the venue)?( please)?$',
            'postal code$'
        ],
        'request_food': [
            '(type|kind) of food (do they)|(does it)',
            '^what type of food is it$',
            '^what type of food( does it serve)?$',
            '^(what is the )?type of food$'
        ],
        'request_location': [
            '^what is the area$',
            '^area$',
            '^what area$',
            '^and the area$',
            '^and what area of town is it in$',
            '^what area is it in$',
            'what part of town'
        ],
        'request_price': [
            'whats the price',
            'what is the price',
            'whats its price range',
            'the price range( of the venue)?$',
            '^price range$'
        ],
        'affirm': [
            '^yes$'
        ],
        'negate': [
            '^no$',
            '^wrong$'
        ]
    }
    human_templates = {intent: [re.compile(pattern) for pattern in human_templates[intent]]
                       for intent in human_templates}
    intent_priority = [  # re patterns are tried in this order. More general patterns go last
        'silence',
        'bye',
        'reqalts',
        'request_address',
        'request_phone',
        'request_postcode',
        'request_food',
        'request_location',
        'request_price',
        'inform',
        'dontcare',
        'affirm',
        'negate'
    ]

    def parse_example(text, act, regex):
        def check_if_synonym(value, entity):
            if value in values[entity]:
                return value
            else:
                for candidate_value in synonyms[entity]:
                    if value in synonyms[entity][candidate_value]:
                        return candidate_value
                raise Exception('unknown value for entity {}: {}'.format(entity, value))

        return {'text': text, 'intent': act,
                'entities': [{'start': regex.span(entity)[0], 'end': regex.span(entity)[1],
                              'value': check_if_synonym(regex.group(entity), entity), 'entity': entity}
                             for entity in regex.groupdict()]
                }

    for intent in intent_priority:
        for template in human_templates[intent]:
            match = template.search(human_says)
            if match:
                return parse_example(human_says, intent, match)
    return None


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=None,
                          zmin=1):  # pragma: no cover
    """Print and plot the confusion matrix for the intent classification.

    Normalization can be applied by setting `normalize=True`.
    """
    from matplotlib.colors import LogNorm

    zmax = cm.max()
    plt.clf()
    plt.imshow(cm, interpolation='nearest', cmap=cmap if cmap else plt.cm.Blues,
               aspect='auto', norm=LogNorm(vmin=zmin, vmax=zmax))
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        logger.info("Normalized confusion matrix: \n{}".format(cm))
    else:
        logger.info("Confusion matrix, without normalization: \n{}".format(cm))

    thresh = cm.max() / 2.
    for i, j in product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('Target')
    plt.xlabel('Predicted')


def plot_request_confusion_matrix():
    intent_examples = {
        'silence': {}, 'bye': {}, 'reqalts': {}, 'request_phone': {}, 'request_address': {}, 'request_postcode': {},
        'request_food': {}, 'request_location': {}, 'request_price': {}, 'inform': {}, 'dontcare': {}, 'affirm': {},
        'negate': {}
    }

    def give_act(bot_said):
        if 'is on' in bot_said and 'phone' in bot_said:
            return 'both'
        if 'is on' in bot_said:
            return 'address'
        if 'phone' in bot_said:
            return 'phone'
        return 'none'

    def requested_act(human_said):
        if 'phone' in human_said and 'address' in human_said:
            return 'both'
        if 'phone' in human_said:
            return 'phone'
        if 'address' in human_said:
            return 'address'
        return 'none'

    request_replies = defaultdict(list)
    for label, log in dstc2_reader.iter_dstc2_files_from_listfile(DSTCT2_TRN_LIST_FILE, path_prefix=DSTC2_DATA_PATH):
        with open(label) as label_fh, open(log) as log_fh:
            label, log = json.load(label_fh), json.load(log_fh)
        for i, human_turn in enumerate(label['turns']):
            act = keyword_classify(human_turn['transcription'])
            if act:
                requested = requested_act(act['text'])
                # if act['intent'] in ('request_address', 'request_phone'):
                #     print('human: {}\t bot: {}'.format(act['text'], log['turns'][i + 1]['output']['transcript']))
                if i < len(label['turns']) - 2:
                    given = give_act(log['turns'][i + 1]['output']['transcript'])
                    request_replies[requested].append(given)

                intent_examples[act['intent']][act['text']] = human_turn['semantics']
                # print('act: {}\tsemantics: {}'.format(act['intent'], human_turn['semantics']))
    # for intent in intent_examples:
    #     for example in intent_examples[intent]:
    #         print('{}: {}\t({})'.format(intent, example, intent_examples[intent][example]))
    for request in request_replies:
        request_replies[request] = Counter(request_replies[request])
    classes = ['none', 'both', 'phone', 'address']
    conf_matrix = []
    for c in classes:
        counter = request_replies[c]
        conf_matrix.append([counter[c2] for c2 in classes])
    conf_matrix = np.array(conf_matrix)
    plot_confusion_matrix(conf_matrix, classes, title='Request confusion matrix')
    plt.show()
    print(request_replies)


def parse_user_text_with_dstc2_das(human_says, json_semantics):
    all_values = {entity: sorted(values[entity] + list(chain(*[synonyms[entity][syn]
                                                               for syn in synonyms[entity]])), reverse=True)
                  for entity in values}
    # make sure to capture only full words, not subwords, i.e. 'italian' is ok, 'kitalian' is not ok. Without this
    # 'north_american would be matched as location=north, cuisine=north_american
    all_values = {entity: ['(?<!\w)' + value + '(?!\w)' for value in all_values[entity]] for entity in all_values}

    entity_regex = [  # will take anything that mentions an entity, should be checked only after request_food etc
            # with the 3 entities
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine location price
                     for entity in ['cuisine', 'location', 'price']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine price location
                     for entity in ['cuisine', 'price', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location cuisine price
                     for entity in ['location', 'cuisine', 'price']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location price cuisine
                     for entity in ['location', 'price', 'cuisine']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price cuisine location
                     for entity in ['price', 'cuisine', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price location cuisine
                     for entity in ['price', 'location', 'cuisine']]) + '.*',
            # with 2 entities
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine location
                     for entity in ['cuisine', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location cuisine
                     for entity in ['location', 'cuisine']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # cuisine price
                     for entity in ['cuisine', 'price']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price cuisine
                     for entity in ['price', 'cuisine']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # price location
                     for entity in ['price', 'location']]) + '.*',
            ''.join(['.*(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'  # location price
                     for entity in ['location', 'price']]) + '.*',
            # with 1 entity
            '.*(?P<cuisine>(' + '|'.join(all_values['cuisine']) + ')).*',  # cuisine
            '.*(?P<location>(' + '|'.join(all_values['location']) + ')).*',  # location
            '.*(?P<price>(' + '|'.join(all_values['price']) + ')).*',  # price

            # not prividing any entities, still inform (only after the previous ones where discarded):
            'find a restaurant'
            # '.*(' + '|'.join(['(?P<' + entity + '>(' + '|'.join(all_values[entity]) + '))'
            # for entity in all_values]) + ')+.*'
        ]

    entity_regex = [re.compile(pattern) for pattern in entity_regex]

    def get_intent():
        acts = set([s['act'] for s in json_semantics])
        if 'bye' in acts:
            return 'bye'
        elif 'reqalts' in acts and not 'inform' in acts:
            return 'reqalts'
        elif 'request' in acts and not 'inform' in acts:
            requested = [sem['slots'][0][1] for sem in json_semantics if sem['act'] == 'request']
            if 'addr' in requested:
                return 'request_address'
            elif 'phone' in requested:
                return 'request_phone'
            elif 'postcode' in requested:
                return 'request_postcode'
            elif 'food' in requested:
                return 'request_food'
            elif 'area' in requested:
                return 'request_location'
            elif 'pricerange' in requested:
                return 'request_price'
            else:
                return 'unknown'
        elif acts == {'confirm'} and json_semantics[0]['slots'][0][1] == 'food':
            return 'request_food'
        elif 'inform' in acts:
            informed = set([sem['slots'][0][1] for sem in json_semantics if sem['act'] == 'inform'])
            if informed != {'dontcare'}:
                return 'inform'
            else:
                return 'dontcare'
        elif acts == {'affirm'} or acts == {'ack'} or acts == {'ack', 'affirm'}:
            return 'affirm'
        elif acts == {'deny'} or acts == {'negate'} or acts == {'deny', 'negate'}:
            return 'negate'
        else:
            return 'unknown'

    def check_if_synonym(value, entity):
        if value in values[entity]:
            return value
        else:
            for candidate_value in synonyms[entity]:
                if value in synonyms[entity][candidate_value]:
                    return candidate_value
            raise Exception('unknown value for entity {}: {}'.format(entity, value))

    intent = get_intent()
    ents = []
    if intent == 'inform':
        for pattern in entity_regex:
            match = pattern.search(human_says)
            if match:
                ents = [{'start': match.span(entity)[0], 'end': match.span(entity)[1],
                         'value': check_if_synonym(match.group(entity), entity), 'entity': entity}
                        for entity in match.groupdict()]
                break
    return {'text': human_says, 'intent': intent, 'entities': ents}


def produce_dstc2_rasa_nlu_file(synonyms):
    examples = []
    for label, log in dstc2_reader.iter_dstc2_files_from_listfile(DSTCT2_TRN_LIST_FILE, path_prefix=DSTC2_DATA_PATH):
        with open(label) as label_fh, open(log) as log_fh:
            label, log = json.load(label_fh), json.load(log_fh)
        for i, human_turn in enumerate(label['turns']):
            examples.append(parse_user_text_with_dstc2_das(human_turn['transcription'],
                                                           human_turn['semantics']['json']))

    synonyms = [{"value": value, "synonyms": synonyms[entity][value]}
                for entity in synonyms for value in synonyms[entity] if synonyms[entity][value]]
    with open('data/rasa/t6_nlu_dstc2_trn.json', 'w') as fh:
        json.dump({'rasa_nlu_data': {'common_examples': examples, 'entity_synonyms': synonyms, 'regex_features': []}},
                  fh, indent=2)


def action_confusion_matrix():
    with open('fabot/custom/lstm/results/tst_t5_lstm_offline_nlu_rasa_results.json') as res_fh:
        results = json.load(res_fh)
    act_predictions = defaultdict(list)
    reader = BabiT5Reader()
    for dialog in results:
        for turn in dialog:
            target_act = reader.get_bot_act(turn['target'])
            predicted_act = reader.get_bot_act(turn['actual'])
            act_predictions[target_act].append(predicted_act)
    for act in act_predictions:
        act_predictions[act] = Counter(act_predictions[act])
    classes = sorted(list(set(act_predictions.keys())))
    conf_matrix = []
    for c in classes:
        counter = act_predictions[c]
        conf_matrix.append([counter[c2] for c2 in classes])
    conf_matrix = np.array(conf_matrix)
    plot_confusion_matrix(conf_matrix, classes, title='Bot act confusion matrix')
    plt.show()


def evaluate_from_file():
    from rasa_nlu.evaluate import evaluate_intents
    with open('fabot/custom/lstm/results/tst_t5_lstm_offline_nlu_rasa_results.json') as res_fh:
        results = json.load(res_fh)
    act_predictions = defaultdict(list)
    reader = BabiT5Reader()
    targets, actuals = [], []
    for dialog in results:
        for turn in dialog:
            target_act = reader.get_bot_act(turn['target'])
            predicted_act = reader.get_bot_act(turn['actual'])
            targets.append(target_act)
            actuals.append(predicted_act)
    evaluate_intents(targets, actuals)


def compute_accuracy_from_file():
    tst_file = BABI_T5_TST_FILE
    total_turns = 18398
    total_dialogs = 1000
    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    with open('fabot/custom/lstm/results/tst_t5_lstm_offline_nlu_rasa_results.json') as res_fh:
        results = json.load(res_fh)
    reader = BabiT5Reader()
    for story in results:
        dialog_act_matches, dialog_literal_matches = 0, 0
        for turn in story:
            dialog_act_matches += int(turn['act_match'])
            dialog_literal_matches += int(turn['literal_match'])
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_act_matches, total_turns,
                                                                                total_act_matches / total_turns,
                                                                                perfect_act_dialogs, total_dialogs,
                                                                                perfect_act_dialogs / total_dialogs))
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_literal_matches, total_turns,
                                                                                total_literal_matches / total_turns,
                                                                                perfect_literal_dialogs, total_dialogs,
                                                                                perfect_literal_dialogs / total_dialogs
                                                                                ))


def print_scarse_traindata_degradation():
    train_sizes = [1000, 500, 250, 100, 50, 10]
    acc_william = [93.28, 93.28, 93.19, 93.09, 92.44, 69.31]
    diag_acc_wi = [9.5, 8.4, 10.1, 8, 5.1, 0]
    acc_rasa = [92.88, 93.04, 93.79, 43.94, 50.67, 31.66]
    diag_acc_ra = [5.1, 8, 13.1, 0, 0, 0]
    plt.plot(train_sizes, acc_william, 'r-o', label='word-based turn acc')
    plt.plot(train_sizes, acc_rasa, 'b-o', label='semantic turn acc')
    plt.plot(train_sizes, diag_acc_wi, 'rs-', label='word-based diag acc')
    plt.plot(train_sizes, diag_acc_ra, 'bs-', label='semantic diag acc')
    plt.xticks(train_sizes, train_sizes)
    plt.legend()
    plt.ylabel('% Accuracy')
    plt.xlabel('Train dialogs')
    plt.title('Accuracy by amount of training dialogs')
    plt.show()


def make_kb_t5oovrestaurants_file():
    from globals import BABI_T5_TST_OOV_FILE, BABI_T5_KB_OOV_FILE
    with open(BABI_T5_KB_OOV_FILE, 'w') as kb_oov_fh:
        kb_oov_fh.write('')  # just to clean it
    rest_lines = []
    with open(BABI_T5_TST_OOV_FILE, 'r') as babi_file, open(BABI_T5_KB_OOV_FILE, 'a') as kb_oov_fh:
        for line in babi_file:
            if line != '\n':  # end of story
                chunks = line.split('\t')
                chunks[0] = ' '.join(chunks[0].split(' ')[1:])  # rid of initial number
                if len(chunks) == 1:  # api call results
                    rest_lines.append(chunks[0])
        rest_lines = sorted(set(rest_lines))
        for rest_line in rest_lines:
            kb_oov_fh.write('1 ' + rest_line)


def validate_t5oovkb_sentences():
    from globals import BABI_T5_TST_OOV_FILE
    reader = BabiT5Reader()
    examples, _, _, _ = reader.extract_rasa_nlu_training_examples(BABI_T5_TST_OOV_FILE)
    for e in examples:
        if not e['intent']:
            print(e['text'])


def test_ner():
    from globals import NLU_T6_MODEL_PATH
    from rasa_core.interpreter import RasaNLUInterpreter
    from data.feature_factory import T6Featurizer
    from sklearn.metrics import precision_recall_fscore_support
    entity_map = {'area': 'location', 'pricerange': 'price', 'food': 'cuisine'}
    nlu_preds_cuisine, regex_preds_cuisine, targets_cuisine = [], [], []
    nlu_preds_location, regex_preds_location, targets_location = [], [], []
    nlu_preds_price, regex_preds_price, targets_price = [], [], []
    nlu = RasaNLUInterpreter(NLU_T6_MODEL_PATH)
    regex = T6Featurizer(use_bow=False, use_turn=False, use_bot_utter=False, use_embeddings=False, use_intent=False,
                         use_nlu_entity_extractor=False, use_entities=True, use_context=False)
    for label, _ in dstc2_reader.iter_dstc2_files_from_listfile(DSTCT2_TST_LIST_FILE, path_prefix=DSTC2_DATA_PATH):
        with open(label) as label_fh:
            label = json.load(label_fh)
        for i, human_turn in enumerate(label['turns']):
            text = human_turn['transcription']
            turn_targets = {'cuisine': 'none', 'price': 'none', 'location': 'none'}
            turn_nlu_preds = {'cuisine': 'none', 'price': 'none', 'location': 'none'}
            turn_regex_preds = {'cuisine': 'none', 'price': 'none', 'location': 'none'}
            inform_acts = [act['slots'][0] for act in human_turn['semantics']['json'] if act['act'] == 'inform']
            for act_entity in inform_acts:
                if act_entity[0] in entity_map:
                    turn_targets[entity_map[act_entity[0]]] = act_entity[1]
            targets_cuisine.append(turn_targets['cuisine'])
            targets_location.append(turn_targets['location'])
            targets_price.append(turn_targets['price'])
            # turn_targets = [item[1] for item in sorted(turn_targets.items(), key=lambda x: x[0])]
            # targets += turn_targets
            nlu_parse_data = nlu.parse(text)
            for en in nlu_parse_data['entities']:
                turn_nlu_preds[en['entity']] = en['value']
            nlu_preds_cuisine.append(turn_nlu_preds['cuisine'])
            nlu_preds_location.append(turn_nlu_preds['location'])
            nlu_preds_price.append(turn_nlu_preds['price'])
            # turn_nlu_preds = [item[1] for item in sorted(turn_nlu_preds.items(), key=lambda x: x[0])]
            # nlu_preds += turn_nlu_preds
            turn_regex_preds_tmp = regex.extract_entities(text)
            for en, val in turn_regex_preds_tmp.items():
                turn_regex_preds[en] = val
            regex_preds_cuisine.append(turn_regex_preds['cuisine'])
            regex_preds_location.append(turn_regex_preds['location'])
            regex_preds_price.append(turn_regex_preds['price'])
            # turn_regex_preds = [item[1] for item in sorted(turn_regex_preds.items(), key=lambda x: x[0])]
            # regex_preds += turn_regex_preds
    print(precision_recall_fscore_support(targets_cuisine, nlu_preds_cuisine, average='weighted'))
    print(precision_recall_fscore_support(targets_location, nlu_preds_location, average='weighted'))
    print(precision_recall_fscore_support(targets_price, nlu_preds_price, average='weighted'))
    print('done')
    print(precision_recall_fscore_support(targets_cuisine, regex_preds_cuisine, average='weighted'))
    print(precision_recall_fscore_support(targets_location, regex_preds_location, average='weighted'))
    print(precision_recall_fscore_support(targets_price, regex_preds_price, average='weighted'))


def mem_size_train():
    from fabot.custom.memnet import model
    from data.feature_factory import T6Featurizer
    from numpy import mean
    features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': True,
                'use_entities': False, 'use_context': False}
    featurizer = T6Featurizer(**features)
    mem_sizes = [29, 25, 20, 15, 10, 5]
    for mem_size in mem_sizes:
        trn_history, trn_query, trn_label, trn_entities, batch_indexes = model.build_batches(filename=BABI_T6_TRN_FILE,
                                                                                             featurizer=featurizer,
                                                                                             batch_size=32,
                                                                                             max_memory_size=mem_size)
        dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes = model.build_batches(
            filename=BABI_T6_DEV_FILE, featurizer=featurizer, batch_size=100, max_memory_size=mem_size)
        memnet = model.MemoryNetwork(num_actions=featurizer.num_actions(), utterance_len=featurizer.feature_len(),
                                     embedding_size=100, mem_size=mem_size, hops=2, keep_prob=0.8, clip_norm=1.)
        highest_dev_acc = 0
        chances2improve = 5
        stop = False
        for epoch in range(40):
            if stop:
                break
            batch_indexes = list(batch_indexes)
            trn_accuracies = []
            for i, (b_start, b_end) in enumerate(batch_indexes):
                pred, loss = memnet.train_step(history_batch=trn_history[b_start:b_end],
                                               query_batch=trn_query[b_start:b_end],
                                               label_batch=trn_label[b_start:b_end])
                accuracy = memnet.sess.run(memnet.accuracy, feed_dict={memnet.history: trn_history[b_start:b_end],
                                                                       memnet.queries: trn_query[b_start:b_end],
                                                                       memnet.labels: trn_label[b_start:b_end],
                                                                       memnet.keep_prob: 1})
                if i % 100 == 0:
                    logging.info('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
                trn_accuracies.append(accuracy)
            dev_accuracies, dev_losses = [], []
            for i, (b_start, b_end) in enumerate(dev_batch_indexes):
                _, dev_loss = memnet.train_step(history_batch=dev_history[b_start:b_end],
                                                query_batch=dev_query[b_start:b_end],
                                                label_batch=dev_label[b_start:b_end])
                dev_accuracy = memnet.sess.run(memnet.accuracy, feed_dict={memnet.history: dev_history[b_start:b_end],
                                                                           memnet.queries: dev_query[b_start:b_end],
                                                                           memnet.labels: dev_label[b_start:b_end],
                                                                           memnet.keep_prob: 1})
                dev_accuracies.append(dev_accuracy)
                dev_losses.append(dev_loss)
            dev_acc = mean(dev_accuracies)
            if dev_acc > highest_dev_acc:
                highest_dev_acc = dev_acc
                chances2improve = 5
                memnet.persist('misc_experiments/memnet_no_context_saved_model/{}/'.format(mem_size))
            else:
                chances2improve -= 1
                if chances2improve == 0:
                    logger.info(
                        'no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                    stop = True
            logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(
                epoch,
                mean(dev_losses),
                dev_acc,
                mean(trn_accuracies)
            ))


def mem_size_test():
    from data.feature_factory import T6Featurizer
    from numpy import argmax
    from fabot.custom.memnet import model
    import numpy as np

    def pad_p(p):
        padding = np.array([[0] * (20 - p.shape[1])])
        return np.concatenate((padding, p), axis=1)

    def bot_prev_utter(story, turn, prev_pred):
        if turn == 0:
            return ''
        else:
            return story[turn - 1]['bot']
    features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': True,
                'use_entities': False, 'use_context': False}
    featurizer = T6Featurizer(**features)
    trn_mem_sizes = [29]
    # tst_mem_sizes = [29, 25, 20, 15, 10, 5]
    tst_mem_sizes = [20]
    p_hist = []
    for trn_mem_size in trn_mem_sizes:
        memnet = model.MemoryNetwork.load('misc_experiments/memnet_no_context_saved_model/{}/'.format(trn_mem_size))
        for tst_mem_size in tst_mem_sizes:
            results = []
            total_act_matches, total_literal_matches = 0, 0
            perfect_act_dialogs, perfect_literal_dialogs = 0, 0
            tst_file = BABI_T6_TST_FILE
            total_turns = 11237
            total_dialogs = 1117
            for story in BabiReader.babi_dialogue_iterator(tst_file):
                featurizer.reset()
                story_results = []
                dialog_act_matches, dialog_literal_matches = 0, 0
                h = []
                prev_pred = ''  # initial value for the previous prediction
                for i, turn in enumerate(story):
                    x = featurizer.featurize(user_text=turn['human'],
                                             prev_bot_text=bot_prev_utter(story, i, prev_pred), turn=i)
                    prediction = memnet.prediction(history=h if len(h) > 0 else [[0] * featurizer.feature_len()],
                                                   query=x)
                    p = memnet.sess.run(memnet.p, feed_dict={memnet.history: [h if len(h) > 0 else [[0] * featurizer.feature_len()]],
                                                             memnet.queries: [x],
                                                             memnet.keep_prob: 1})
                    p_hist.append(pad_p(p))
                    turn_results = dict()
                    turn_results['human'] = turn['human']
                    turn_results['target'] = turn['bot']
                    actual_da = featurizer.get_bot_act(turn['bot'])
                    predicted_da = featurizer.id2act(argmax(prediction))
                    prev_pred = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
                    turn_results['actual'] = prev_pred
                    turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                             string=turn_results['target']) is not None
                    turn_results['act_match'] = actual_da == predicted_da
                    story_results.append(turn_results)

                    h.append(x)
                    if len(h) > tst_mem_size:
                        h = h[::-1][:tst_mem_size][::-1]

                    dialog_act_matches += int(turn_results['act_match'])
                    dialog_literal_matches += int(turn_results['literal_match'])
                total_act_matches += dialog_act_matches
                total_literal_matches += dialog_literal_matches
                perfect_act_dialogs += int(dialog_act_matches == len(story))
                perfect_literal_dialogs += int(dialog_literal_matches == len(story))
                results.append(story_results)
            with open('misc_experiments/memnet_nocontext_results/{}_{}.json'.format(trn_mem_size, tst_mem_size), 'w') as fh:
                json.dump(results, fh, indent=2)
            logging.info('train {}, test {}:'.format(trn_mem_size, tst_mem_size))
            logging.info('test act match results:\n'
                         'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
                total_act_matches, total_turns, total_act_matches / total_turns, perfect_act_dialogs, total_dialogs,
                                                perfect_act_dialogs / total_dialogs))
            logging.info('test literal match results:\n'
                         'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
                total_literal_matches, total_turns, total_literal_matches / total_turns, perfect_literal_dialogs, total_dialogs,
                                                    perfect_literal_dialogs / total_dialogs))
            memnet.sess.close()
            p_hist = np.array(p_hist).squeeze()
            print(np.mean(p_hist, axis=0))


def memnet_t5_pcheck_train():
    from globals import BABI_T5_DEV_FILE
    from data.feature_factory import T5Featurizer
    from fabot.custom.memnet.model import build_batches, MemoryNetwork
    from numpy import mean
    num_actions = T5Featurizer.num_actions()
    features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': True,
                'use_entities': True, 'use_context': False}
    featurizer = T5Featurizer(**features)
    h_len = featurizer.feature_len()
    print_cycle = 100
    hops = 2
    embedding_size = 100
    batch = 32
    mem_size = 9
    epochs = 35
    clip_norm = 1.
    keep_prob = 0.8
    trn_file = BABI_T5_TRN_FILE
    dev_file = BABI_T5_DEV_FILE
    logging.info(
        'starting training\nConfig:\nhops: {}\nactions: {}\nhistory utterance length: {}\n'
        'embedding size: {}\nbatch size: {}\nmemory size: {}\nepochs: {}\ngradient clip norm: {}\n'
        'keep prob: {}\n'.format(hops, num_actions, h_len, embedding_size, batch, mem_size, epochs,
                                 clip_norm,
                                 keep_prob))
    print('getting training data')
    trn_history, trn_query, trn_label, trn_entities, batch_indexes = build_batches(filename=trn_file,
                                                                                   featurizer=featurizer,
                                                                                   batch_size=batch,
                                                                                   max_memory_size=mem_size)
    print('getting dev data')
    dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes = build_batches(
        filename=dev_file, featurizer=featurizer, batch_size=100, max_memory_size=mem_size)

    model = MemoryNetwork(num_actions=num_actions, utterance_len=h_len,
                          embedding_size=embedding_size, mem_size=mem_size, hops=hops, keep_prob=keep_prob,
                          clip_norm=clip_norm)
    highest_dev_acc = 0
    chances2improve = 5
    stop = False
    for epoch in range(epochs):
        if stop:
            break
        batch_indexes = list(batch_indexes)
        trn_accuracies = []
        for i, (b_start, b_end) in enumerate(batch_indexes):
            pred, loss = model.train_step(history_batch=trn_history[b_start:b_end],
                                          query_batch=trn_query[b_start:b_end],
                                          label_batch=trn_label[b_start:b_end])
            accuracy = model.sess.run(model.accuracy, feed_dict={model.history: trn_history[b_start:b_end],
                                                                 model.queries: trn_query[b_start:b_end],
                                                                 model.labels: trn_label[b_start:b_end],
                                                                 model.keep_prob: 1})
            if i % print_cycle == 0:
                logging.info('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
            trn_accuracies.append(accuracy)
        dev_accuracies, dev_losses = [], []
        for i, (b_start, b_end) in enumerate(dev_batch_indexes):
            _, dev_loss = model.train_step(history_batch=dev_history[b_start:b_end],
                                           query_batch=dev_query[b_start:b_end],
                                           label_batch=dev_label[b_start:b_end])
            dev_accuracy = model.sess.run(model.accuracy, feed_dict={model.history: dev_history[b_start:b_end],
                                                                     model.queries: dev_query[b_start:b_end],
                                                                     model.labels: dev_label[b_start:b_end],
                                                                     model.keep_prob: 1})
            dev_accuracies.append(dev_accuracy)
            dev_losses.append(dev_loss)
        dev_acc = mean(dev_accuracies)
        if dev_acc > highest_dev_acc:
            highest_dev_acc = dev_acc
            chances2improve = 5
            model.persist('misc_experiments/t5/memnet_nocontext_persisted/')
        else:
            chances2improve -= 1
            if chances2improve == 0:
                logger.info('no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                stop = True
        logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(
            epoch,
            mean(dev_losses),
            dev_acc,
            mean(trn_accuracies)
        ))


def memnet_t5_pcheck_test():
    from data.feature_factory import T5Featurizer
    from numpy import argmax
    from fabot.custom.memnet import model
    import numpy as np

    def pad_p(p):
        padding = np.array([[0] * (20 - p.shape[1])])
        return np.concatenate((padding, p), axis=1)

    def bot_prev_utter(story, turn, prev_pred):
        if turn == 0:
            return ''
        else:
            return story[turn - 1]['bot']

    features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': True,
                'use_entities': True, 'use_context': False}

    featurizer = T5Featurizer(**features)
    memnet = model.MemoryNetwork.load('misc_experiments/t5/memnet_nocontext_persisted/')
    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    tst_file = BABI_T5_TST_FILE
    total_turns = 18398
    total_dialogs = 1000
    p_hist = []
    for story in BabiReader.babi_dialogue_iterator(tst_file):
        featurizer.reset()
        story_results = []
        dialog_act_matches, dialog_literal_matches = 0, 0
        h = []
        prev_pred = ''  # initial value for the previous prediction
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'],
                                     prev_bot_text=bot_prev_utter(story, i, prev_pred), turn=i)
            prediction = memnet.prediction(history=h if len(h) > 0 else [[0] * featurizer.feature_len()],
                                           query=x)
            p = memnet.sess.run(memnet.p, feed_dict={
                memnet.history: [h if len(h) > 0 else [[0] * featurizer.feature_len()]],
                memnet.queries: [x],
                memnet.keep_prob: 1})
            p_hist.append(pad_p(p))
            turn_results = dict()
            turn_results['human'] = turn['human']
            turn_results['target'] = turn['bot']
            actual_da = featurizer.get_bot_act(turn['bot'])
            predicted_da = featurizer.id2act(argmax(prediction))
            prev_pred = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
            turn_results['actual'] = prev_pred
            turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                     string=turn_results['target']) is not None
            turn_results['act_match'] = actual_da == predicted_da
            story_results.append(turn_results)

            h.append(x)

            dialog_act_matches += int(turn_results['act_match'])
            dialog_literal_matches += int(turn_results['literal_match'])
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
        results.append(story_results)
    with open('misc_experiments/t5/memnet_nocontext_results.json', 'w') as fh:
        json.dump(results, fh, indent=2)
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_act_matches, total_turns, total_act_matches / total_turns, perfect_act_dialogs, total_dialogs,
                                        perfect_act_dialogs / total_dialogs))
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_literal_matches, total_turns, total_literal_matches / total_turns, perfect_literal_dialogs,
        total_dialogs,
                                            perfect_literal_dialogs / total_dialogs))
    memnet.sess.close()
    p_hist = np.array(p_hist).squeeze()
    print(np.mean(p_hist, axis=0))


def lstm_t6_nocontext_train():
    from data.feature_factory import T6Featurizer
    from fabot.custom.lstm.model import format_babi_data, CustomLSTM
    import tensorflow as tf
    # features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': True,
    #             'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': True,
    #             'use_entities': False, 'use_context': False}
    features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': True, 'use_intent': False, 'use_nlu_entity_extractor': True,
                'use_entities': True, 'use_context': True}
    featurizer = T6Featurizer(**features)
    num_actions = T6Featurizer.num_actions()
    input_dim = featurizer.feature_len()
    hidden_size = 128
    trn_file = BABI_T6_TRN_FILE
    dev_file = BABI_T6_DEV_FILE

    epochs = 35
    clip_norm = 1.
    logging.info('starting training\nConfig:\nactions: {}\ninput_dim: {}\nhidden_size: {}\nepochs: {}\ngradient clip '
                 'norm: {}\n'.format(num_actions, input_dim, hidden_size, epochs, clip_norm))
    print('formatting training data')
    trn_dialogs = format_babi_data(filename=trn_file, featurizer=featurizer)
    print('formatting dev data')
    dev_dialogs = format_babi_data(filename=dev_file, featurizer=featurizer)

    model = CustomLSTM(input_dim=input_dim, hidden_size=hidden_size, num_actions=num_actions)

    optimizer = tf.train.AdadeltaOptimizer(0.1)

    grads, vars = zip(*optimizer.compute_gradients(model.loss))
    grads_clipped, _ = tf.clip_by_global_norm(grads, clip_norm=clip_norm)
    train_op = optimizer.apply_gradients(zip(grads_clipped, vars))

    model.sess.run(tf.global_variables_initializer())
    total_turns = sum([len(dialog) for dialog in trn_dialogs])
    dev_total_turns = sum([len(dialog) for dialog in dev_dialogs])
    highest_dev_matches = 0
    chances2improve = 5
    stop = False
    for epoch in range(epochs):
        if stop:
            break
        total_loss = 0
        total_matches = 0
        perfect_dialogs = 0
        for di, dialog in enumerate(trn_dialogs):
            dialog_matches = 0
            model.reset_conversation_state()
            for turn in dialog:
                pred, loss = model.train_step(featurized_turn=turn['x'], action=turn['y'],
                                              action_mask=[1] * num_actions, train_op=train_op)
                total_loss += loss
                dialog_matches += int(pred == turn['y'])
            total_matches += dialog_matches
            perfect_dialogs += int(dialog_matches == len(dialog))
        logging.info('epoch: {}\ttrn loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({:.2%})'.format(
            epoch, total_loss, total_matches, total_turns, total_matches/total_turns, perfect_dialogs, len(trn_dialogs),
            perfect_dialogs/len(trn_dialogs)))
        # evaluate in dev
        dev_total_loss = 0
        dev_total_matches = 0
        dev_perfect_dialogs = 0
        for dialog in dev_dialogs:
            dev_dialog_matches = 0
            for turn in dialog:
                pred = model.prediction(features=turn['x'])
                dev_total_loss += loss
                dev_dialog_matches += int(pred == turn['y'])
            dev_total_matches += dev_dialog_matches
            dev_perfect_dialogs += int(dev_dialog_matches == len(dialog))
        logging.info('dev loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({:.2%})'.format(
            dev_total_loss, dev_total_matches, dev_total_turns, dev_total_matches / dev_total_turns,
            dev_perfect_dialogs, len(dev_dialogs), dev_perfect_dialogs / len(dev_dialogs)))
        if dev_total_matches >= highest_dev_matches:
            highest_dev_matches = dev_total_matches
            chances2improve = 5
            # model.persist('misc_experiments/lstm_nocontext/persisted/')
            model.persist('misc_experiments/ensemble/lstm/persisted/')
        else:
            chances2improve -= 1
            if chances2improve == 0:
                logger.info('no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                stop = True


def lstm_t6_nocontext_test():
    from fabot.custom.lstm.model import CustomLSTM
    from data.feature_factory import T6Featurizer

    def bot_prev_utter(story, turn, prev_pred):
        if turn == 0:
            return ''
        else:
            return story[turn - 1]['bot']
    # model = CustomLSTM.load(path='misc_experiments/lstm_nocontext/persisted')
    model = CustomLSTM.load(path='misc_experiments/ensemble/lstm/persisted')
    # features = {'use_bow': False, 'use_turn': True, 'use_bot_utter': True,
    #             'use_embeddings': False, 'use_intent': True, 'use_nlu_entity_extractor': True,
    #             'use_entities': False, 'use_context': False}
    features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': True, 'use_intent': False, 'use_nlu_entity_extractor': True,
                'use_entities': True, 'use_context': True}
    featurizer = T6Featurizer(**features)
    tst_file = BABI_T6_TST_FILE
    total_turns = 11237
    total_dialogs = 1117
    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    for si, story in enumerate(BabiReader.babi_dialogue_iterator(tst_file)):
        print('\rstory {}'.format(si + 1), end="", flush=True)
        featurizer.reset()
        story_results = []
        dialog_act_matches, dialog_literal_matches = 0, 0
        prev_pred = ''  # just to have an initial previous prediction
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text=bot_prev_utter(story, i, prev_pred), turn=i)
            pred = model.prediction(features=np.array(x, dtype=np.float32))
            turn_results = dict()
            turn_results['human'] = turn['human']
            turn_results['target'] = turn['bot']
            actual_da = featurizer.get_bot_act(turn['bot'])
            predicted_da = featurizer.id2act(pred)
            prev_pred = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
            turn_results['actual'] = prev_pred
            turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                     string=turn_results['target']) is not None
            turn_results['act_match'] = actual_da == predicted_da
            story_results.append(turn_results)

            dialog_act_matches += int(turn_results['act_match'])
            dialog_literal_matches += int(turn_results['literal_match'])
        model.reset_conversation_state()
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
        results.append(story_results)
    # with open('misc_experiments/lstm_nocontext/results.json', 'w') as fh:
    with open('misc_experiments/ensemble/lstm/results.json', 'w') as fh:
        json.dump(results, fh, indent=2)
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_act_matches, total_turns,
                                                                                total_act_matches / total_turns,
                                                                                perfect_act_dialogs, total_dialogs,
                                                                                perfect_act_dialogs / total_dialogs))
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_literal_matches, total_turns,
                                                                                total_literal_matches / total_turns,
                                                                                perfect_literal_dialogs, total_dialogs,
                                                                                perfect_literal_dialogs / total_dialogs
                                                                                ))


def format_babi_data(stories, featurizer):
    """
    produces bAbI data in a format suitable for the memory network. Each conversation provides as many training examples
    as turns. Turn i produces a training example that contains the conversation history up to turn i-1, the user
    utterance from turn i and the bot action at turn i
    :param filename: bAbI conversation filename
    :param featurizer: featurizer object
    :return: List of training examples with labels. Each element is a Dictionary['history': h, 'query': q, 'label': l,
    'entities': e]
    h: List, h[i] is the featurized data point at turn i in the conversation
    q: vector of features representing the current turn (in the same format as the elements of h)
    l: 1 hot vector indicating the bot action at the current turn
    e: Dictionary with the value of each entity at that point in the conversation (None, for those with no value set)
    """
    data = []

    def prev_bot_utter():
        return '' if i == 0 else story[i-1]['bot']

    for si, story in enumerate(stories):
        logger.info('featurizing story {}'.format(si))
        h = []
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text=prev_bot_utter(), turn=i)
            data.append({'history': copy(h), 'query': x, 'label': featurizer.bot_features(turn['bot']),
                         'entities': copy(featurizer.slot_values)})
            h.append(x)
        featurizer.reset()
    return data


def build_batches(stories, featurizer, batch_size=32, max_memory_size=8):
    """
    Produces batch indexes of points with similar length of history and adds padding so that the history component of
    all points in a batch have the same length
    :param filename: story list
    :param featurizer: featurizer object
    :param batch_size: number of elements in a batch, unless there are not enough elements, then a batch will have the
    remaining points, with len < batch_size
    :param max_memory_size: max number of previous utterances (bot and user alike) to keep in history for a single
    data point
    :return: history, query, label, entities, batch_indexes. Each one is a list. The ith element of all lists is refers
    to one data point. The lists are sorted by decreasing length of history and adding padding so that all histories in
    the same batch have equal length. batch_indexes is an iterable of Tuple[start, end], where end is not part of the
    current batch but of the next only (i.e. end_i = start_i+1 for all i except the last). Do note the end index of the
    last batch is not checked against the number of elements in the data, therefore this number can be higher.
    This should not be a problem if data is split using the data[start:end] slicing format
    """
    data = format_babi_data(stories=stories, featurizer=featurizer)
    max_memory_size = min(max_memory_size, max(len(x['history']) for x in data))  # no point in max_mem > longest h
    batch_size = min(batch_size, len(data))
    data.sort(key=lambda x: len(x['history']), reverse=True)
    history, query, label, entities = [], [], [], []
    batch_memory_size = max_memory_size  # redundant, just to comply with PEP8 (batch_mem could be reference before bla)
    for i, x in enumerate(data):
        h, q, l, e = x.values()
        if i % batch_size == 0:  # new batch. history length of this first point in the batch determines memory_size
            batch_memory_size = max(1, min(max_memory_size, len(h)))  # memory in [1, max_memory_size]
        h = h[::-1][:batch_memory_size][::-1]  # take only last memory_size sentences (flip, cut at mem size, flip back)
        pad_size = max(0, batch_memory_size - len(h))  # pad h
        for _ in range(pad_size):  # empty histories will thus consist of 1 0 padded memory
            h.append([0] * featurizer.feature_len())
        history.append(h)
        query.append(q)
        label.append(l)
        entities.append(e)
    batch_indexes = list(zip(range(0, len(data) - batch_size, batch_size), range(batch_size, len(data), batch_size)))
    return history, query, label, entities, batch_indexes


def stacking_memnet_train():
    from fabot.custom.memnet import model
    from data.feature_factory import T6Featurizer
    from numpy import mean
    from numpy.random import shuffle, seed
    seed(42)
    stories = []
    for filename in [BABI_T6_TRN_FILE, BABI_T6_DEV_FILE]:
        for story in BabiReader.babi_dialogue_iterator(filename):
            stories.append(story)
    shuffle(stories)
    features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': True, 'use_intent': False, 'use_nlu_entity_extractor': True,
                'use_entities': True, 'use_context': True}
    featurizer = T6Featurizer(**features)
    trn_history, trn_query, trn_label, trn_entities, batch_indexes = build_batches(
        stories=stories[:int(len(stories)*.4)],
        featurizer=featurizer,
        batch_size=32,
        max_memory_size=10)
    dev_history, dev_query, dev_label, dev_entities, dev_batch_indexes = build_batches(
        stories=stories[int(len(stories)*.4):int(len(stories)*.5)], featurizer=featurizer, batch_size=100, max_memory_size=10)
    memnet = model.MemoryNetwork(num_actions=featurizer.num_actions(), utterance_len=featurizer.feature_len(),
                                 embedding_size=100, mem_size=10, hops=2, keep_prob=0.8, clip_norm=1.)
    highest_dev_acc = 0
    chances2improve = 5
    stop = False
    for epoch in range(40):
        if stop:
            break
        batch_indexes = list(batch_indexes)
        trn_accuracies = []
        for i, (b_start, b_end) in enumerate(batch_indexes):
            pred, loss = memnet.train_step(history_batch=trn_history[b_start:b_end],
                                           query_batch=trn_query[b_start:b_end],
                                           label_batch=trn_label[b_start:b_end])
            accuracy = memnet.sess.run(memnet.accuracy, feed_dict={memnet.history: trn_history[b_start:b_end],
                                                                   memnet.queries: trn_query[b_start:b_end],
                                                                   memnet.labels: trn_label[b_start:b_end],
                                                                   memnet.keep_prob: 1})
            if i % 100 == 0:
                logging.info('epoch: {}\tbatch: {}\tloss: {}\taccuracy:{}'.format(epoch, i, loss, accuracy))
            trn_accuracies.append(accuracy)
        dev_accuracies, dev_losses = [], []
        for i, (b_start, b_end) in enumerate(dev_batch_indexes):
            _, dev_loss = memnet.train_step(history_batch=dev_history[b_start:b_end],
                                            query_batch=dev_query[b_start:b_end],
                                            label_batch=dev_label[b_start:b_end])
            dev_accuracy = memnet.sess.run(memnet.accuracy,
                                           feed_dict={memnet.history: dev_history[b_start:b_end],
                                                      memnet.queries: dev_query[b_start:b_end],
                                                      memnet.labels: dev_label[b_start:b_end],
                                                      memnet.keep_prob: 1})
            dev_accuracies.append(dev_accuracy)
            dev_losses.append(dev_loss)
        dev_acc = mean(dev_accuracies)
        if dev_acc > highest_dev_acc:
            highest_dev_acc = dev_acc
            chances2improve = 5
            memnet.persist('misc_experiments/ensemble/memnet/persisted/')
        else:
            chances2improve -= 1
            if chances2improve == 0:
                logger.info(
                    'no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                stop = True
        logging.info('epoch: {}\tdev loss: {}\tdev accuracy: {}\ttrain accuracy: {}'.format(
            epoch,
            mean(dev_losses),
            dev_acc,
            mean(trn_accuracies)
        ))


def stacking_memnet_test():
    from data.feature_factory import T6Featurizer
    from numpy import argmax
    from fabot.custom.memnet import model
    import numpy as np

    def pad_p(p):
        padding = np.array([[0] * (20 - p.shape[1])])
        return np.concatenate((padding, p), axis=1)

    def bot_prev_utter(story, turn, prev_pred):
        if turn == 0:
            return ''
        else:
            return story[turn - 1]['bot']

    features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': True, 'use_intent': False, 'use_nlu_entity_extractor': True,
                'use_entities': True, 'use_context': True}
    featurizer = T6Featurizer(**features)
    p_hist = []
    memnet = model.MemoryNetwork.load('misc_experiments/ensemble/memnet/persisted/')
    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    tst_file = BABI_T6_TST_FILE
    total_turns = 11237
    total_dialogs = 1117
    for story in BabiReader.babi_dialogue_iterator(tst_file):
        featurizer.reset()
        story_results = []
        dialog_act_matches, dialog_literal_matches = 0, 0
        h = []
        prev_pred = ''  # initial value for the previous prediction
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'],
                                     prev_bot_text=bot_prev_utter(story, i, prev_pred), turn=i)
            prediction = memnet.prediction(history=h if len(h) > 0 else [[0] * featurizer.feature_len()],
                                           query=x)
            p = memnet.sess.run(memnet.p, feed_dict={
                memnet.history: [h if len(h) > 0 else [[0] * featurizer.feature_len()]],
                memnet.queries: [x],
                memnet.keep_prob: 1})
            p_hist.append(pad_p(p))
            turn_results = dict()
            turn_results['human'] = turn['human']
            turn_results['target'] = turn['bot']
            actual_da = featurizer.get_bot_act(turn['bot'])
            predicted_da = featurizer.id2act(argmax(prediction))
            prev_pred = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
            turn_results['actual'] = prev_pred
            turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                     string=turn_results['target']) is not None
            turn_results['act_match'] = actual_da == predicted_da
            story_results.append(turn_results)

            h.append(x)

            dialog_act_matches += int(turn_results['act_match'])
            dialog_literal_matches += int(turn_results['literal_match'])
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
        results.append(story_results)
    with open('misc_experiments/ensemble/memnet/results.json', 'w') as fh:
        json.dump(results, fh, indent=2)
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_act_matches, total_turns, total_act_matches / total_turns, perfect_act_dialogs, total_dialogs,
                                        perfect_act_dialogs / total_dialogs))
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(
        total_literal_matches, total_turns, total_literal_matches / total_turns, perfect_literal_dialogs,
        total_dialogs,
                                            perfect_literal_dialogs / total_dialogs))
    memnet.sess.close()
    p_hist = np.array(p_hist).squeeze()
    print(np.mean(p_hist, axis=0))


def stacking_lstm_train():
    from data.feature_factory import T6Featurizer
    from fabot.custom.lstm.model import CustomLSTM
    import tensorflow as tf
    from numpy.random import seed, shuffle

    def format_lstm_data(stories, featurizer):
        data = []
        for story in stories:
            dialog = []
            for i, turn in enumerate(story):
                x = featurizer.featurize(user_text=turn['human'], prev_bot_text='' if i == 0 else story[i-1]['bot'], turn=i)
                dialog.append({'x': np.array(x, dtype=np.float32), 'y': featurizer.get_bot_utterance_act_id(turn['bot']),
                               'e': copy(featurizer.slot_values)})
            featurizer.reset()
            data.append(dialog)
        return data

    seed(42)
    stories = []
    for filename in [BABI_T6_TRN_FILE, BABI_T6_DEV_FILE]:
        for story in BabiReader.babi_dialogue_iterator(filename):
            stories.append(story)
    shuffle(stories)
    features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True,
                'use_embeddings': True, 'use_intent': False, 'use_nlu_entity_extractor': True,
                'use_entities': True, 'use_context': True}
    featurizer = T6Featurizer(**features)
    print('formatting training data')
    trn_dialogs = format_lstm_data(stories=stories[:int(len(stories) * .4)], featurizer=featurizer)
    print('formatting dev data')
    dev_dialogs = format_lstm_data(stories=stories[int(len(stories) * .4):int(len(stories) * .5)], featurizer=featurizer)

    num_actions = T6Featurizer.num_actions()
    input_dim = featurizer.feature_len()
    hidden_size = 128
    epochs = 35
    clip_norm = 1.
    logging.info(
        'starting training\nConfig:\nactions: {}\ninput_dim: {}\nhidden_size: {}\nepochs: {}\ngradient clip '
        'norm: {}\n'.format(num_actions, input_dim, hidden_size, epochs, clip_norm))
    print('formatting training data')
    model = CustomLSTM(input_dim=input_dim, hidden_size=hidden_size, num_actions=num_actions)

    optimizer = tf.train.AdadeltaOptimizer(0.1)

    grads, vars = zip(*optimizer.compute_gradients(model.loss))
    grads_clipped, _ = tf.clip_by_global_norm(grads, clip_norm=clip_norm)
    train_op = optimizer.apply_gradients(zip(grads_clipped, vars))

    model.sess.run(tf.global_variables_initializer())
    total_turns = sum([len(dialog) for dialog in trn_dialogs])
    dev_total_turns = sum([len(dialog) for dialog in dev_dialogs])
    highest_dev_matches = 0
    chances2improve = 5
    stop = False
    for epoch in range(epochs):
        if stop:
            break
        total_loss = 0
        total_matches = 0
        perfect_dialogs = 0
        for di, dialog in enumerate(trn_dialogs):
            dialog_matches = 0
            model.reset_conversation_state()
            for turn in dialog:
                pred, loss = model.train_step(featurized_turn=turn['x'], action=turn['y'],
                                              action_mask=[1] * num_actions, train_op=train_op)
                total_loss += loss
                dialog_matches += int(pred == turn['y'])
            total_matches += dialog_matches
            perfect_dialogs += int(dialog_matches == len(dialog))
        logging.info('epoch: {}\ttrn loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({:.2%})'.format(
            epoch, total_loss, total_matches, total_turns, total_matches / total_turns, perfect_dialogs,
            len(trn_dialogs),
                                                           perfect_dialogs / len(trn_dialogs)))
        # evaluate in dev
        dev_total_loss = 0
        dev_total_matches = 0
        dev_perfect_dialogs = 0
        for dialog in dev_dialogs:
            dev_dialog_matches = 0
            for turn in dialog:
                pred = model.prediction(features=turn['x'])
                dev_total_loss += loss
                dev_dialog_matches += int(pred == turn['y'])
            dev_total_matches += dev_dialog_matches
            dev_perfect_dialogs += int(dev_dialog_matches == len(dialog))
        logging.info('dev loss: {}\taccuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({:.2%})'.format(
            dev_total_loss, dev_total_matches, dev_total_turns, dev_total_matches / dev_total_turns,
            dev_perfect_dialogs, len(dev_dialogs), dev_perfect_dialogs / len(dev_dialogs)))
        if dev_total_matches >= highest_dev_matches:
            highest_dev_matches = dev_total_matches
            chances2improve = 5
            # model.persist('misc_experiments/lstm_nocontext/persisted/')
            model.persist('misc_experiments/ensemble/lstm/persisted/')
        else:
            chances2improve -= 1
            if chances2improve == 0:
                logger.info(
                    'no improvement in dev in more the last 5 epochs, stopping now with the best model so far')
                stop = True


def stacking_ensemble_train():
    from data.feature_factory import T6Featurizer
    from fabot.custom.memnet.model import MemoryNetwork
    from fabot.custom.lstm.model import CustomLSTM
    from fabot.custom.ensemble.model import CustomEnsemble
    from os.path import isfile
    import pickle
    from keras.utils import to_categorical
    from keras.callbacks import BaseLogger, EarlyStopping
    from numpy.random import seed, shuffle
    seed(42)
    features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True, 'use_embeddings': True,
                'use_intent': False, 'use_nlu_entity_extractor': True, 'use_entities': True,
                'use_context': True}
    featurizer = T6Featurizer(**features)
    num_actions = T6Featurizer.num_actions()
    memnet = MemoryNetwork.load('misc_experiments/ensemble/memnet/persisted/')
    lstm = CustomLSTM.load('misc_experiments/ensemble/lstm/persisted/')
    ensemble = CustomEnsemble(models=[memnet, lstm], num_actions=num_actions, policy='learned')
    # ensemble.train_t6(trn_filename=BABI_T6_TRN_FILE, featurizer=featurizer, epochs=35,
    #                   dev_filename=BABI_T6_DEV_FILE)

    def format_babi_data(ensemble, featurizer):
        """
        produces bAbI data in a format suitable for the memory network. Each conversation provides as many training examples
        as turns.
        :param filename: bAbI conversation filename
        :param featurizer: featurizer object
        :return: List of dialogues, each dialogue is a sequence of training examples (turns). A turn is a dict with keys:
        x: List of floats, a featurized turn
        y: int, id of the target bot action
        e: Dictionary with the value of each entity at that point in the conversation (None, for those with no value set)
        """
        stories = []
        for filename in [BABI_T6_TRN_FILE, BABI_T6_DEV_FILE]:
            for story in BabiReader.babi_dialogue_iterator(filename):
                stories.append(story)
        shuffle(stories)

        x, y, e = [], [], []
        for si, story in enumerate(stories):
            logger.info('story {}'.format(si))
            for i, turn in enumerate(story):
                f = featurizer.featurize(user_text=turn['human'], prev_bot_text='' if i == 0 else story[i - 1]['bot'],
                                         turn=i)
                preds = np.array([])
                for model in ensemble.models:
                    preds = np.concatenate((preds, model.predict_turn(f)))
                x.append(preds)
                y.append(featurizer.get_bot_utterance_act_id(turn['bot']))
                e.append(copy(featurizer.slot_values))
            for m in ensemble.models:
                m.reset_conversation_state()
            featurizer.reset()
        return np.array(x), np.array(y), e

    def load_data(ensemble, featurizer, saved_filename):
        if isfile(saved_filename):
            with open(saved_filename, 'rb') as fh:
                x, y, _ = pickle.load(fh)
        else:
            logger.info('no saved data found. Building it now')
            x, y, e = format_babi_data(ensemble, featurizer)
            with open(saved_filename, 'wb') as fh:
                pickle.dump((x, y, e), fh)
                logger.info('successfully saved data at {}'.format(saved_filename))
        return x, y

    x, y = load_data(ensemble, featurizer, 'misc_experiments/ensemble/ensemble_t6_data.pickle')
    x_trn, y_trn = x[int(len(x)*.5):int(len(x)*.9)], y[int(len(x)*.5):int(len(x)*.9)]
    x_dev, y_dev = x[int(len(x)*.9):], y[int(len(x)*.9):]
    y_trn = to_categorical(np.array(y_trn), num_classes=num_actions)
    y_dev = to_categorical(y_dev, num_classes=num_actions)
    ensemble.ensemble.fit(x_trn, y_trn, epochs=35, verbose=2, validation_data=(x_dev, y_dev),
                          callbacks=[BaseLogger(),
                                     EarlyStopping(monitor='val_acc', patience=5)])
    model_json = ensemble.ensemble.to_json()
    with open('misc_experiments/ensemble/persisted/model.json', "w") as json_file:
        json_file.write(model_json)
    ensemble.ensemble.save_weights('misc_experiments/ensemble/persisted/model.h5')
    logger.info('successfully persisted ensemble at {}'.format('misc_experiments/ensemble/persisted/'))


def stacking_ensemble_test():
    from data.feature_factory import T6Featurizer
    from fabot.custom.memnet.model import MemoryNetwork
    from fabot.custom.lstm.model import CustomLSTM
    from fabot.custom.ensemble.model import CustomEnsemble
    from numpy import argmax
    features = {'use_bow': True, 'use_turn': True, 'use_bot_utter': True, 'use_embeddings': True,
                'use_intent': False, 'use_nlu_entity_extractor': True, 'use_entities': True,
                'use_context': True}
    featurizer = T6Featurizer(**features)
    memnet = MemoryNetwork.load('misc_experiments/ensemble/memnet/persisted/')
    lstm = CustomLSTM.load('misc_experiments/ensemble/lstm/persisted/')
    ensemble = CustomEnsemble(models=[memnet, lstm], num_actions=T6Featurizer.num_actions(),
                              policy='learned')
    ensemble.load('misc_experiments/ensemble/persisted/')
    results = []
    total_act_matches, total_literal_matches = 0, 0
    perfect_act_dialogs, perfect_literal_dialogs = 0, 0
    total_turns = 11237
    total_dialogs = 1117
    for story in BabiReader.babi_dialogue_iterator(BABI_T6_TST_FILE):
        featurizer.reset()
        story_results = []
        dialog_act_matches, dialog_literal_matches = 0, 0
        for i, turn in enumerate(story):
            x = featurizer.featurize(user_text=turn['human'], prev_bot_text='' if i == 0 else story[i - 1]['bot'],
                                     turn=i)
            prediction = ensemble.ensemble_predict(x)

            turn_results = dict()
            turn_results['human'] = turn['human']
            turn_results['target'] = turn['bot']
            actual_da = featurizer.get_bot_act(turn['bot'])
            predicted_da = featurizer.id2act(argmax(prediction))
            turn_results['actual'] = featurizer.act2pattern(predicted_da)[1].format(**featurizer.slots())
            turn_results['literal_match'] = re.match(pattern=turn_results['actual'],
                                                     string=turn_results['target']) is not None
            turn_results['act_match'] = actual_da == predicted_da
            story_results.append(turn_results)

            dialog_act_matches += int(turn_results['act_match'])
            dialog_literal_matches += int(turn_results['literal_match'])
        total_act_matches += dialog_act_matches
        total_literal_matches += dialog_literal_matches
        perfect_act_dialogs += int(dialog_act_matches == len(story))
        perfect_literal_dialogs += int(dialog_literal_matches == len(story))
        results.append(story_results)
        for m in ensemble.models:
            m.reset_conversation_state()
    with open('misc_experiments/ensemble/tst_t6_ensemble_offline_results.json', 'w') as fh:
        json.dump(results, fh, indent=2)
    logging.info('test act match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.format(total_act_matches, total_turns,
                                                                                total_act_matches / total_turns,
                                                                                perfect_act_dialogs, total_dialogs,
                                                                                perfect_act_dialogs / total_dialogs)
                 )
    logging.info('test literal match results:\n'
                 'accuracy: {}/{} ({:.2%})\tperfect dialogs: {}/{} ({})'.
                 format(total_literal_matches, total_turns, total_literal_matches / total_turns,
                        perfect_literal_dialogs, total_dialogs, perfect_literal_dialogs / total_dialogs))


def display_t6_memnet_p_context():
    # labels, values_t6_tst = get_freqs(task=6, trn=False)
    # _, values_t6_trn = get_freqs(task=6, trn=True)
    p_context = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1.44866577e-34, 1.88568793e-29, 1.47498448e-23, 7.87984705e-19,
                 1.14565658e-14, 5.32715478e-11, 4.21298652e-08, 7.69682170e-06, 4.75022943e-04, 2.68702509e-02,
                 9.72646988e-01]
    p_no_cont = [0, 0, 0, 0, 0, 2.94346016e-35, 9.65242126e-31, 4.54206725e-26, 1.42268184e-21, 2.53403762e-18,
                 1.03974982e-14, 1.28936978e-11, 4.01998784e-09, 6.32114176e-07, 2.03698379e-05, 6.56894987e-04,
                 5.61347250e-03, 2.92208966e-02, 1.21911612e-01, 8.42576117e-01]
    # counter_t6_tst = get_freqs(task=5, trn=False)
    # counter_t6_trn = get_freqs(task=5, trn=True)
    # labels = list(set(counter_t6_trn.keys()) | set(counter_t6_tst.keys()))
    # values_t6_tst = [counter_t6_tst[l] for l in labels]
    # values_t6_trn = [counter_t6_trn[l] for l in labels]
    # values_t6_trn = np.array(values_t6_trn) / sum(values_t6_trn)
    # values_t6_tst = np.array(values_t6_tst) / sum(values_t6_tst)
    # print('kl divergence: {}'.format(entropy(values_t6_trn, values_t6_tst, base=2)))
    x = np.arange(20, 0, -1)
    plt.bar(x - 0.2, p_context, color='b', align='center', width=0.4, label='with context')
    plt.bar(x + .2, p_no_cont, color='r', align='center', width=0.4, label='without context')
    plt.legend()
    plt.xticks(x, x)
    plt.xlabel('Turns ago')
    plt.ylabel('Allocated attention')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # display_babi_bot_freqs()
    # plot_request_confusion_matrix()
    # produce_dstc2_rasa_nlu_file(synonyms)
    # evaluate_from_file()
    # compute_accuracy_from_file()
    # print_scarse_traindata_degradation()
    # make_kb_t5oovrestaurants_file()
    # validate_t5oovkb_sentences()
    # test_ner()
    # mem_size_train()
    # mem_size_test()
    # memnet_t5_pcheck_train()
    # memnet_t5_pcheck_test()
    # lstm_t6_nocontext_train()
    # lstm_t6_nocontext_test()
    # stacking_memnet_train()
    # stacking_memnet_test()
    # stacking_lstm_train()
    # stacking_ensemble_train()
    # stacking_ensemble_test()
    display_t6_memnet_p_context()
