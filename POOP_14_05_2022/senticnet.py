class Senticnet:
    def __init__(self, path="senticnet/senticnet.py"):
        """
            Loads a senticnet file into a dict
        """

        self.senticnet = {}

        # Trying to open the file
        try:
            with open(path, 'r') as senticnetFile:
                senticnetFile = senticnetFile.readlines()

                # Looping through each line
                for line in senticnetFile[:100]:
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
                            self.senticnet[word] = eval(values)

                        # If something goes wrong (comment/wrong-formatted line)
                        except IndexError:
                            pass
                print(f"# Note : Senticnet successfully loaded with {len(self.senticnet)} entries.")
                return

        except IOError:
            print("# Note : Failed to load senticnet file.")
            return

    def emotionsOf(self, word):
        """
            Returns the primary and secondary emotions associated
            with a word given as argument and returns a dict
            with the two emotions, if found.
        """

        try:
            # Finding primary and secondary emotion of the word
            primary_emotion = self.senticnet[word][4]
            secondary_emotion = self.senticnet[word][5]

            # Replacing # if the emotion is a string (and not None)
            if primary_emotion:
                primary_emotion = primary_emotion.replace('#', '')
            if secondary_emotion:
                secondary_emotion = secondary_emotion.replace('#', '')

            return {
                'primary_emotion':primary_emotion,
                'secondary_emotion':secondary_emotion
            }

        except KeyError:
            return {'primary_emotion':None, 'secondary_emotion':None}

    def synonymsOf(self, word):
        """
            Tries to find the synonyms of a word given as argument
            and returns a list of synonyms, if found.
        """

        try:
            return self.senticnet[word][8:]

        except KeyError:
            return []

