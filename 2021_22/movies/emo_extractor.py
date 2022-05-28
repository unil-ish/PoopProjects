#Import the packages that we need
import string
import pandas as pd
import tqdm
import senticnet

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
                elif word not in senticnet.senticnet.keys() or senticnet.senticnet.values():


        #Create 2 new columns in the dataframe, one for the first emotion and another for the second, containing
        #the corresponding list
        self.emotions_df['1st emotion'] = pd.Series(first_emotion)
        self.emotions_df['2nd emotion'] = pd.Series(second_emotion)


        #Return the final result
        return self.emotions_df