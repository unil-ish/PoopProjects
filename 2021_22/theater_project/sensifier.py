from bs4 import BeautifulSoup
from senticnetStuff import Senticnet_ops as sops
import json


file_path = 'C:/Users/helpdesk/Documents/Github_Pedro/PoopProjects/2021_22/theater_project/corr_senticnet.json'


def loadCorrectedSenticnet(path):
    with open(path, 'r') as file:
        corr_senti = json.load(file)
    return corr_senti    

corrected_senticnet = loadCorrectedSenticnet(file_path)

emotions = sops.getEmotions(corrected_senticnet, ['love', 'hate', 'fool'])
print(emotions)