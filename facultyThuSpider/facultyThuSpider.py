# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:37:48 2020

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
    
def getFacultyUrl(url):
    homePage = 'http://life.tsinghua.edu.cn'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    facultyURLs = []
    for x in soup.findAll('a', target="_self"):
        if  isinstance(x, bs4.element.Tag):
            if x.get('href'):
                #print(x.get('href'))
                facultyURLs.append(homePage + x.get('href'))
    return facultyURLs

def getFacultyInfo(url):
    html = getHTMLText(url)
    htmlNew = html.replace('</br>', '')
    soup = BeautifulSoup(htmlNew, "html.parser")
    facultyInfo = []
    for tr in soup.findAll('div', attrs={'class', 'article'}):
        # print(tr.get_text())
        facultyInfo.append(tr.get_text())
    return facultyInfo

def writeTxt(datastr,name):
    f=open(name, 'w', encoding = 'utf-8')
    f.write(datastr)
    f.write('\n')
    f.close()

def main():
    url = 'http://life.tsinghua.edu.cn/publish/smkx/11119/index.html'
    path = 'D:\\ProgramFiles\\PythonScripts\\facultyThuSpider\\'
    facultyURLs = getFacultyUrl(url)
    for url in facultyURLs:
        facultyInfo = getFacultyInfo(url)
        fname = facultyInfo[0].split('\n')[1] + '.txt'
        name = path + fname
        for x in facultyInfo:
            writeTxt(x, name)        

if __name__ == '__main__':
    main()