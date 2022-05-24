import re


class Preprocessor():

    def __init__(self,filepath):
        with open(filepath, "r") as f :
            self.document = f.read()

    def preprocess(self):
        regex = re.compile("(?<=Synset\(')[^.]+")
        regex_dog = str(regex.findall(str(self.document)))
        print(regex_dog)

