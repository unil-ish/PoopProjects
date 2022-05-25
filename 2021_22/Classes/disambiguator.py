from pywsd import disambiguate

class Disambiguator():

    def __init__(self, dataframe_speaker_speech):
        self.disambiguated_df = dataframe_speaker_speech

    def disambiguate(self):
        self.disambiguated_df=self.disambiguated_df.astype('string')
        self.disambiguated_df['disambiguated']=self.disambiguated_df.speech.apply(lambda x: disambiguate(x))
        return self.disambiguated_df