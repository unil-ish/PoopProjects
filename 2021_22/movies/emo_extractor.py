import string
import pandas as pd
import tqdm

import senticnet

class Emo_Extractor():


    def __init__(self, disambigauted_df):
        self.emotions_df = disambigauted_df

    def extract_emotion(self):
        first_emotion = []
        second_emotion = []
        self.emotions_df = self.emotions_df.astype('string')
        for elements in tqdm.tqdm(self.emotions_df['disambiguated']):
            for each in elements:
                word = each[0].lower()
                if word in senticnet.senticnet:
                    first_emotion.append(senticnet.senticnet[word[4]])
                    second_emotion.append(senticnet.senticnet[word[5]])

        self.emotions_df['2nd emotion'] = pd.Series(second_emotion)
        self.emotions_df['1st emotion'] = pd.Series(first_emotion)
        return self.emotions_df