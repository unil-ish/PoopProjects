import seaborn as sns
import matplotlib.pyplot as plt
import play

class Visualization:
    """
        Visualization class.

        Makes different visualizations based on the parameters entered.
    """
    def __init__(self):
        self.play = play

    def countCharacters(self):

        #Counts how many speakers there are
        pass


    def countSpeechesFromCharacter(self):

        path = './theater/AbrahamLincolnbyJohnDrinkwater11172.xml'
        p = play.Play(path)

        valeurs = {}

        for c in p.characters:
            #     # for s in c.speeches:
            #     #     s.disambiguate()
            valeurs[c.name] = len(c.speeches)

        print(valeurs)

        # Orders the dict by the value
        valeursList = sorted((value, key) for (key, value) in valeurs.items())
        valeursSorted = dict([(k, v) for v, k in valeursList])

        keys = list(valeursSorted.keys())
        values = list(valeursSorted.values())

        sns.barplot(x=values, y=keys)
        plt.title('Characters who spoke the most')
        plt.subplots_adjust(left=0.30)
        plt.show()

    def countWordsFromCharacters(self):

        # Ranks the characters based on how many words they spoke
        pass

    def emotionBarPlot(self):

        #Makes a barplot for every emotion of a character
