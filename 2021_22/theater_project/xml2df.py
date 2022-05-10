from bs4 import BeautifulSoup
import pandas as pd

def xml2df(xml_path):
    """
        Converts a TEI-encoded theater play into a panda's dataframe.

        It takes as argument a local path to the XML file
        and returns a panda's dataframe object.
        The returned dataframe contains two columns :
            - speaker : The speaker who said the related speech
            - speech  : The content of the speech (XML tag p or l)
        Each XML tag p or l is one line in the dataframe.
    """

    # Tries to open the file
    try:
        with open(xml_path, 'r') as xml_file:
            xml_file = xml_file.read()

            # Makes a bs object
            soup = BeautifulSoup(xml_file, 'xml')

            # Creates dataframe object
            speaker_speech_df = pd.DataFrame(columns=['speaker', 'speech'])

            # Finds all "sp" tags
            tags_sp = soup.find_all('sp')

            # Loops through each sp
            for _, sp in enumerate(tags_sp):
                # Finding speaker
                speaker = sp.find('speaker').text

                # Skipping speakers that have long names
                # because it sometimes happens that the speech
                # got confused with the speaker's name during encoding
                if len(speaker) > 35 or speaker.count(" ") > 5:
                    continue

                # Finds all other possible speech that 
                # a speaker can have (tags p and l)
                tags_p = sp.find_all('p')
                tags_l = sp.find_all('l')

                # Loops through "p" tags and adds to dataframe
                for _, p in enumerate(tags_p):
                    p = p.text.strip()
                    speaker_speech_df = pd.concat([speaker_speech_df,speaker_speech_df.from_dict({'speaker':speaker, 'speech':p})], ignore_index=True)

                # Loops through "p" tags and adds to dataframe
                for _, l in enumerate(tags_l):
                    l = l.text.strip()
                    speaker_speech_df = pd.concat([speaker_speech_df,speaker_speech_df.from_dict({'speaker':speaker, 'speech':l})], ignore_index=True)

        return speaker_speech_df

    # Returns empty dataframe if the file could not be opened/found
    except IOError:
        print("Note : The supplied file was not found.")
        return pd.DataFrame(columns=['speaker', 'speech'])
