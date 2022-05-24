import re


class Preprocessor():

    def __init__(self,filepath):
        with open(filepath, "r") as f :
            self.document = f.read()

    def preprocess_speaker(self):
        regex_speaker = re.compile("[A-Z]{2}.+")
        regex_dog = str(regex.findall(str(self.document)))
        print(regex_dog)

