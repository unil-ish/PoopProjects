from senticnetStuff import Senticnet_ops as sops
from pywsd import disambiguate as dis
from pywsd.similarity import max_similarity as maxsim
from lemmarize import Lemmarize as lem
import pandas as pd
import json



file_path = 'C:/Users/helpdesk/Documents/Github_Pedro/PoopProjects/2021_22/theater_project/corr_senticnet.json'

test = "the love is pouring from death"

def main():
    # Disambiguate function 
    disamb_text = (dis(test, algorithm=maxsim, similarity_option='wup', keepLemmas=True))
    corrected_senticnet = loadCorrectedSenticnet(file_path)


    lemmas = lem.getLemmas(disamb_text)
    emotions = fromLemmas(lemmas, corrected_senticnet)

    print(emotions)

def loadCorrectedSenticnet(path):
    with open(path, 'r') as file:
        corr_senti = json.load(file)
    return corr_senti  
 
def fromLemmas(lemmas, senti_file):
    emotions_df = pd.DataFrame(columns=['word', 'primary_emotion', 'secondary_emotion'])
    lemmas_list = []
    for column in lemmas :
        lemmas_list.append([item for sublist in lemmas[column] for item in sublist])  
    for lemma_list in lemmas_list:
        emotions_df = pd.concat([emotions_df,sops.getEmotions(senti_file, lemma_list)])
    return emotions_df

if __name__ == "__main__":
    main()
