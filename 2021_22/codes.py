"""
        Converts a TEI-encoded theater play into a panda's dataframe.
        It takes as argument a local path to the XML file
        and returns a panda's dataframe object.
        The returned dataframe contains two columns :
            - speaker : The speaker who said the related speech
            - speech  : The content of the speech (XML tag p or l)
        Each XML tag p or l is one line in the dataframe.
    """

from bs4 import BeautifulSoup
import pandas as pd


def xml2df(xml_path):
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
                speaker = sp.find('speaker').text

                # Skipping long names to avoid possible mistags
                if len(speaker) > 35 or speaker.count(" ") > 5:
                    continue

                # Finds all possible speech that a speaker can have (tags 'p' and 'l')
                tags = sp.find_all('l') + sp.find_all('p')

                # Loops through tags and adds to dataframe
                for tag in tags:
                    speaker_speech_df = strip_n_concat(speaker_speech_df, speaker, tag)

        return speaker_speech_df

        # Returns empty dataframe if the file could not be opened/found
    except IOError:
        print("Note : The supplied file was not found.")
        return pd.DataFrame(columns=['speaker', 'speech'])


# Strips texts and concatenates dataframe, df.append is deprecated
def strip_n_concat(dataframe, speaker, tag):
    tag = tag.text.strip()
    dataframe = pd.concat([dataframe, dataframe.from_dict({'speaker': [speaker], 'speech': [tag]})], ignore_index=True)
    return dataframe


xml2df("./data/AbrahamLincolnbyJohnDrinkwater11172.xml")

#size_data = data.groupby(['speaker']).size()
#speech_data = data.groupby(['speech']).size()
#plt.ylabel('speakers')
#plt.set_title('Abraham Lincoln')
"""import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

theater = sns.load_dataset("")

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=speaker, kind="speech",
    x="species", y="body_mass_g", hue="sex",
    ci="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Body mass (g)")
g.legend.set_title("")
-Statistic (qui prendra certainement une instance de Play lors de son _init_() 
 et qui permettra de faire des statistiques sur la pièce en entier)
- Vizualisation (pareil que Statistics, mais qui permettra de faire des visualisations de la pièce : 
p.ex.: combien de personnes parlent ? Le nombre de fois qu'elles parlent ? La quantité qu'elles parlent ? 
toutes les pr sur une graphique, L'évolution de leurs émotions au long du texte ? 
Les émotions principales par personnage ? etc.) emotion1,emotion2..
reqirement txt fichier = pip instal



sns.set_theme(style="ticks", color_codes=True)

theater = sns.load_dataset("")
sns.catplot(x="nom_speaker", y="speeches", hue="class", kind="bar", data=titanic)"""