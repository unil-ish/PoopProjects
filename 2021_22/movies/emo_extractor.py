import string

from . import senticnet

class Emo_Extractor():


    def __init__(self, disambigauted_df):
        self.emotions_df = disambigauted_df

    def extract_emotion(self):
        first_emotion=[]
        second_emotion=[]
        self.emotions_df = self.emotions_df.astype('string')
        for each in self.emotions_df['disambiguated']:
            for word, synset in each:
                first_emotion.append(senticnet.senticnet[word.lower()][4])
                second_emotion.append(senticnet.senticnet[word.lower()][5])

        self.emotions_df['2nd emotion'] = second_emotion
        self.emotions_df['1st emotion'] = first_emotion
        return self.emotions_df