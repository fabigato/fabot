from unittest import TestCase
import data.dstc2_reader as processor
from data.dstc2_reader import BOT_DAS as bot_das
from json import load as json_load
from globals import DSTC2_DATA_PATH, BABI_PATH
import re
from data.babi_reader import BabiReader
from os.path import join
# from data.babi_reader import BabiComparatorV2


class TestDialogueProcessor(TestCase):
    def test_act_to_rasa(self):
        test_cases = [
            {
                'dstc2': 'inform(pricerange=moderate,area=north)',
                'rasa': 'inform{"pricerange": "moderate", "area": "north"}'
            },
            {
                'dstc2': 'inform()',
                'rasa': 'inform'
            }
        ]
        for test in test_cases:
            self.assertEqual(processor.act_to_rasa(test['dstc2']), test['rasa'])

    def test_get_bot_da(self):
        tests = [
            {  # test 1: all acts are same
                'X':
                    [
                        {'act': 'only_value_present'},
                        {'act': 'only_value_present'},
                        {'act': 'only_value_present'}
                    ],
                'Y': 'only_value_present'
            },
            {  # test 2: only one option
                'X':
                    [
                        {'act': 'only_act'}
                    ],
                'Y': 'only_act'
            },
            {  # test 3: only inform and offer acts available
                'X':
                    [
                        {'act': 'inform'},
                        {'act': 'offer'},
                        {'act': 'inform'},
                        {'act': 'inform'}
                    ],
                'Y': 'inform'
            },
            {  # test 4: only canthelp and canthelp.exception
                'X':
                    [
                        {'act': 'canthelp.exception'},
                        {'act': 'canthelp.exception'},
                        {'act': 'canthelp'},
                        {'act': 'canthelp.exception'}
                    ],
                'Y': 'canthelp'
            },
            {  # test 5: only impl-conf and request
                'X':
                    [
                        {'act': 'impl-conf'},
                        {'act': 'request'},
                        {'act': 'impl-conf'}
                    ],
                'Y': 'impl-conf'
            }
        ]
        error_tests = [
            [],  # error test 1: no das
            [{'act': 'impl-conf'}, {'act': 'inform'}],  # error test 2: impl-conf with something other than request
            # and also, inform with something other than offer
            [{'act': 'offer'}, {'act': 'other'}],  # error test 3: offer with something other than inform
            [{'act': 'canthelp'}, {'act': 'canthelp.exception'}, {'act': 'other'}]
            # error test 4: canthelp with canthelp.exception and something else
        ]
        for t in tests:
            self.assertEqual(processor.get_bot_da(t['X']), t['Y'])
        for t in error_tests:
            self.assertRaises(ValueError, processor.get_bot_da, t)

    def test__make_story(self):
        tests = [
            {
                'file': 'Mar13_S0A1/voip-b772dbf437-20130402_143019/',  # {'inform', 'reqalts'} => inform
                'label':
                    [
                        ('inform{"food": "swedish", "pricerange": "moderate"}', 'canthelp'),
                        ('inform{"food": "asian oriental"}', 'inform'),  # yippee noodle bar is a great restaurant
                        ('reqalts', 'reqmore'),  # h: more options? b: can I help you with something else?
                        ('request{"addr": "True", "phone": "True"}', 'inform'),  # bot ignores phone request
                        ('request{"phone": "True"}', 'inform'),
                        ('bye', 'bye')
                    ]
            },
            {
                'file': 'Mar13_S0A1/voip-fce37b0ccb-20130328_145418/',  # {affirm, inform} => include_filter
                'label':
                    [
                        ('include_filter{"pricerange": "moderate"}', )
                    ]
            }
        ]
        # check Mar13_S1A1/voip-ddcaad92a1-20130325_234956, two repeat errors from the bot
        # check Mar13_S1A0/voip-ddcaad92a1-20130325_234752, one null user input (cough)
        # check Mar13_S1A1/voip-d645d56d23-20130401_204424, starts with noise, then it should ignore that and delete the
        # following bot question
        for test in tests:
            with open(DSTC2_DATA_PATH + test['file'] + 'label.json', 'r') as label, \
                 open(DSTC2_DATA_PATH + test['file'] + 'log.json', 'r') as log:
                human_dic, bot_dic = json_load(label), json_load(log)
                story = processor._make_story(human_dic, bot_dic)
                self.assertEqual(story, test['label'])

    def test_all_da_values(self):
        from collections import Counter, defaultdict
        da_examples = defaultdict(list)
        das = ['request_pricerange_detailed', 'request_food_detailed', 'expl-conf', 'select', 'request_area_detailed']

        def collect_da_examples(human, bot, **kwargs):
            for bot_turn, human_turn in zip(bot['turns'], human['turns']):
                bot_da = processor.get_bot_da(bot_turn['output']['dialog-acts'])
                for da_of_interest in das:
                    if bot_da == da_of_interest:
                        da_examples[da_of_interest].append(bot_turn['output']['transcript'])
        processor.process_dstc2_files(process=collect_da_examples, path_prefix=DSTC2_DATA_PATH)
        for da in da_examples:
            da_examples[da] = Counter(da_examples[da])
        res = {
            'request_pricerange_detailed': [
                'There are \d+ restaurants serving [\w ]+ in the \w+ of town . What price range would you like?',  #
                'There are \d+ restaurants serving [\w ]+ food in any part of town . What price range would you'
                ' like?',  #
                'There are \d+ restaurants if you don\'t care about the area or the type of food . What price range '
                'would you like?',  #
                'There are \d+ restaurants in the \w+ of town serving any kind of food . What price range would you '
                'like?',  #
                'There are \d+ restaurants serving [\w ]+ food . What price range do you want?',  #
                'There are \d+ restaurants in all parts of town . What type of pricerange do you want?',  #
                'There are \d+ restaurants if you don\'t care about the food . What price range do you want?'  #
            ],
            'request_food_detailed': [
                'There are \d+ restaurants in the \w+ price range and the \w+ of town . What type of food would you '
                'like?',  #
                'There are \d+ restaurants in the \w+ of town . What type of food do you want?',  #
                'There are \d+ restaurants in the \w+ price range . What type of food do you want?',  #
                'There are \d+ restaurants in all parts of town . What type of food do you want?'  #
            ],
            'expl-conf': [
                'You are looking for a restaurant serving any kind of food right?',
                'You are looking for a [\w ]+ restaurant right?',
                'Did you say you are looking for a restaurant in the \w+ of town?',
                'Let me confirm , You are looking for a restaurant in the \w+ price range right?',
                'Let me confirm , You are looking for a restaurant and you dont care about the price range right?',
                'Ok , a restaurant in any part of town is that right?'
            ],
            'select': [
                'Sorry would you like something in the w+ or in the \w+',
                'Sorry would you like [\w ]+ or [\w ]+ food',
                'Sorry would you like [\w ]+ food or you dont care',
                'Sorry would you like the \w+ of town or you dont care',
                'Sorry would you like something in the \w+ price range or in the \w+ price range',
                'Sorry would you like something in the \w+ price range or you dont care',
                'Sorry would you like something in the \w+ or in the \w+'
            ],
            'request_area_detailed': [
                'There are  restaurants serving [\w ]+ food . What area do you want?',
                'There are  restaurants serving [\w ]+ in the \w+ price range . What area would you like?',
                'There are \d+ restaurants serving [\w ]+ in the \w+ price range . What area would you like?',
                'There are \d+ restaurants serving [\w ]+ food . What area do you want?',
                'There are \d+ restaurants if you don\'t care about the food . What area do you want?',
                'There are \d+ restaurants serving [\w ]+ in any price range. What area would you like?',
                'There are \d+ restaurants in the \w+ price range . What area do you want?'
            ]
        }
        for da in res:
            res[da] = [re.compile(pattern) for pattern in res[da]]
        for da in da_examples:
            for utterance in da_examples[da]:
                matches = [pattern.match(utterance) for pattern in res[da]]
                if not any(matches):
                    print('troublesome {}: {}'.format(da, utterance))

    def test_misc_dstc2_cases_checker(self):
        from collections import Counter
        import re
        """Meant only for debugging and finding out the behavior of dstc2 files"""
        conversation_qualities = []
        successes = []
        das = []
        user_acts = []
        bot_acts = []
        from collections import defaultdict
        human_act_combinations = defaultdict(list)
        bot_act_combinations = defaultdict(list)

        def is_known_user_da(da):
            # match expressions of the form function(list of key-value pairs), with the parameter list comma separated
            # and the values can be a single word or several words in between double quotes, space separated
            da_re = re.compile('\w+\((\w+=((\"\w+( \w+)*\")|(\w+))(,\w+=((\"\w+( \w+)*\")|(\w+)))*)*\)')
            request_re = re.compile('request\(\w+(,\w+)*\)')
            dontcare_act = 'inform(=dontcare)'
            thankyoubye = 'thankyou()|bye()'
            generic_match = da_re.match(da)
            return (generic_match is not None and da_re.match(da).span()[1] == len(da)) or \
                request_re.match(da) is not None or \
                da == dontcare_act or \
                da == thankyoubye or (da[:8] == "affirm()" and request_re.match(da[9:])) or \
                da[:16] == "negate()|reqalts" or \
                da[:18] == "inform(=dontcare)|" or \
                re.match('request\(\w+(,\w+)*,\w+=((\w+)|("\w+( \w+)*"))(,\w+=((\w+)|("\w+( \w+)*")))*\)', da) is not None or \
                da[:6] == "ack()|" or \
                da == "thankyou()|bye()" or \
                da[:11] == "thankyou()|"
        def is_known_case(semantics):
            return is_known_user_da(semantics['cam']) or \
                   ({'slots': [['this', 'dontcare']], 'act': 'inform'} in semantics['json'] and (len([None for jsondic in semantics['json'] if ['this', 'dontcare'] not in jsondic['slots']]) > 0))
        for label, log in processor.iter_dstc2_files(dstc2_data_path='../../data/trndev/dstc2/data'):
        # for label, log in data.data_processor.iter_dstc2_files_from_listfile(
        #         '../../data/trndev/dstc2/scripts/config/dstc2_dev.flist',
        #         '../../data/trndev/dstc2/data'):
            with open(label) as json_label, open(log) as json_log:
                label_dic, log_dic = json_load(json_label), json_load(json_log)
                # put your test code mostly here

                conversation_quality = label_dic['task-information']['feedback']['questionnaire'][0][1]
                success = label_dic['task-information']['feedback']['success']
                conversation_qualities.append(conversation_quality)
                successes.append(success)

                for bot_turn, human_turn in zip(log_dic['turns'], label_dic['turns']):
                    for da in human_turn['semantics']['json']:
                        user_acts.append(da['act'])
                    for da in bot_turn['output']['dialog-acts']:
                        bot_acts.append(da['act'])
                    bot_act_combinations[tuple((json['act'] for json in bot_turn['output']['dialog-acts']))].append(
                        (human_turn['semantics']['cam'], bot_turn['output']['dialog-acts'],
                         bot_turn['output']['transcript'], human_turn['transcription'], log))
                    human_act_combinations[tuple((json['act'] for json in human_turn['semantics']['json']))].append(
                        (human_turn['semantics']['cam'], human_turn['semantics']['json'],
                         bot_turn['output']['transcript'], human_turn['transcription'], label))

                    #if not is_known_case(human_turn['semantics']):
                    # if 'thankyou' in [jsondic['act'] for jsondic in human_turn['semantics']['json']] \
                    #         and 'bye' not in [jsondic['act'] for jsondic in human_turn['semantics']['json']]:
                    #for jsondic in
                    #if 'inform' in [act for jsondic in human_turn['semantics']['json'] for act in jsondic['act'] if 'dontcare' in [slot[1] for slot in jsondic['slots']]]:
                    #if ({'slots': [['this', 'dontcare']], 'act': 'inform'} in human_turn['semantics']['json'] and (len([None for jsondic in human_turn['semantics']['json'] if ['this', 'dontcare'] not in jsondic['slots']]) > 0)):
                    if 'reqalts' in [json['act'] for json in human_turn['semantics']['json'] if len(human_turn['semantics']['json']) > 1]:
                        print('troublesome da {} at {}\nwith acts {}\nbot text: {}\nhuman text:{}'.format(
                            human_turn['semantics']['cam'],
                            label,
                            human_turn['semantics']['json'],
                            bot_turn['output']['transcript'],
                            human_turn['transcription']))
                if len(log_dic['turns']) != len(label_dic['turns']):
                    print('different number of turns at {}'.format(label))
                    # this will never happen
                for turn in log_dic['turns']:
                    # use this loop if you need to check turn data

                    turn_index = turn['turn-index']
                    hasoffer = False
                    hasinform = False
                    hasnoselect = False
                    hascanthelpexception = False
                    hasimplconf = False
                    hasrequest = False
                    for da in turn['output']['dialog-acts']:
                        das.append(da['act'])
                        if da['act'] == 'welcomemsg':
                            welcome = True
                        if da['act'] == 'canthelp':
                            canthelp = True
                        if da['act'] == 'expl-conf':
                            canthelp = True
                        if da['act'] == 'offer':
                            hasoffer = True
                        if da['act'] == 'inform':
                            hasinform = True
                        if da['act'] == 'select':
                            hasnoselect = True
                        if da['act'] == 'canthelp.exception':
                            hascanthelpexception = True
                        if da['act'] == 'impl-conf':
                            hasimplconf = True
                        if da['act'] == 'request':
                            hasrequest = True
                        if da['act'] == 'affirm':
                            affirm = True
                        if da['act'] == 'reqmore':
                            reqmore = True
                        if da['act'] == 'confirm-domain':
                            confirmdomain = True
                        if da['act'] == 'repeat':
                            repeat = True
                    # if hasoffer ^ hasinform:
                    #    print('check {}, turn {}'.format(log, turn_index))
                    # if hasinform and not hasoffer:
                    #    print('check {}, turn {}'.format(log, turn_index))
                    # if not (hasinform and hasoffer) and len(turn['output']['dialog-acts']) > 1 and hasnoselect and \
                    #         not hascanthelpexception and not hasimplconf:
                    #     print('check {}, turn {}'.format(log, turn_index))
                    # if len(turn['output']['dialog-acts']) == 0:
                    #     print('wtf')
        qualities = Counter(conversation_qualities)
        print('quality counts:\n {}'.format(qualities))
        print('successes: {}'.format(Counter(successes)))
        print('das: {}'.format(Counter(das)))
        print('user acts: {}'.format(Counter(user_acts)))
                    # if hasimplconf and hasrequest and len(turn['output']['dialog-acts']) > 2:

    def test_all_bot_utterances(self):
        sentences_babi_all = set()
        for story in babi_dialogue_iterator(babi_filename=join(BABI_PATH, 'dialog-babi-task6-dstc2-tst.txt')):
            clean_story = BabiComparatorV2.story_cleaner(story)
            sentences_babi_all.update([turn['bot'] for turn in clean_story])
        # for da in bot_das:
        #     bot_das[da] = [re.compile(pattern) for pattern in bot_das[da]]
        for utterance in sentences_babi_all:
            matched = False
            for da in bot_das:
                matches = [pattern.match(utterance) for pattern in bot_das[da]]
                if any(matches):
                    matched = True
                    break
            if not matched:
                print('troublesome bAbI: {}'.format(utterance))

        sentences_dstc2_trn_dev = processor.collect_all_bot_utterances(path_prefix=DSTC2_DATA_PATH,
                                                                       only_success=False)
        for utterance in sentences_dstc2_trn_dev:
            matched = False
            for da in bot_das:
                matches = [pattern.match(utterance) for pattern in bot_das[da]]
                if any(matches):
                    matched = True
                    break
            if not matched:
                print('troublesome DSTC2: {}'.format(utterance))
