from rasa_core.channels.channel import InputChannel, OutputChannel
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.console import ConsoleOutputChannel

END_UTTERANCE_TOKEN = '<END_UTTERANCE>'
INPUT_SPLIT_SEPARATOR = '|||'
SILENCE_TOKEN = ''


class FileOutputChannel(OutputChannel):
    """
    A simple file output channel
    """
    def __init__(self, outputfile):
        """
        :param outputfile: output file handler. Must have a write(Text) callable member
        """
        self.outputfile = outputfile

    def send_text_message(self, recipient_id, message):
        """
        Writes a message through the channel
        :param recipient_id: id of recipient
        :param message: Text. \n character is appended to it
        """
        self.outputfile.write(message + '\n')


class FileInputChannel(InputChannel):
    """
    A channel that receives user utterances from a file. Each line in the file has one user utterance that are passed
    sequentially to the bot. It can be used in test mode, with labels to compare bot utterances against (see
    _read_test_mode(message_handler) documentation)
    It can also use in non test mode. In this case the output is directed to console. See
    _read_with_console_output(message_handler) documentation for this mode
    """

    def __init__(self, inputfilename='input_labels.txt', outputfilename=None):
        """
        :param inputfilename: name of input file
        :param outputfilename: name of output file. If not provided, output is printed to console
        """
        self.inputfilename = inputfilename
        self.outputfilename = outputfilename
        self.output_to_file = outputfilename is not None

    def _read_test_mode(self, message_handler):
        """
        Reads from an input file and outputs to another file. Each line of the input file must follow the format
        user_message \t bot_answer
        If a line in the input file is meant for the bot label only, you can put the SILENCE_TOKEN in the user input
        side and that line won't be sent.
        The output file produced can be compared with the input file for discrepancies.
        :param message_handler: Callable[[UserMessage], Optional[List[Text]]], a function that given the message,
        handles the tracker update and action selection of the model. Normally it's rasa.core.processor.handle_message
        """
        with open(self.inputfilename, 'r') as inputfile, open(self.outputfilename, 'a') as outputfile:
            for line in inputfile:
                usr_input = line.strip().split(INPUT_SPLIT_SEPARATOR)[0]  # no need for bot label
                if usr_input != SILENCE_TOKEN:  # if user said nothing, this line was just meant for bot output
                    message_handler(UserMessage(usr_input, FileOutputChannel(outputfile)))

    def _read_with_console_output(self, message_handler):
        """
        Reads from an input file and outputs to console. Each line of the file must have one user utterance. The
        SILENCE_TOKEN token must not be used.
        :param message_handler: Callable[[UserMessage], Optional[List[Text]]], a function that given the message,
        handles the tracker update and action selection of the model. Normally it's rasa.core.processor.handle_message
        """
        with open(self.inputfilename, 'r') as inputfile:
            for line in inputfile:
                message_handler(UserMessage(line.strip(), ConsoleOutputChannel()))

    def start_sync_listening(self, message_handler):
        """
        Starts listening synchronously. See InputChannel.start_sync_listening
        :param message_handler: Callable[[UserMessage], Optional[List[Text]]], a function that given the message,
        handles the tracker update and action selection of the model. Normally it's rasa.core.processor.handle_message
        """
        if self.output_to_file:
            self._read_test_mode(message_handler)
        else:
            self._read_with_console_output(message_handler)
