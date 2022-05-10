from lxml import etree as et
import re

file_path = "C:/Users/helpdesk/Documents/Github Pedro/PoopProjects/2021_22/theater_project/data/AbrahamLincolnbyJohnDrinkwater11172.xml"


def parsePlayXML(xmlfile):
    #with open(xmlfile, encoding="utf-8") as file_obj:
    #    xml = file_obj.read()
    with open(xmlfile, "rb") as file:
        opened_file = file.read()
        tree = et.XML(opened_file)
        nsmap = {'s': 'http://www.tei-c.org/ns/1.0'}
        print(tree.xpath('.//s:speaker/text()', namespaces=nsmap))

#parsePlayXML(file_path)

def pre_processXML(xmlfile):
    with open(xmlfile, "rb") as file:
        xmlfile = str(file.read())

        regex = r"<sp>[^<]+<speaker>[^<]+</speaker>"
        res = re.findall(regex, xmlfile)
        print(res)

pre_processXML(file_path)