import senticnet

class Emo_extractor():

    def __init__(self, disambigauted_df):
        self.emotions_df = disambigauted_df

    def extract_emotion(self):
        self.emotions_df = self.emotions_df.astype('string')
        for each in self.emotions_df:
            for word, synset in each:
                self.emotions_df['1st emotion'] = self.emotions_df.disambiguated[word].senticnet.senticnet[word][4]
                self.emotions_df['2nd emotion'] = self.emotions_df.disambiguated[word].senticnet.senticnet[word][5]

