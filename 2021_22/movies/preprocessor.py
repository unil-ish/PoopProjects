import re
import pandas as pd
import re,os,tqdm
import pandas as pd
class Preprocessor():

    def __init__(self,filepath):
        self.path = filepath

        self.regex_speaker_in_doc=[]
        self.regex_speech_in_doc=[]
        self.filename=[]
        self.gender=[]

    def process_speakers_and_speeches(self):
        for folder in os.listdir(self.path):
            #print(folder)
            for file in tqdm.tqdm(os.listdir(self.path+"/"+folder)):
                #print(file)
                with open(self.path +"/"+ folder + "/" + file, "r") as f :
                    document = f.read()
                    self.gender.append(folder)
                    self.filename.append(file)

                regex_speaker = re.compile("[A-Z]{3}.+")
                self.regex_speaker_in_doc.append(regex_speaker.findall(document))

                regex_speech = re.compile("(^[A-Z]{3}.+\n\n)(.+\n\n)+?(?=[A-Z]{3}.+)")
                self.regex_speech_in_doc.append(regex_speech.findall(document))

        return pd.DataFrame({"Speech":pd.Series(self.regex_speech_in_doc),"Speaker":pd.Series(self.regex_speaker_in_doc), 'Filename':pd.Series(self.filename),'Gender':pd.Series(self.gender)}
                                     )

