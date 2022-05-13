"""WORK IN PROGRESS"""

from bs4 import BeautifulSoup
from senticnetStuff import Senticnet_ops as sops


file_path = '/Users/st-hilairecharlotte/Documents/GitHub/PoopProjects/2021_22/senticnet.py'

print(sops.loadSenticnet(file_path))


with open(file_path, 'r') as xml_file:
    xml_file = xml_file.read()
    soup = BeautifulSoup(xml_file, 'xml')
    primary_emotions = soup.find('primary_emotion')

    print(primary_emotions)