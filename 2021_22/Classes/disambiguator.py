from pywsd import disambiguate

class Disambiguator():

    def __init__(self, dataframe):
        self.disambigauted_df=dataframe

    def disambiguate(self):
        self.disambigauted_df=self.disambigauted_df.astype('string')
        self.disambigauted_df['disambiguated']=self.disambigauted_df.speech.apply(lambda x: disambiguate(x))
        return self.disambigauted_df