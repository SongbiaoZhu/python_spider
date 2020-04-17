# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:35:02 2020

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def fillRankList(html):
    rankList = []
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            rankList.append([tds[0].string, tds[1].string, tds[2].get_text().replace('\r\n', '').replace('  ',''), tds[3].string])
    tableHead = ['Rank', 'Name', 'Country/Region', 'Score']
    rankList[0] = tableHead
    return rankList

def writeTxt(rankList,path, fname):
    name = path + fname
    f=open(name, 'w', encoding = 'utf-8')
    for i in rankList:
        for j in i:
            f.write(j)
            f.write('\t')
        f.write('\n')
    f.close()

def main():
    url = 'http://www.betteredu.net/rankings/THE/2019-2020/top-1000.html'
    html = getHTMLText(url)
    rankList = fillRankList(html)
    path = 'D:/ProgramFiles/PythonScripts/'
    fname = 'University_World_Rank.txt'
    writeTxt(rankList,path, fname)
    
if __name__ == '__main__':
    main()