class Character:
    """
        Character class.

        It is used to store the name and speeches of a character
        in the play, and allows the user to easily obtain the
        values they are looking for (e.g. the amount of total
        words spoken by a character, etc.).

        It requires the Speech class to work as expected.
    """

    def __init__(self, name):
        self.name = name
        self.speeches = []
        self.primary_emotion = None
        self.secondary_emotion = None

    def getEmotion(self, scene=0):
        """ Estimates the general emotion of the character throughout the play. """

        # TO DO #

        # Loops through each speech in a specific scene (if specified)
        # If scene is 0, loops through the entire play (= all speeches)
        # [code here]
        
        # Finds the average primary/secondary emotion
        # [code here]

        # Finally setting values as attributes
        # [code here]

        pass

    @property
    def countWords(self):
        """ Counts the amount of words spoken by a character. """

        # Loops through each speech and makes the sum
        wordCount = sum([speech.countWords for speech in self.speeches])

        return wordCount

    @property
    def countSpeeches(self):
        """ Counts the amount of speeches belonging to a character. """

        return len(self.speeches)
