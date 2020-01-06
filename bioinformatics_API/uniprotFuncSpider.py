# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:55:20 2019

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import time
import os


def getHTMLText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        r = requests.get(url, headers = header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getFunc(html):
    soup = BeautifulSoup(html, "lxml")
    try:
        func = soup.select('#function > div:nth-child(2) > span')[0].get_text().split('\r\n')[0]
    except:
       func = 'Not found summary of functions'
    return func

start = time.process_time()
publicDir = 'E:/publicData/' 
f = open(os.path.join(publicDir, 'Accession.txt'), 'r')
accession = f.readlines()
f.close()
funcs = []
for i in accession[1:5]:
    url = 'https://www.uniprot.org/uniprot/{}'.format(i)
    html =  getHTMLText(url)
    func = getFunc(html)
    funcs.append(func)
fw = open(os.path.join(publicDir, 'Functions.txt'), 'w')
fw.write('Function\n')
for i in funcs:
    fw.write(i)
    fw.write('\n')
fw.close()
elapsed = (time.process_time() - start)
print("Time used:{} seconds".format(elapsed))

