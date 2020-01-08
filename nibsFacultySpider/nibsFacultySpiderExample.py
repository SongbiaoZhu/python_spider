# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:15:12 2020

@author: samsung
"""

import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def writeTxt(datastr,path, fname):
    name = path + fname
    f=open(name, 'w', encoding = 'utf-8')
    f.write(datastr)
    f.write('\n')
    f.close()

def delblankline(infile, outfile):
    """ Delete blanklines of infile """
    infp = open(infile, "r", encoding = 'utf-8')
    outfp = open(outfile, "a", encoding = 'utf-8')
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()

url = 'http://www.nibs.ac.cn/yjsjyimgshow.php?cid=5&sid=6&id=775'
html = getHTMLText(url)
soup = BeautifulSoup(html, "html.parser")
path = 'D:/ProgramFiles/PythonScripts/nibsFacultySpider/'
fname = 'Luominmin'+'.txt'
dat = []
for tr in soup.findAll('div', attrs={'class', 'ds_js'}):
    # print(tr.get_text())
    dat.append(tr.get_text())
    
for x in dat:
    writeTxt(x, path, fname)
    delblankline(path + fname, path + 'Luominmin_new.txt')