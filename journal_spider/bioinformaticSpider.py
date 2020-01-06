# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:06:16 2019

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import os

import random
from selenium import webdriver
from time import sleep

def getHTMLText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        r = requests.get(url, headers = header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
		
def getDocURL(html):
    soup = BeautifulSoup(html, "html.parser")
    docURLs = []
    for i in soup.find_all('a', attrs = {'class':'viewArticleLink'}):
        #print(i.get('href'))
        docURLs.append('https://academic.oup.com' + i.get('href'))
    return docURLs
	
def getpdfURL(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    pdfURL = soup.find('meta', attrs = {'name':'citation_pdf_url'}).get('content')
    #print(pdfURL)
    return pdfURL

def main(page, fname):
    html = getHTMLText(page)
    docURLs = getDocURL(html)
    pdfURLs = []
    for url in docURLs:
        pdfURL = getpdfURL(url)
        pdfURLs.append(pdfURL)
    with open(fname,'w') as f:
        for line in pdfURLs:
            f.write(line)
            f.write('\n')
    return pdfURLs
            
if __name__ == '__main__':
    vol = 34
    iss = 2
    page = 'https://academic.oup.com/bioinformatics/issue/{}/{}'.format(vol, iss)
    root = "D:\\ProgramFiles\\bioinformatics"
    fname = os.path.join(root, 'pdfURLs_{}_{}.txt'.format(vol, iss))
    pdfURLs = main(page, fname)
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', 'D:\\ProgramFiles\\bioinformatics')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
    driver = webdriver.Firefox(firefox_profile=profile)
    for i in pdfURLs:
        try:
            print(i)
            driver.get(i)
            sleep(random.randint(5,10))
            driver.find_element_by_id("download").click()
            sleep(random.randint(30,45))
        except:
            continue
    driver.quit()