# -*- coding: utf-8 -*-

import requests
import json
#from xml.dom import minidom
import xml.etree.ElementTree
import re

def xliff_translate(text): #funkcija sarunājas ar tildi - iztulko no angļu uz latviešu
    return 'Tulkojums'


def main():
    # namespaces = {'default': 'urn:oasis:names:tc:xliff:document:1.2',
    #               'okp': 'okapi-framework:xliff-extensions',
    #               'its': 'http://www.w3.org/2005/11/its',
    #               'itsxlf': 'http://www.w3.org/ns/its-xliff/'}


    filename = 'manual.md.xlf'
    with open(filename, 'r', encoding='UTF-8') as file:
        xliff = file.read()

    xliff_translated = xliff

    rx_source = re.compile(r'<source xml:lang="en">((.|\n|\r)*?)</source>', re.MULTILINE)
    for chunk in  rx_source.finditer(xliff):
        translation = xliff_translate(chunk.group(1))
        xliff_translated = xliff_translated.replace(chunk.group(1),translation)

    print(xliff_translated)


if __name__ == '__main__':
    main()