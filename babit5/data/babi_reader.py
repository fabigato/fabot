from copy import deepcopy
import re
import argparse
import os.path
import json

user_das = {
    'greet': [
        '^good morning$',
        '^hello$',
        '^hi$'
    ],
    'inform': [
        '^i love (?P<cuisine>\w+) food$',
        '^(?P<cuisine>\w+) please$',
        '^i am looking for a (?P<price>\w+) restaurant$',  # watchout: not totally sure only price can go there
        '^(i\'d like to book a table|may i have a table|instead could it be|actually i would prefer|'
        'can you make a restaurant reservation|can you book a table)?'
        '(( ?with (?P<cuisine>\w+) (cuisine|food))?( ?in a (?P<price>\w+) price range)?'
        '( ?for (?P<number>\w+)( people)?)?( ?in (?P<location>\w+))?)+( please)?$',
        '^we will be (?P<number>\w+)$'
    ],
    'deny': [
        '^no$',
        '^no this does not work for me$',
        '^do you have something else$',
        '^no i don\'t like that$'
    ],
    'affirm': [
        '^it\'s perfect$',
        '^i love that$',
        '^let\'s do it$',
        '^that looks great$'
    ],
    'request_phone': [
        '^may i have the phone number of the restaurant$',
        '^what is the phone number of the restaurant$',
        '^do you have its phone number$'
    ],
    'request_address': [
        '^may i have the address of the restaurant$',
        '^do you have its address$',
        '^can you provide the address$'
    ],
    'thankyou': [
        '^thanks$',
        '^thank you$',
        '^you rock$'
    ],
    'bye': [
        '^no thank you$',
        '^no thanks$'
    ],
    'silence': [
        '^<SILENCE>$'
    ]
}
for da in user_das:
    user_das[da] = [re.compile(pattern) for pattern in user_das[da]]


bot_das = {
    'give_phone': [
        '^here it is \w+phone$'
    ],
    'give_address': [
        '^here it is \w+address$'
    ],
    'suggest_restaurant': [
        '^what do you think of this option: \w+$'
    ],
    'announce_search': [
        '^ok let me look into some options for you$'
    ],
    'request_updates': [
        '^sure is there anything else to update$'
    ],
    'announce_keep_searching': [
        '^sure let me find an other option for you$'
    ],
    'api_call': [
        '^api_call \w+ \w+ \w+ \w+$'
    ],
    'reserve': [
        '^great let me do the reservation$'
    ],
    'greet': [
        '^hello what can i help you with today$'
    ],
    'on_it': [
        '^i\'m on it$'
    ],
    'ask_location': [
        '^where should it be$'
    ],
    'ask_number_of_people': [
        '^how many people would be in your party$'
    ],
    'ask_price': [
        '^which price range are looking for$'
    ],
    'ask_cuisine': [
        '^any preference on a type of cuisine$'
    ],
    'ask_anything_else': [
        '^is there anything i can help you with$'
    ],
    'bye': [
        '^you\'re welcome$'
    ]
}


for da in bot_das:
    bot_das[da] = [re.compile(pattern) for pattern in bot_das[da]]


def get_user_act(text):
    """
    Determines the dialog act of a bAbI t5 user utterance
    :param text: user utterance
    :return: da of the utterance (str) or None if no match found
    """
    for act in user_das:
        for pattern in user_das[act]:
            match = pattern.search(text)
            if match:
                return act, [{"start": match.span(ent)[0], "end": match.span(ent)[1], "value": val, "entity": ent}
                             for ent, val in match.groupdict().items() if val]
    return None


def get_bot_act(text):
    """
    Determines the dialog act of a bAbI t5 bot utterance
    :param text: bot utterance
    :return: da of the utterance (str) or None if no match found
    """
    for act in bot_das:
        for pattern in bot_das[act]:
            if pattern.search(text):
                return act
    return None


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


def produce_nlu_training_file(input_filename, output_filename):
    result = {"rasa_nlu_data": {"common_examples": [], "entity_examples": [], "intent_examples": []}}
    for story in babi_dialogue_iterator(input_filename):
        for turn in story:
            text = turn['human']
            intent, entities = get_user_act(text)
            result["rasa_nlu_data"]["common_examples"].append({"text": text, "intent": intent, "entities": entities})
    with open(output_filename, 'w') as output_fh:
        json.dump(result, output_fh, indent=2)


def rasafy(intent, entities):
    if entities:
        return intent + '{' + ', '.join(['"{}": "{}"'.format(e['entity'], e['value']) for e in entities]) + '}'
    else:
        return intent


def produce_dialog_training_file(input_filename, output_filename, action_prefixes=None):
    action_prefixes = {action: '' for action in bot_das} if not action_prefixes else action_prefixes
    with open(output_filename, 'w') as output_fh:
        for i, story in enumerate(babi_dialogue_iterator(input_filename)):
            output_fh.write('## {}'.format(i) + '\n')
            for turn in story:
                intent, entities = get_user_act(turn['human'])
                bot_says = get_bot_act(turn['bot'])
                output_fh.write('* ' + rasafy(intent, entities) + '\n')
                output_fh.write(' - ' + action_prefixes[bot_says] + bot_says + '\n')
            output_fh.write('\n')


def _get_args():
    parser = argparse.ArgumentParser(
        description='produce Rasa format training files')
    parser.add_argument(
        'task',
        choices=["nlu", "dialog"],
        help="nlu: produce nlu training file\ndialog: produce keras policy training file")
    parser.add_argument('--input', type=str, help='input file name')
    parser.add_argument('--output', type=str, help='output file name')
    parser.add_argument('--utter-prefixes', action='store_true', default=False)
    return parser.parse_args()


def _basic_checks(args):
    if args.task not in ['nlu', 'dialog']:
        raise ValueError('invalid value for argument task: {}\nMust be either nlu or dialog'.format(args.task))
    if not args.input:
        raise Exception('argument --input is mandatory')
    if not os.path.isfile(args.input):
        raise FileNotFoundError('file {} does not exist'.format(args.input))
    if not args.output:
        raise Exception('argument --output is mandatory')


if __name__ == '__main__':
    args = _get_args()
    _basic_checks(args)
    if args.task == "nlu":
        produce_nlu_training_file(args.input, args.output)
    elif args.task == "dialog":
        prefixes = {action: 'utter_' for action in bot_das} if args.utter_prefixes else None
        produce_dialog_training_file(args.input, args.output, prefixes)
