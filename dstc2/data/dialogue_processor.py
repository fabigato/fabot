from os import listdir
from os.path import join
from json import load as json_load
import copy
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")


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


def _get_bot_da(das):
    """
    Extract the right Dialog Act uttered by the bot. These are the rules:
    accumulation rule:
    - {x(*slots1), x(*slots2), ...} => {x(*slots1, *slots2), ...}
    regular mappings
    - {welcomemsg} => WELCOME_ERROR
    - {repeat} => REPEAT_ERROR
    - {offer, inform} => offer_detailed
        search with current filters, offer one retrieved option listing all the filters used.
        e.g. 'thanh binh is a nice place in the west of town serving tasty vietnamese food'
    - {request(informable)} => request_informable
        one action per informable, except name. i.e. request_area, request_pricerange, request_food
    - {canthelp, canthelp.exception} => canthelp
        canthelp.exception clauses have no effect on output
    - {request(informable), impl-conf} => request_informable_detailed
        like request_informable, but lists the filters used
        e.g. 'There are  restaurants serving tuscan in the expensive price range . What area would you like?'
    identity mappings:
    {canthelp}
    {reqmore}
    {expl-conf}
    {select}
    {confirm-domain}
    {offer}
    :param das: a dialogue act list as present in the dstc2 log.json files (a list of dictionaries, each with an 'act'
    key. This comes from the log.json files, in log_turn['output']['dialog-acts'])
    :return: a str indicating the bot da
    """
    compressed_semantics = compress_semantics(das)
    acts = {da['act'] for da in compressed_semantics}
    if acts == {'welcomemsg'}:  # {welcomemsg} => WELCOME_ERROR
        return 'WELCOME_ERROR'
    elif acts == {'repeat'}:  # {repeat} => REPEAT_ERROR
        return 'REPEAT_ERROR'
    elif acts == {'offer', 'inform'}:  # {offer, inform} => offer_detailed
        return 'offer_detailed'
    elif acts == {'request'}:  # {request(informable)} => request_informable
        assert len(compressed_semantics[0]['slots']) == 1, 'request bot da with more than one informable:  {}'.\
            format(compressed_semantics)
        return 'request_' + compressed_semantics[0]['slots'][0][1]
    elif acts == {'canthelp', 'canthelp.exception'}:  # {canthelp, canthelp.exception} => canthelp
        return 'canthelp'
    elif acts == {'request', 'impl-conf'}:  # {request(informable), impl-conf} => request_informable_detailed
        request = next(semantic for semantic in compressed_semantics if semantic['act'] == 'request')
        assert len(request['slots']) == 1, 'request bot da with more than one informable:  {}'. \
            format(compressed_semantics)
        return 'request_' + request['slots'][0][1] + '_detailed'
    elif len(acts) == 1:  # identity mappings
        return list(acts)[0]
    else:
        raise ValueError('unknown bot da configuration: {}'.format(acts))


def _get_user_intent(semantics):
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

    Map rules (evaluated only after preprocess rules):
    - {hello} => HELLO_ERROR (useless utterance, remove all until next non useless human utterance)
    - {repeat} => REPEAT_ERROR
        user asks bot to repeat utterance. This should be deleted as well as bot utterance that triggered it
    - {restart} => RESTART_ERROR
    - {} => NULL_ERROR
        user didn't say anything (useful). Should be deleted as well as the bot utterance that triggered it
    - {reqmore} => reqalts
    - {inform(this, *informables)} => inform_dontcare(*informables)
    - {inform(*informables)} => inform(*informables)
    - {negate, inform(*informables)} => {correct(*informables)}
        clean all slots collected thus far. This inform should never contain the 'this' slot
    - {request(*requestables), inform(*informables)} => {query(*requestables, *informables)}
    - {affirm, inform(*informables)} => {include_filter(*informables)}
    - {negate, reqalts} => {reqalts}
    - {affirm, request(*requestables)} => {request(*requestables)}
    - {reqalts, deny} => {reqalts}
    (identity mappings)
    - {confirm(*informables)}
    - {request(*requestables)}
    - {thankyou} => {thankyou}
    - {negate} => {negate}
    - {affirm} => {affirm}
    - {deny} => {deny}
    - {ack} => {ack}
    - {reqalts} => {reqalts}

    :param semantics: Dictionary as provided from DSTC2 label['turns']['semantics']['json']
    :return: string with the user intent in the architecture specific rasa format
    """
    def change_and_filter(semantics, oldname, newname=None):
        """Finds the act with oldname, replaces by newname and returns a list with only that semantic"""
        changed_semantics = [semantic for semantic in semantics if semantic['act'] == oldname]
        assert len(changed_semantics) == 1
        if newname is not None:
            changed_semantics[0]['act'] = newname
        return changed_semantics[0]
    # bye priority rule
    if 'bye' in [semantic['act'] for semantic in semantics]:
        return {'act': 'bye', 'slots': []}
    # pre-cleanup rule (remove garbage intents provided there are others (e.g. {thankyou, ...} => {...}))]
    clean_semantics = [semantic for semantic in semantics
                       if semantic['act'] not in ['hello', 'thankyou', 'deny', 'ack']] \
        if len([semantic for semantic in semantics if semantic['act'] not in ['hello', 'thankyou', 'deny', 'ack']]) > 0\
        else copy.deepcopy(semantics)  # at any rate, we'll work with a copy of semantics
    # confirms2inform rule
    if all(semantic['act'] == 'confirm' for semantic in clean_semantics) and len(clean_semantics) > 1:
        clean_semantics = compress_semantics(clean_semantics)
        clean_semantics[0]['act'] = 'inform'
    # accumulation rule (ensure at most one of each intent is present. Combine their slots if more than one is found)
    compressed_semantics = compress_semantics(clean_semantics)
    acts = {intent['act'] for intent in compressed_semantics}
    assert len(compressed_semantics) == len(set(acts))  # reducing => at most one of each, set should remove nothing
    # inform precedence rules (keep inform, drop the rest)
    if acts in [{'reqalts', 'inform'}, {'ack', 'inform'}, {'negate', 'reqalts', 'inform'}, {'deny', 'inform'}]:
        compressed_semantics = [semantic for semantic in compressed_semantics if semantic['act'] == 'inform']
        acts = {'inform'}
    # map rules
    # first, fix request by renaming its keys and giving them the True value
    for semantic in compressed_semantics:
        if semantic['act'] == 'request':
            semantic['slots'] = [['requested_' + slot[1], "True"] for slot in semantic['slots']]
    if acts == {'hello'}:  # {hello} => HELLO_ERROR
        return 'HELLO_ERROR'
    elif acts == {'repeat'}:
        return 'REPEAT_ERROR'  # {repeat} => REPEAT_ERROR
    elif acts == {'restart'}:  # {restart} => RESTART_ERROR
        return 'RESTART_ERROR'
    elif acts == set():  # {} => NULL_ERROR
        return 'NULL_ERROR'
    elif acts == {'reqmore'}:  # {reqmore} => reqalts
        return change_and_filter(compressed_semantics, oldname='reqmore', newname='reqalts')
    elif acts == {'inform'} and 'this' in [slot[0] for semantic in compressed_semantics for slot in semantic['slots']]:
        # {inform(this, *informables)} => inform_dontcare(*informables)
        return {'act': 'inform_dontcare', 'slots': [slot for slot in compressed_semantics[0]['slots']
                                                    if slot[0] != 'this']}
    elif acts == {'inform'}:  # {inform(*informables)} => inform(*informables)
        return compressed_semantics[0]
    elif acts == {'negate', 'inform'}:  # {negate, inform(*informables)} = > {correct(*informables)}
        return change_and_filter(compressed_semantics, oldname='inform', newname='correct')
    elif acts == {'request', 'inform'}:
        # {request(*requestables), inform(*informables)} => {query(*requestables, *informables)}
        requestables = next(semantic for semantic in compressed_semantics if semantic['act'] == 'request')['slots']
        result = change_and_filter(compressed_semantics, oldname="inform", newname="query")
        result['slots'] = [slot for slot in result['slots'] if 'this' not in slot]  # 'this' not allowed here
        result['slots'] += requestables
        return result
    elif acts == {'affirm', 'inform'}:  # {affirm, inform(*informables)} => {include_filter(*informables)}
        return change_and_filter(compressed_semantics, oldname='inform', newname='include_filter')
    elif acts == {'negate', 'reqalts'}:  # {negate, reqalts} => {reqalts}
        return {'act': 'reqalts', 'slots': []}
    elif acts == {'affirm', 'request'}:  # {affirm, request(*requestables)} => {request(*requestables)}
        return next(semantic for semantic in compressed_semantics if semantic['act'] == 'request')
    elif acts == {'reqalts', 'deny'}:  # {reqalts, deny} => {reqalts}
        return next(semantic for semantic in compressed_semantics if semantic['act'] == 'reqalts')
    elif len(acts) == 1:  # identity mappings
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
    last_good_bot_utter = None
    for bot_turn, human_turn in zip(bot['turns'], human['turns']):  # bot always start first
        if last_good_bot_utter is not None:  # if we kept last bot utter, means we should skip the current
            bot_da = last_good_bot_utter
            last_good_bot_utter = None  # clean the flag
        else:
            bot_da = _get_bot_da(bot_turn['output']['dialog-acts'])  # else, take the current bot utter
            if bot_da == 'REPEAT_ERROR':
                h_utterances.pop()  # delete last user utterance, since it was unclear
                # this bot da is also useless, later we check and discard it
            elif bot_da == 'WELCOME_ERROR':
                pass
        user_intent = _get_user_intent(human_turn['semantics']['json'])
        if isinstance(user_intent, dict):  # normal intent, just convert to rasa string
            user_utter = user_intent['act']
            if len(user_intent['slots']) > 0:
                slot_name, slot_value = user_intent['slots'][0][0], user_intent['slots'][0][1]
                assert slot_name != 'this', 'a \'this\' argument detected: {}'.format(user_intent)
                assert slot_name != 'slot', 'a \'slot\' argument detected: {}'.format(user_intent)
                user_utter += '{{"{}": "{}"'.format(slot_name, slot_value)  # note {{
                for slot in user_intent['slots'][1:]:  # only if there are still more, to deal with the commas
                    slot_name, slot_value = slot[0], slot[1]
                    user_utter += ', "{}": "{}"'.format(slot_name, slot_value)
                user_utter += '}'
            if bot_da != 'REPEAT_ERROR':
                b_utterances.append(bot_da)  # else, we only save the user utterance
            h_utterances.append(user_utter)
        elif isinstance(user_intent, str):  # error signal that requires story correction
            if user_intent == 'HELLO_ERROR':  # user should never say just hi. Else, we remove it and the next bot utter
                last_good_bot_utter = bot_da
                continue
            elif user_intent == 'REPEAT_ERROR':  # useless, just skip this and bot repetition
                last_good_bot_utter = bot_da
                continue
            elif user_intent == 'NULL_ERROR':  # no intent, just skip this garbage and next bot utterance
                last_good_bot_utter = bot_da
                continue
            elif user_intent == 'RESTART_ERROR':  # clean all utterances until now
                h_utterances, b_utterances = [], []  # next bot reply will be deleted at the end, so user always starts
            else:
                raise ValueError('Unexpected user intent while building story: {}'.format(user_intent))
        else:
            raise ValueError('Unexpected user intent while building story: {}'.format(user_intent))
    b_utterances.pop(0)  # delete first welcome message
    b_utterances.append('bye')  # add a final bye
    assert len(b_utterances) == len(h_utterances), "different number of bot and human utterances\nbot: {}\nhuman: {}".\
        format(b_utterances, h_utterances)
    return list(zip(h_utterances, b_utterances))


def produce_rasa_file(files_list=None, path_prefix='', only_success=False, quality_filters=('strongly agree', 'agree',
                                                                                            'slightly agree',
                                                                                            'slightly disagree',
                                                                                            'strongly disagree'),
                      output_file='stories.md'):
    """
    Writes (or overwrites) the rasa format story file, from the dstc2 files
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
        with open(label) as json_label, open(log) as json_log, open(output_file, 'a') as output:
            label_dic, log_dic = json_load(json_label), json_load(json_log)
            if only_success and not label_dic['task-information']['feedback']['success']:
                logger.warning('skipping unsuccessful dialogue: {}'.format(json_label))
                continue
            if label_dic['task-information']['feedback']['questionnaire'][0][1] not in quality_filters:
                logger.warning('skipping dialogue with unacceptable {} quality\nOnly values allowed: {}\nDialogue: {}'.
                               format(label_dic['task-information']['feedback']['questionnaire'][0][1],
                                      quality_filters, json_label))
                continue
            output.write('## ' + label.replace(path_prefix, '').replace('/Mar', 'Mar')[:-11] + '\n')
            try:
                story = _make_story(label_dic, log_dic)
            except AssertionError as e:
                print('assertion error at story {}'.format(label))
            for turn in story:
                output.write('* ' + turn[0] + '\n - ' + turn[1] + '\n')
            output.write('\n')


if __name__ == '__main__':
    produce_rasa_file(files_list='trndev/dstc2/scripts/config/dstc2_train.flist', path_prefix='trndev/dstc2/data',
                      only_success=True, output_file='stories.md')
