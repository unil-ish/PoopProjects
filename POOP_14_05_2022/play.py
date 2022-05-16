from bs4 import BeautifulSoup
import pandas as pd
import re

# Custom classes
import character
import speech

class Play:
    def __init__(self, path):
        """
            Creates an object from a TEI-encoded theater play.

            Various information are also stored in the object,
            such as the title of the play, the author,
            the first publication date, etc.

            The object makes it easy to access characters of
            the play and their respective speeches.
        """

        # Declaring attributes needed to describe the play
        self.path = path
        self.speaker_speech = pd.DataFrame(columns=['speaker', 'speech', 'scene'])
        self.title = '?'
        self.author = '?'
        self.date = '?'
        self.text = '?' # Raw, unstructured text, without speaker
        self.scenes = 0 # Amount of scenes in the play
        self.characters = [] # List of instanciated Character

        # Tries to open the file
        try:
            with open(self.path, 'r') as xml_file:
                xml_file = xml_file.read()

                # Removes all <stage> tags before processing
                xml_file = re.sub(r'<stage>[^<]+?</stage>', ' ', xml_file)

                # Makes a bs object
                soup = BeautifulSoup(xml_file, 'xml')

                # Gets the title of the play
                self.title = soup.find('title').text

                # Gets the author of the play
                self.author = soup.find('author').text

                # Gets the date of publication
                self.date = soup.find('imprint').find('date').text

                # Finds all the scenes
                scenes = soup.find_all("div", attrs={"type" : "scene"})

                # Loops through each scene
                for s in scenes:
                    # Increments the number of scenes
                    self.scenes += 1

                    # Finds all "sp" tags in current scene
                    tags_sp = s.find_all('sp')

                    # Gets scene number
                    if s["n"]:
                        scene_number = s["n"]
                    else:
                        scene_number = 0

                    # Loops through each sp
                    for _, sp in enumerate(tags_sp):
                        # Finding speaker
                        speaker = sp.find('speaker').text

                        # Skipping speakers that have long names
                        # because it happens that the speech gets confused
                        # with the speaker's name during encoding
                        if len(speaker) > 35 or speaker.count(' ') > 5:
                            continue

                        # Finds all other possible speech that 
                        # a speaker can have (tags p and l)
                        tags_p = sp.find_all('p')
                        tags_l = sp.find_all('l')

                        # Loops through "p" tags and adds to dataframe
                        for _, p in enumerate(tags_p):
                            p = p.text.strip()

                            # Stores in dataframe for easy retrieval
                            self.speaker_speech = self.speaker_speech.append({'speaker':speaker, 'speech':speech.Speech(p, scene_number), 'scene':scene_number}, ignore_index=True)

                            # Adds raw text
                            self.text += ' ' + p

                        # Loops through "p" tags and adds to dataframe
                        for _, l in enumerate(tags_l):
                            l = l.text.strip()

                            # Stores in dataframe for easy retrieval
                            self.speaker_speech = self.speaker_speech.append({'speaker':speaker, 'speech':speech.Speech(l, scene_number), 'scene':scene_number}, ignore_index=True)

                            # Adds raw text
                            self.text += ' ' + l

            # Once it's done, creates all Character's instance
            self.makeCharacters()

            # Success message
            print(f'# Play "{self.title}" ({self.author}, {self.date}) with {self.scenes} scene(s) and {len(self.characters)} character(s) successfully loaded!')
            

        # Returns empty dataframe if the file could not be opened/found
        except IOError:
            print('# Note : The supplied file was not found.')

    def makeCharacters(self):
        """ Creates a list of Characters to handle speeches easily. """

        # Gets a list of unique names for the characters
        characters = self.speaker_speech.speaker.unique()

        # Loops through each name and adds speech to character object
        for char in characters:
            speeches_df   = self.speaker_speech[self.speaker_speech.speaker == char]
            speeches_list = []

            # Skips names appearing once (mistakes while encoding the XML)
            if len(speeches_df) < 2:
                continue

            # Adds each speech object to a temporary list
            for _, row in speeches_df.iterrows():
                speeches_list.append(row.speech)

            # Creates Character instance and links speeches to it
            newCharacter = character.Character(char)
            newCharacter.speeches = speeches_list

            # Stores Character instance in self.characters (list)
            self.characters.append(newCharacter)

    def getCharacters(self):
        """ Displays all characters in the play. """

        # Loops through each character and find their name
        character_names = [character.name for character in self.characters]
        character_names.sort()

        return character_names

    @property
    def speechAmount(self):
        """ Displays the amount of speech in the whole play. """

        return len(self.speaker_speech)

    @property
    def countWords(self):
        """ Displays the length of the play in words. """

        words = 0

        # Loops through each character
        for char in self.characters:
            # Loops through each speech
            for speech in char.speeches:
                # Increment counter
                words += speech.countWords

        return words

    def __str__(self):
        """ Returning the name of the play when printed. """
        return self.title

    def __len__(self):
        return self.countWords

