# Import the different packages that we need
from pywsd import disambiguate


# Create the "Disambiguator" class
class Disambiguator():

    # This class needs an __init__ function
    def __init__(self, dataframe):
        # With the dataframe we received after the preprocess operation
        self.disambiguated_df = dataframe

    # Create a "disambiguate" function
    def disambiguate(self):
        # Convert the dataframe columns into strings
        self.disambiguated_df = self.disambiguated_df.astype('string')
        # Disambiguate the Speech information and put it under a new column "disambiguated"
        self.disambiguated_df['disambiguated'] = self.disambiguated_df.Speech.apply(lambda x: disambiguate(x))

        # Return the dataframe with the disambiguated speeches
        return self.disambiguated_df