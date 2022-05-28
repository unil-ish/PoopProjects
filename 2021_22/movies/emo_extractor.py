#Import the packages that we need
import string
import pandas as pd
import tqdm
import senticnet
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

#Create our class
class Emo_Extractor():

    #Define the __init__ function which take the disambiguated dataframe that we created in the previous step
    def __init__(self, disambigauted_df):
        self.emotions_df = disambigauted_df

    #Create the function to extract the emotion of our speeches
    def extract_emotion(self):
        #Create 2 empty lists in which we'll put our first and second emotions
        first_emotion = []
        second_emotion = []
        #Convert to string so we can use it
        self.emotions_df = self.emotions_df.astype('string')

        #Create a loop to take each word in our disambiguated speeches
        for elements in tqdm.tqdm(self.emotions_df['disambiguated']):
            for each in elements:
                #Lower the words so there is no conflict
                word = each[0].lower()
                #If our word has a result in senticnet, add the first and second emotion in the corresponding list
                if word in senticnet.senticnet.keys():
                    first_emotion.append(senticnet.senticnet[word[4]])
                    second_emotion.append(senticnet.senticnet[word[5]])
                #If our word has a result in the values from senticnet,
                #add the first and second emotion in the corresponding list
                elif word in senticnet.senticnet.values():
                    first_emotion.append(senticnet.senticnet[word[4]])
                    second_emotion.append(senticnet.senticnet[word[5]])
                # If our word has no result neither in the keys nor in the values
                elif word not in senticnet.senticnet.keys() or senticnet.senticnet.values():
                    #Create an empty list "synonyms"
                    synonyms = []
                    #Find synonyms in wordnet
                    for syn in wordnet.synsets(word):
                        for l in syn.lemmas():
                            synonyms.append(l.name())
                    #If the word has synonyms
                    if synonyms:
                        #Look up if the first synonym of the list is in the senticnet's keys
                        if synonyms[0] in senticnet.senticnet.keys():
                            #Add the first and second emotion in the corresponding list
                            first_emotion.append(senticnet.senticnet[word[4]])
                            second_emotion.append(senticnet.senticnet[word[5]])
                        #If not, look up if the first synonym of the list is in the senticnet's values
                        elif synonyms[0] in senticnet.senticnet.values():
                            #Add the first and second emotion in the corresponding list
                            first_emotion.append(senticnet.senticnet[word[4]])
                            second_emotion.append(senticnet.senticnet[word[5]])
                        #If the synonym isn't in the senticnet's keys or values,
                        #add "not found" to the corresponding list
                        else:
                            first_emotion.append("not found")
                            second_emotion.append("not found")
                    #If there isn't a synonym for the word, add "not found" to the corresponding list
                    else:
                        first_emotion.append("not found")
                        second_emotion.append("not found")

        #Create 2 new columns in the dataframe, one for the first emotion and another for the second, containing
        #the corresponding list
        self.emotions_df['1st emotion'] = pd.Series(first_emotion)
        self.emotions_df['2nd emotion'] = pd.Series(second_emotion)


        #Return the final result
        return self.emotions_df