from pywsd import disambiguate

class Disambiguator():

    def __init__(self, dataframe_speaker_speech):
        self.disambigauted_df = dataframe_speaker_speech

    def disambiguate(self):
        self.disambigauted_df=self.disambigauted_df.astype('string')
        self.disambigauted_df['disambiguated']=self.disambigauted_df.speech.apply(lambda x: disambiguate(x))
        return self.disambigauted_df