from rasa_core.domain import TemplateDomain
import re
from src.custom_channels.bot_file_io import INPUT_SPLIT_SEPARATOR

IGNORE_REGEX = '\[IGNORE\]'
IGNORE_TOKEN = '[IGNORE]'
ANY_TOKEN = '[ANY]'


def compare_bot_actual_vs_labels(labels_filename, bot_filename, domain_file):
    """
    Determines the first mismatch occurred in a test conversation, as well as the expected length of the conversation.
    See test_utils.match(...) for a description on match criteria
    :param labels_filename: input filename. See the README file in data/test_files on format
    :param bot_filename: actual output filename
    :param domain_file: bot domain yml file
    :return: a dictionary r with r['mismatch_at'] = index of the first mismatched bot utterance (None, if there were no
    mismatches), and r['conversation_len'] = expected number of bot utterances
    """
    domain = TemplateDomain.load(domain_file)
    actual_vs_labels = _bot_actual_vs_labels(labels_filename, bot_filename)
    results = {'mismatch_at': None, 'conversation_len': len([label for _, label in actual_vs_labels
                                                             if label != IGNORE_TOKEN])}
    for i, (actual, label) in enumerate(actual_vs_labels):
        if label == IGNORE_TOKEN and i == 0:
            raise ValueError('{} token found on first line of the file. {} can only appear after a successful '
                             'match'.format(IGNORE_TOKEN, IGNORE_TOKEN))
        else:
            if not match(actual, label, domain):
                results['mismatch_at'] = i
                return results
    return results


def match(bot_actual, label, domain):
    """
    Determines if the actual bot utterance and the label match
    :param bot_actual: Union[Text, None]. Actual utterance of the bot
    :param label: Union[Text, None]. Target utterance. bot_actual must either match label exactly, or any of the
    template phrases mapped to the label in the domain.
    If label is ANY_TOKEN or IGNORE_TOKEN, this will return True.
    :param domain: rasa.core.domain.Domain. Domain object with the valid templates specifying all valid utterances for
    a given speech act
    :return: Union[True, False]
    """
    if bot_actual == label:
        return True
    if label == ANY_TOKEN:
        return True
    if label == IGNORE_TOKEN:
        return True
    if label in domain.templates:
        if bot_actual in [domain.templates[label][i]['text'] for i in range(len(domain.templates[label]))]:
            return True
    return False


def _bot_actual_vs_labels(labels_filename, bot_filename):
    actual_vs_label = []
    with open(labels_filename, 'r') as labels_file, open(bot_filename, 'r') as botfile:
        for label in labels_file:
            bot_label = label.split(INPUT_SPLIT_SEPARATOR)[1].strip()
            if re.match(IGNORE_REGEX, bot_label):
                ignore_times = re.search('\d+', bot_label)
                # if there is a number along with the [IGNORE] token
                ignore_times = int(bot_label[ignore_times.start():ignore_times.end()]) if ignore_times else 1
                [actual_vs_label.append((botfile.readline().strip(), IGNORE_TOKEN)) for _ in range(ignore_times)]
            else:
                actual_vs_label.append((botfile.readline().strip(), bot_label))
    return actual_vs_label


