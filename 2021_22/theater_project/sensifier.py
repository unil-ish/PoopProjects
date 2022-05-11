"""WORK IN PROGRESS"""

from bs4 import BeautifulSoup



file_path = '/Users/st-hilairecharlotte/Documents/GitHub/PoopProjects/2021_22/senticnet.py'

with open(file_path, 'r') as xml_file:
    xml_file = xml_file.read()
    soup = BeautifulSoup(xml_file, 'xml')
    primary_emotions = soup.find('primary_emotion')

    print(primary_emotions)