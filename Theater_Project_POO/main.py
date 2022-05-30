import glob
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import wordnet as wn
import pandas as pd
import pywsd
import seaborn as sns

# Custom classes
import character
import play
import senticnet
import speech
import vizualisation

def debug():
    """ Debug function """

    p = play.Play("theater/AbrahamLincolnbyJohnDrinkwater11172.xml")

    path_csv = "csv/Abraham Lincoln- Exported.csv"
    p.from_csv(path_csv)

    # Bar plot for speeches
    barPlotSpeeches = vizualisation.Vizualisation(p, "bps")
    barPlotSpeeches.plot()

    # Bar plot for words
    barPlotWords = vizualisation.Vizualisation(p, "bpw")
    barPlotWords.plot()

    # Emotions by character
    emotionByCharacter = vizualisation.Vizualisation(p, "ebc")
    emotionByCharacter.plot()

    # Emotions by act
    emotionByAct = vizualisation.Vizualisation(p, "eba")
    emotionByAct.plot()

def main(path, stcnet):
    """ Main function """

    # (4) Loads the play into a new object
    p = play.Play(path)

    # Avoids processing not found plays
    if p.speech_amount > 0:
        # (5) Loops through each speech of each character to get
        # the emotions for each speech of the play
        for character in p.characters:
            for speech in character.speeches:
                # Compute overall emotions of each speech
                speech.getEmotions(stcnet)

        # (6) Exports the data to CSV, for later reuse
        p.to_csv()

        # (7) If needed, reimports everything from the csv
        #path_csv = "path/to/csv" 
        #p.from_csv(path_csv)

        # (8) Generates and saves plots

        # Bar plot for speeches
        barPlotSpeeches = vizualisation.Vizualisation(p, "bps")
        barPlotSpeeches.plot(True)

        # Bar plot for words
        barPlotWords = vizualisation.Vizualisation(p, "bpw")
        barPlotWords.plot(True)

        # Emotions by character
        emotionByCharacter = vizualisation.Vizualisation(p, "ebc")
        emotionByCharacter.plot(True)

        # Emotions by act
        emotionByAct = vizualisation.Vizualisation(p, "eba")
        emotionByAct.plot(True)

    return

if __name__ == '__main__':

    debug()

    ######################################
    # Uncomment this once tests are done #
    ######################################

    """
    # (1) Loading senticnet [mandatory for emotions' search]
    stcnet = senticnet.Senticnet()

    # (2) Finds all xml files
    plays = glob.glob("theater/*.xml")

    # (3) Makes the whole process for each xml file [takes a long time]
    for path in plays:
        main(path, stcnet)
    """
