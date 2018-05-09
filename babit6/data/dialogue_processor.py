from os import listdir
from os.path import join
from json import load as json_load
import copy
import logging
from globals import RASA_TRAIN_PATH, DSTC2_TRN_DEV_DATA_PATH, DSTCT2_TRN_LIST_FILE
import re

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


BOT_DAS = {
            'welcome_msg': [
                '^Hello , welcome to the Cambridge restaurant system\?? (\. )?You can ask for restaurants by area , '
                'price range or food type \.'
            ],
            'repeat': [
                '^Sorry, I can\'t hear you$',
                '^Sorry I am a bit confused ; please tell me again what you are looking for \.$',
                '^Could you please repeat that\?$'
            ],
            'utter_request_food': [
                '^What kind of food would you like\?$'
            ],
            'utter_request_area': [
                '^What part of town do you have in mind\?$'
            ],
            'no_more_options': [
                '^(I am sorry|Sorry) but there is no other .*restaurant',
                # in the centre of town$', that matches your request
            ],
            'offer_phone': [
                '^The phone number of .+ is .+$',
                '.*Their phone number is .* \.$'
            ],
            'canthelp': [
                '^(Sorry|I am sorry but|I\'m sorry but) there is no(?! other) .*restaurant'
            ],
            'offer_restaurant': [
                '^.+ serves .+ food',  # in the \w+ price range',
                '^.+ is a nice (place|restaurant) in the \w+ of town',
                '^.+ is a great restaurant serving \w+ .+ food in the \w+ of town .$',
                '^.+ is a nice place in the \w+ of town serving tasty .+ food',
            ],
            'confirm_ask_price': [
                # '^There are restaurants serving .+ food in (the \w+|any part) of town .
                # What price range would you like\?$',
                # ^There are restaurants in all parts of town . What type of pricerange do you want\?$',
                # ^There are restaurants if you don\'t care about the area or the type of food . What price range
                # would you like?$',
                '^There are restaurants .+ What (type of )?price ?range (do you want|would you like)\?$'
            ],
            'confirm_ask_area': [
                # There are restaurants serving .+ food (in any price range)?. What area do you want?
                '^There are  ?restaurants .+ What area (do you want\?|would you like\?)$',
                '^There are  restaurants \. That area would you like\?$'
            ],
            'confirm_ask_food': [
                '^There are  ?restaurants .+ What type of food (do you want|would you like)\?$'
            ],
            'offer_postcode': [
                '^The post code of .+ is .+$'
            ],
            'offer_address': [
                '^(Sure , )?.+ is on .+$',
                '^The address of .* is .* \.$'
            ],
            'offer_pricerange': [
                '.+ is in the \w+ price range',
                '^The price range at .* is \w+$',
                '^The price range at .* is \w+ \.$'
            ],
            'confirm_food': [
                '^You are looking for a .*restaurant .*right\?$'
            ],
            'futile_offer_restaurant': [
                '.+ is a great restaurant$'
            ],
            'utter_offer_area': [
                '.+ is a nice place in the \w+ of town$',
                '.* is in the \w+ part of town \.$',
                '.* is in the \w+ ,'
            ],
            'confirm_summary': [
                '^Let me confirm , You are looking for a restaurant .* right\?$'  # only 32 times in test
                # all of them missed and still produces 49 false positives. That's the size of the price if removing
            ],
            'confirm_area': [
                '^Did you say you are looking for a restaurant in the \w+ of town\?$',
                '^Ok , a restaurant in any part of town is that right\?$'
            ],
            'utter_anything_else': [
                '^Can I help you with anything else\?$'
            ],
            'utter_bye': [
                '^ you are welcome$'
            ],
            'utter_select_price': [
                '^Would you like something in the cheap , moderate , or expensive price range\?$',
                '^Sorry would you like something in the \w+ price range or'
            ],
            'utter_select_food': [  # never observed in test data
                '^Sorry would you like .* or .* food\?$',
                '^Sorry would you like .* food or you dont care$'
            ],
            'utter_select_area': [
                '^Sorry would you like something in the \w+ or in the \w+$',
                'Sorry would you like the \w+ of town or you dont care$'
            ],
            'api_call': [
                '^api_call \w+ \w+ \w+$'
            ]
        }

for da in BOT_DAS:
    BOT_DAS[da] = [re.compile(pattern) for pattern in BOT_DAS[da]]


def iter_dstc2_files(dstc2_data_path='data/'):
    """Get an iterator over all the (label.json, log.json) file tuples from dstc2"""
    for folder in listdir(dstc2_data_path):
        for sub_folder in listdir(join(dstc2_data_path, folder)):
            yield (join(dstc2_data_path, folder, sub_folder, 'label.json'),
                   join(dstc2_data_path, folder, sub_folder, 'log.json'))


def iter_dstc2_files_from_listfile(list_file, path_prefix=''):
    from re import sub
    """Get all label and log json files listed in a file, one per line"""
    with open(list_file, 'r') as files:
        for path in files:
            path = sub(r'\n', '', path)
            yield (join(path_prefix, path, 'label.json'),
                   join(path_prefix, path, 'log.json'))


def act_to_rasa(act):
    """
    Converts a DSTC2 dialogue act to rasa format. Example conversions (DSTC2 -> Rasa):
    inform(pricerange=moderate,area=north) -> inform{"pricerange": "moderate", "area": "north"}
    inform() -> inform
    """
    output = act.split('(')[0]
    slots = act[:-1].split('(')[1].strip()  # get only the list of variables
    if slots != '':
        output += '{'
        pairs = slots.split(',')
        for i, pair in enumerate(pairs):
            slot, value = pair.split('=')
            output += '"' + slot + '": "' + value + '"'
            if i+1 < len(pairs):
                output += ', '
        output += '}'
    return output


def compress_semantics(semantics):
    """
    Make sure at most one instance of each intent is present. Combine their slots if more than one is found. E.g.
    [{'slots':[['cuisine', 'italian']], 'act':'inform'},
    {'slots':[], 'act':'other'},
    {'slots':[['price', 'cheap']], 'act':'inform'}]
    =>
    [{'slots':[['cuisine', 'italian'], ['price', 'cheap']], 'act':'inform'},
    {'slots':[], 'act':'other'}]
    :param semantics: semantics object to compress.
    List = [
        {'slots': [[key1, value1], ...], 'act': str},  # first act
        ...
        {'slots': [[key1, value1], ...], 'act': str}  # last act
    ]
    Do note, this list gets modified, so you might prefer to pass a copy if that is important
    :return a list with the same format as the original, but at most one act of each type in the original is present,
    with all the accumulated slots
    """
    compressed_semantics = []
    while len(semantics) > 0:
        intent = semantics.pop(0)
        same_intents = [same_intent for same_intent in semantics if same_intent['act'] == intent['act']]
        for same_intent in same_intents:
            intent['slots'] += same_intent['slots']
            semantics.remove(same_intent)
        compressed_semantics.append(intent)
    return compressed_semantics


def get_bot_da(text):
    """
    Extract the right Dialog Act uttered by the bot.
    :param text: bot transcript text
    :return: a str indicating the bot da
    """
    matched = False
    for da in BOT_DAS:
        matches = [pattern.match(text) for pattern in BOT_DAS[da]]
        if any(matches):
            if da == 'utter_select_food':  # appears only 44 times in trn/dev and 0 in tst
                return 'offer_restaurant'
                # return 'confirm_ask_food'
            # if da == 'utter_select_area':  # only 26 times in trn/dev, 0 in tst
            #     return 'confirm_ask_area'  # has similar behavior and is one of fabot's top sources of false negatives
            return da
    raise ValueError('unknown da: {}'.format(text))


def get_user_intent(semantics):
    """
    Determines the architecture specific user intent in rasa format given the utterance semantics from DSTC2.
    Rasa can only deal with one user intent per utterance, so whenever DSTC2 contains more than one user intent, it
    should be converted to only one. All observed combinations of user dialogue acts are considered in the following
    rules.
    Pre-process rules, by order of application:
    - {bye, ...} => {bye} (bye priority rule)
    - {(hello|thankyou|deny|ack), ...} => {...} (pre clean rule).
        Do note, they are deleted only when there is at least another act (not in this set) along.
        Deny observed with inform and reqalts only. With inform, the informables always correct the 'this' value, no
        need to do explicit correction.
    - {confirm(*informables1), confirm(*informables2)} => {inform(*informables1, *informables2)} (confirms2inform rule)
    - {x(*slots1), x(*slots2), ...} => {x(*slots1, *slots2), ...} (accumulation rule)
    (Inform precedence rules)
    - {reqalts, inform(*informables)} => {inform(*informables)}.
        reqalts slots are always empty
    - {ack, inform(*informables)} => {inform(*informables)}
    - {negate,reqalts,inform(*informables)} => {inform(*informables)}
    - {deny,inform(*informables)} => {inform(*informables)}
    - {affirm, inform(*informables)} => {inform(*informables)}
    Request fix:
    -{request(requestable1, requestable2, ...)} => request_requestable1, unless requestable1 in [signature, name] since
    those instances are too scarse and the bot never replies them right. Those are eliminated
    -{request(), ...} => {...}
    Map rules (evaluated only after preprocess rules):
    - {reqmore} => reqalts
    - {inform(this, *informables)} => {inform(*informables)}
    - {inform(*informables)} => inform(*informables)
    - {negate, inform(*informables)} => {correct(*informables)}
        clean all slots collected thus far. This inform should never contain the 'this' slot
    - {request(*requestables), inform(*informables)} => {request(*requestables, *informables)}
    - {negate, reqalts} => {reqalts}
    - {affirm, request(*requestables)} => {request(*requestables)}
    - {reqalts, deny} => {reqalts}
    Simple converstion rules:
    - {deny} => {negate}  omdat er is bijna geen deny
    - {ack} => {affirm}  omdat er is bijna geen ack
    (identity mappings)
    - {hello} => {hello}
    - {repeat} => {repeat}
    - {restart} => {restart}
    - {} => {null}
    - {confirm(*informables)}
    - {thankyou} => {thankyou}
    - {negate} => {negate}
    - {affirm} => {affirm}
    - {reqalts} => {reqalts}

    :param semantics: Dictionary as provided from DSTC2 label['turns']['semantics']['json']
    :return: string with the user intent in the architecture specific rasa format
    """
    def change_and_filter(semantics, oldname, newname=None):
        """Finds the act with oldname, replaces by newname and returns a list with only that semantic. If there
        are several semantics with oldname, only the first one will be considered. This should never be the case"""
        changed_semantics = next(semantic for semantic in semantics if semantic['act'] == oldname)
        if newname is not None:
            changed_semantics['act'] = newname
        return changed_semantics
    semantics = copy.deepcopy(semantics)
    for semantic in semantics:
        semantic['slots'] = [[slot[0], slot[1].replace(' ', '_').lower()] for slot in semantic['slots']]
    # bye priority rule
    if 'bye' in [semantic['act'] for semantic in semantics]:
        return {'act': 'bye', 'slots': []}
    # pre-cleanup rule (remove garbage intents provided there are others (e.g. {thankyou, ...} => {...}))]
    clean_semantics = [semantic for semantic in semantics
                       if semantic['act'] not in ['hello', 'thankyou', 'deny', 'ack']] \
        if len([semantic for semantic in semantics if semantic['act'] not in ['hello', 'thankyou', 'deny', 'ack']]) > 0\
        else semantics  # at any rate, we'll work with a copy of semantics
    # confirms2inform rule
    if all(semantic['act'] == 'confirm' for semantic in clean_semantics) and len(clean_semantics) > 1:
        clean_semantics = compress_semantics(clean_semantics)
        clean_semantics[0]['act'] = 'inform'
    # accumulation rule (ensure at most one of each intent is present. Combine their slots if more than one is found)
    compressed_semantics = compress_semantics(clean_semantics)

    # fix request by renaming its keys and giving them the True value
    for semantic in compressed_semantics:
        if semantic['act'] == 'request':
            # if 'name' in [slot[1] for slot in semantic['slots']]:
            #      print('got it')
            # request_signature and request_name are scarse and never answered correctly by the bot
            semantic['slots'] = [slot for slot in semantic['slots'] if slot[1] not in ['signature', 'name']]
            if semantic['slots']:  # if not empty
                semantic['act'] = 'request_' + semantic['slots'][0][1]  # take only the first slot to define the intent
                semantic['slots'] = []
            else:  # remove request from compressed_semantics
                compressed_semantics = [semantic for semantic in compressed_semantics if semantic['act'] != 'request']
    acts = sorted([intent['act'] for intent in compressed_semantics])
    # inform precedence rules (keep inform, drop the rest)
    if set(acts) in [{'reqalts', 'inform'}, {'ack', 'inform'}, {'negate', 'reqalts', 'inform'}, {'deny', 'inform'},
                     {'affirm', 'inform'}]:
        compressed_semantics = [semantic for semantic in compressed_semantics if semantic['act'] == 'inform']
        acts = ['inform']
    # map rules
    """basic sanity checks that can only be done after the user da was produced"""
    for j, semantic in enumerate(compressed_semantics):
        for i, (slot_name, slot_value) in enumerate(semantic['slots']):
            if slot_name == 'addr':  # our entity is called address, not addr
                compressed_semantics[j]['slots'][i][0] = 'address'
    if acts == ['hello']:  # {hello} => HELLO_ERROR
        return {'act': 'hello', 'slots': []}
    elif acts == ['repeat']:
        return {'act': 'repeat', 'slots': []}  # {repeat} => REPEAT_ERROR
    elif acts == ['restart']:  # {restart} => RESTART_ERROR
        return {'act': 'restart', 'slots': []}
    elif acts == []:  # [] => NULL_ERROR
        return {'act': 'null', 'slots': []}
    elif acts == ['reqmore']:  # {reqmore} => reqalts
        return change_and_filter(compressed_semantics, oldname='reqmore', newname='reqalts')
    elif acts == ['inform']:  # {inform(*informables)} => inform(*informables)
        return {'act': 'inform', 'slots': [slot for slot in compressed_semantics[0]['slots']
                                    if slot[0] != 'this']}
    elif acts == ['inform', 'negate']:  # {negate, inform(*informables)} = > {correct(*informables)}
        return change_and_filter(compressed_semantics, oldname='inform', newname='correct')
    elif len(acts) == 2 and acts[0] == 'inform' and 'request' in acts[1]:
        # {request(*requestables), inform(*informables)} => {request(*requestables, *informables)}
        requestables = next(semantic for semantic in compressed_semantics if 'request' in semantic['act'])['slots']
        result = change_and_filter(compressed_semantics, oldname="inform", newname=acts[1])
        result['slots'] = [slot for slot in result['slots'] if 'this' not in slot]  # 'this' not allowed here
        result['slots'] += requestables
        return result
    # elif acts == ['affirm', 'inform']:  # {affirm, inform(*informables)} => {inform(*informables)}
    #     for sem in compressed_semantics:
    #         sem['slots'] = [slot for slot in sem['slots'] if 'this' not in slot]
    #     return change_and_filter(compressed_semantics, oldname='inform', newname='inform')
    elif acts == ['negate', 'reqalts']:  # {negate, reqalts} => {reqalts}
        return {'act': 'reqalts', 'slots': []}
    elif len(acts) == 2 and acts[0] == 'affirm' and 'request' in acts[1]:  # {affirm, request(*requestables)} => {request(*requestables)}
        return next(semantic for semantic in compressed_semantics if 'request' in semantic['act'])
    elif acts == ['deny', 'reqalts']:  # {reqalts, deny} => {reqalts}
        return next(semantic for semantic in compressed_semantics if semantic['act'] == 'reqalts')
    elif len(acts) == 1:  # identity mappings
        # if 'request' in acts[0] and 'name' in [slot_name for slot_name, _ in compressed_semantics[0]['slots']]:
        #     # a weird case observed 3 times in training data: user asks for the name of the restaurant and it is
        #     # annotated as request rather than a confirm
        #     compressed_semantics[0]['act'] = 'confirm'
        if acts[0] == 'deny':  # {deny} => negate
            compressed_semantics[0]['act'] = 'negate'
        if acts[0] == 'ack':  # {ack} => affirm
            compressed_semantics[0]['act'] = 'affirm'
        return compressed_semantics[0]
    else:
        raise ValueError('unknown user act combination found: {}\nwith semantics:{}'.format(acts, semantics))


def _make_story(human, bot):
    """
    Produces a story compatible with rasa (i.e. only one human intend and robot action per turn), cleaning useless
    DSTC2 human utterances like hello, repeat or null
    :param human: human dictionary, the raw DSTC2 label.json file
    :param bot: bot dictionary, the raw DSTC2 log.json file
    :return: list of turns = [
        (bot_intent, human_utter),  # turn 1
        ...
        (bot_intent, human_utter),  # last turn
    ]
    Each intent is a string that includes all the arguments along with its name, in rasa format e.g.
    inform{"area": "south", "price": "moderate"}
    """
    b_utterances, h_utterances = [], []
    for bot_turn, human_turn in zip(bot['turns'], human['turns']):  # bot always start first
        bot_da = get_bot_da(bot_turn['output']['transcript'])  # else, take the current bot utter
        if bot_da == 'repeat':
            h_utterances.pop()  # delete last user utterance, since it was unclear
            # this bot da is also useless, later we check and discard it
        elif bot_da == 'welcome_msg':  # nothing to do, it gets deleted at the end. Why is this if even here?
            pass
        user_intent = get_user_intent(human_turn['semantics']['json'])
        if isinstance(user_intent, dict):  # normal intent, just convert to rasa string
            user_utter = user_intent['act']
            if len(user_intent['slots']) > 0:
                slot_name, slot_value = user_intent['slots'][0][0], user_intent['slots'][0][1]
                user_utter += '{{"{}": "{}"'.format(slot_name, slot_value)  # note {{
                for slot in user_intent['slots'][1:]:  # only if there are still more, to deal with the commas
                    slot_name, slot_value = slot[0], slot[1]
                    user_utter += ', "{}": "{}"'.format(slot_name, slot_value)
                user_utter += '}'
            if bot_da != 'repeat':
                b_utterances.append(bot_da)  # else, we only save the user utterance
            h_utterances.append(user_utter)
        else:
            raise ValueError('Unexpected user intent while building story: {}'.format(user_intent))
    b_utterances.pop(0)  # delete first welcome message
    b_utterances.append('utter_bye')  # add a final bye
    assert len(b_utterances) == len(h_utterances), "different number of bot and human utterances\nbot: {}\nhuman: {}".\
        format(b_utterances, h_utterances)
    return list(zip(h_utterances, b_utterances))


def process_dstc2_files(process, files_list=None, path_prefix='', only_success=False,
                        quality_filters=('strongly agree', 'agree', 'slightly agree', 'slightly disagree',
                                         'strongly disagree')):
    """
    Goes through dstc2 stories and executes a given function on each one of them
    :param process: callable with the code to execute on each story. It receives as parameters the dstc2 label json file
    as a dictionary, the log dictionary and the dstc2 path to this story.
    :param files_list: a file with the list of dstc files to consider (from dstc2 data folder, up to dialog folder,
    without json files). If ommited, all files are considered
    :param path_prefix: prefix to the dstc2 file paths
    :param only_success: consider only successful dialogs (label['task-information']['feedback']['success'] == True)
    :param quality_filters: consider only dialogs where the questionnaire was positive
    (label['task-information']['feedback']['questionnaire'][0][1] is in this iterable)
    :param output_file: name of the output file
    """
    files = iter_dstc2_files_from_listfile(files_list, path_prefix) if files_list else iter_dstc2_files(path_prefix)
    for label, log in files:
        with open(label) as json_label, open(log) as json_log:
            label_dic, log_dic = json_load(json_label), json_load(json_log)
            if only_success and not label_dic['task-information']['feedback']['success']:
                logger.warning('skipping unsuccessful dialogue: {}'.format(json_label))
                continue
            if label_dic['task-information']['feedback']['questionnaire'][0][1] not in quality_filters:
                logger.warning('skipping dialogue with unacceptable {} quality\nOnly values allowed: {}\nDialogue: {}'.
                               format(label_dic['task-information']['feedback']['questionnaire'][0][1],
                                      quality_filters, json_label))
                continue
            process(human=label_dic, bot=log_dic,
                    story_path=label.replace(path_prefix, '').replace('/Mar', 'Mar')[:-11])


def produce_rasa_file(files_list=None, path_prefix='', only_success=False,
                      quality_filters=('strongly agree', 'agree', 'slightly agree', 'slightly disagree',
                                       'strongly disagree'),
                      output_file='stories.md'):
    """
    Writes (or overwrites) the rasa format story file, from the dstc2 files (appending, in case file existed)
    :param files_list: a file with the list of dstc files to consider (from dstc2 data folder, up to dialog folder,
    without json files). If ommited, all files are considered
    :param path_prefix: prefix to the dstc2 file paths
    :param only_success: consider only successful dialogs (label['task-information']['feedback']['success'] == True)
    :param quality_filters: consider only dialogs where the questionnaire was positive
    (label['task-information']['feedback']['questionnaire'][0][1] is in this iterable)
    :param output_file: name of the output file
    """
    def process_story(human, bot, story_path):
        with open(output_file, 'a') as output:
            try:
                story = _make_story(human, bot)
                output.write('## ' + story_path + '\n')
                for turn in story:
                    output.write('* ' + turn[0] + '\n - ' + turn[1] + '\n')
                output.write('\n')
            except AssertionError as e:
                print('assertion error at story {}'.format(story_path))
    with open(output_file, 'w') as output:
        output.write('')  # just to clean it
    process_dstc2_files(process=process_story, files_list=files_list, path_prefix=path_prefix,
                        only_success=only_success, quality_filters=quality_filters)


def collect_all_bot_utterances(*args, **kwargs):
    """Collect all bot sentences in DSTC2. All arguments are passed to process_dstc2_files, except the process argument,
    which shouldn't be provided to this function
    :return: set with all sentences observed"""
    sentences = set()

    def sentences_collector(log_dic, *args, **kwargs):
        for turn in log_dic['turns']:
            sentences.add(turn['output']['transcript'])
    process_dstc2_files(process=sentences_collector, *args, **kwargs)
    return sentences


if __name__ == '__main__':
    produce_rasa_file(files_list=DSTCT2_TRN_LIST_FILE,
                      path_prefix=DSTC2_TRN_DEV_DATA_PATH, only_success=True,
                      output_file=RASA_TRAIN_PATH + 'stories.md')
    # produce_rasa_file(
    #                   path_prefix='data/test/dstc2/data/', only_success=True,
    #                   output_file='data/test/rasa/stories_test.md')
