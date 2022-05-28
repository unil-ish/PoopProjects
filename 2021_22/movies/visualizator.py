# Import the differnet packages that we need
import seaborn as sns


# Create the "Visualizator" class
class Visualizator():

    # This class needs an __init__ function
    def __init__(self, df_speakers_speeches):
        # With the dataframe we received after the preprocess operation
        self.df_speeker_speech_vizualization = df_speakers_speeches

    # Create a "gender_vizualize" function
    def gender_visualize(self):

        # Create and return a visualization of the gender's occurrences in our datatable
        sns.set_theme()
        return sns.histplot(data=self.df_speeker_speech_vizualization, x="Gender")


