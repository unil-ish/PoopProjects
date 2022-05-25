import re
import pandas as pd

class Preprocessor():

    def __init__(self,filepath):
        with open(filepath, "r") as f :
            self.document = f.read()

    def preprocess_speaker(self):
        self.regex_speaker = re.compile("[A-Z]{3}.+")
        self.regex_speaker_in_doc = str(self.regex_speaker.findall(str(self.document)))
        return self.regex_speaker_in_doc

    def preprocess_speech(self):
        self.regex_speech = re.compile("^(?![A-Z]{2}).*$")
        self.regex_speech_in_doc = str(self.regex_speech.findall(str(self.document)))
        return self.regex_speech_in_doc

    def dataframe_speaker_speech(self):
        self.dataframe_speaker_speech = pd.DataFrame(self.regex_speaker_in_doc, self.regex_speech_in_doc,
                                                columns=["Speaker", "Speech"])
        return self.dataframe_speaker_speech