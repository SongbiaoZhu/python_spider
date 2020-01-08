# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:50:43 2020

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

def getPageNum(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    num = 1
    num = soup.find('a', title = '最后一页').get('href').split('=')[-1]  
    return int(num)

def getFacultyPage(url, num):
    pages = []
    for x in range(1, num + 1):
        page = url + '&page=' + str(x)
        pages.append(page)
    return pages

def getFacultyURL(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    facultyURLs = []
    for x in soup.findAll('a', attrs={'class':'fl'}):
        print(x.get('href'))
        facultyURLs.append('http://www.nibs.ac.cn/' + x.get('href'))
    return facultyURLs

def getFacultyInfo(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    facultyInfo = []
    for tr in soup.findAll('div', attrs={'class', 'ds_js'}):
        # print(tr.get_text())
        facultyInfo.append(tr.get_text())
    return facultyInfo

def writeTxt(datastr,name):
    f=open(name, 'w', encoding = 'utf-8')
    f.write(datastr)
    f.write('\n')
    f.close()

def delblankline(infile):
    """ Delete blanklines of infile """
    outfile = infile.split('.')[0] + '_new.txt'
    infp = open(infile, "r", encoding = 'utf-8')
    outfp = open(outfile, "a", encoding = 'utf-8')
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()

def main(url):
    num = getPageNum(url)
    pages = getFacultyPage(url, num)
    facultyURLs = []
    for url in pages:
        facultyURLs = getFacultyURL(url)
        for url in facultyURLs:
            facultyInfo = getFacultyInfo(url)
            for x in facultyInfo:
                writeTxt(x, name)
                delblankline(name)

url = 'http://www.nibs.ac.cn/yjsjyimg.php?cid=8&sid=25'
path = 'D:/ProgramFiles/PythonScripts/'
fname = 'nibsFaculty'+'.txt'
name = path + fname
if __name__ == '__main__':
    main(url)