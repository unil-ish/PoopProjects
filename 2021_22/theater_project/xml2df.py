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
        with open(xml_path, 'rb') as xml_file:
            xml_file = xml_file.read()

            # Makes a bs object
            soup = BeautifulSoup(xml_file, 'xml')

            # Creates dataframe object
            speaker_speech_df = pd.DataFrame(columns=['speaker', 'speech'])

            # Finds all "sp" tags
            tags_sp = soup.find_all('sp')

            # Loops through each sp
            for sp in tags_sp:
<<<<<<< Updated upstream
                # Finding speaker
=======
>>>>>>> Stashed changes
                speaker = sp.find('speaker').text

                # Skipping speakers that have long names
                # because it sometimes happens that the speech
                # got confused with the speaker's name during encoding
                if len(speaker) > 35 or speaker.count(" ") > 5:
                    continue

                # Finds all possible speech that 
                # a speaker can have (tags p and l)
                tags = sp.find_all('l') + sp.find_all('p')
                
                # Loops through tags and adds to dataframe
                for tag in tags:
<<<<<<< Updated upstream
                   speaker_speech_df = strip_n_concat(speaker_speech_df,speaker,tag)          
=======
                   speaker_speech_df = strip_n_concat(speaker_speech_df,speaker,tag)     
                        
>>>>>>> Stashed changes
        print(speaker_speech_df)
        return speaker_speech_df       

    # Returns empty dataframe if the file could not be opened/found
    except IOError:
        print("Note : The supplied file was not found.")
        return pd.DataFrame(columns=['speaker', 'speech'])

def strip_n_concat(dataframe,speaker, tag):
    tag = tag.text.strip()
    dataframe = pd.concat([dataframe, dataframe.from_dict({'speaker':[speaker], 'speech':[tag]})], ignore_index=True)
    return dataframe
xml2df("./data/AbrahamLincolnbyJohnDrinkwater11172.xml")
