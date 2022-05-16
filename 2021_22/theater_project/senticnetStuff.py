import pandas as pd
import json


class Senticnet_ops:
    def loadSenticnet(path):
        """
            Loads broken-encoded senticnet file
            into a well-formatted python dict
        """

        senticnet = {}

        # Opening senticnet.py and reading it
        with open(path, 'r', encoding='utf-8') as senticnetFile:
            senticnetFile = senticnetFile.readlines()

            # Looping through each line
            for line in senticnetFile:
                line = line.strip()

                # Skipping comments
                if line [0] == '#':
                    pass
                else:
                    # Trying to get the word
                    try:
                        # Getting the word
                        word = line.split("'] = [")[0].strip()
                        word = word.replace("senticnet['", '')

                        # Getting the value associated with the word
                        values = '[' + line.split("'] = [")[1]

                        # Adding to senticnet dict
                        # Unsafe (because of eval()), but I won't create
                        # a parser for the values
                        senticnet[word] = eval(values)

                    # If something goes wrong (comment/wrong-formatted line)
                    except IndexError:
                        pass
        # 
        #with open('corr_senticnet.json', 'w') as output_file:
        #    output_file = json.dump(senticnet, output_file)
        return senticnet

    def getEmotions(senticnet, wordlist):
        """
            Returns primary and secondary emotions
            associated with a word found in senticnet

            Take as argument a well-formatted
            senticnet dict and a word and returns
            a dict with the two emotions
        """

        try:
            emo_df = pd.DataFrame(columns=['word','primary_emotion', 'secondary_emotion'])
            for word in wordlist:
                # Finding primary and secondary emotion of the word
                primary_emotion = senticnet[word][4]
                secondary_emotion = senticnet[word][5]

                # Replacing # if the emotion is a string (and not None)
                if primary_emotion:
                    primary_emotion = primary_emotion.replace('#', '')
                if secondary_emotion:
                    secondary_emotion = secondary_emotion.replace('#', '')
                emo_df = pd.concat([emo_df, emo_df.from_dict({'word':[word],'primary_emotion':[primary_emotion], 'secondary_emotion':[secondary_emotion]})])      
        except KeyError:
            return {'primary_emotion':None, 'secondary_emotion':None}
        return emo_df


    def getSynonyms(senticnet, word):
        """
            Try to find the synonyms of a word and returns a list

            Take as argument a well-formatted
            senticnet dict and a word and returns
            a list of synonyms
        """

        try:
            return senticnet[word][8:]
        except KeyError:
            return []
