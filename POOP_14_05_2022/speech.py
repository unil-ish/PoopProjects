import re

class Speech:
    """
        Speech class.

        It is used to store the text of each speech spoken
        by a character in the play, and allows the user
        to easily obtain the values they are looking for
        (e.g. the amount of words, the primary/secondary
        emotions of the speech, etc.).
    """

    def __init__(self, text, scene):
        self.text = text
        self.tokenized = None
        self.primary_emotion = None
        self.secondary_emotion = None
        self.scene = scene

    def tokenize(self):
        """ Converts a string into a list of words. """

        # Deletes punctuation
        text = re.sub(r'[^\w ]+', '', self.text)

        # Splits into tokens/words
        tokens = re.split(r'\s+', text)

        # Removing empty elements
        tokens = [t for t in tokens if t]

        # Stores into attribute
        self.tokenized = tokens

    @property
    def countWords(self):
        """ Counts the amount of token/words in the speech. """

        # Tokenizing if needed
        if not self.tokenized:
            self.tokenize()

        return len(self.tokenized)

    def disambiguate(self):
        """ Disambiguates words in a speech. """

        # TO DO

        pass

    def getEmotions(self):
        """ Gets primary and secondary emotion for a speech. """

        # TO DO

        pass
