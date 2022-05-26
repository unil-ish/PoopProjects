# Import the different packages that we need
import re, os, tqdm
import pandas as pd


# Create the "Preprocessor" class
class Preprocessor():

    # This class needs an __init__ function
    def __init__(self, filepath):
        # With the file's path
        self.path = filepath

        # Create four empty lists to use later
        self.regex_speaker_in_doc = []
        self.regex_speech_in_doc = []
        self.filename = []
        self.gender = []

    # Create a "process_speakers_and_speeches" function
    def process_speakers_and_speeches(self):
        # For each folder in the main folder
        for folder in os.listdir(self.path):
            #print(folder)
            # For each file in each folder
            for file in tqdm.tqdm(os.listdir(self.path+"/"+folder)):
                #print(file)
                # Open the file
                with open(self.path +"/"+ folder + "/" + file, "r") as f :
                    # Put the content of the file in a variable "document"
                    document = f.read()
                    # Add the gender of the folder to the list "self.gender"
                    self.gender.append(folder)
                    # Add the filename to the list "self.filename"
                    self.filename.append(file)

                # Initialize a regular expression for the speakers
                    regex_speaker = re.compile("[A-Z]{3}.+")
                # Use this regex to find all the speakers in the "document"
                    self.regex_speaker_in_doc.append(regex_speaker.findall(document))

                # Initialize another regular expression for the speeches
                regex_speech = re.compile("((^[A-Z]{3}.+\n\n)(.+\n\n)+?(?=[A-Z]{3}.+))")
                # Use this regex to find all the speeches in the "document"
                self.regex_speech_in_doc.append(regex_speech.findall(document))
        #print(self.regex_speech_in_doc)

        # Return a dataframe with the columns Speech and Speaker with the associated information
        return pd.DataFrame({"Speech":pd.Series(self.regex_speech_in_doc),"Speaker":pd.Series(self.regex_speaker_in_doc), 'Filename':pd.Series(self.filename),'Gender':pd.Series(self.gender)}
                                     )


