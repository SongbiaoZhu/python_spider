# -*- coding: utf-8 -*-
"""
Compared with the asmsJobSpider.py, only difference is change the url to filterd postdoc position in line 43.
Created on Tue Jan 14 11:42:19 2020

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import bs4
import os

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

# crawl all the jobUrls
path = 'D:/ProgramFiles/PythonScripts/asmsJobSpider/'
url = 'https://asms-jobs.careerwebsite.com/jobs/?keywords=postdoctoral&location=&location_completion=&location_type=&location_text=&location_autocomplete=1'
html = getHTMLText(url)
soup = BeautifulSoup(html, "html.parser")
jobUrls = []
urlPrefix = 'https://asms-jobs.careerwebsite.com'
for x in soup.findAll('div', role = 'button'):
    for child in x.descendants:
        if isinstance(child, bs4.element.Tag):
            if child.name =='a':
                if not child.get('href')=='#':
                    #print(child.get('href'))
                    jobUrls.append(urlPrefix + child.get('href'))
fname = 'jobUrls_postdoc' + '.txt'  
name = path + fname
f=open(name, 'w', encoding = 'utf-8')
for x in jobUrls:
    f.write(x)
    f.write('\n')
f.close()

# Crawl every job information details
path = 'D:/ProgramFiles/PythonScripts/asmsJobSpider/jobDetails_postdoc/'
if not os.path.exists(path):
    os.mkdir(path)
for url in jobUrls:
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    dat = []
    for x in soup.findAll('div', attrs={'class', 'job-data-contain'}):
            #print(x.get_text())
            datastr = x.get_text().replace('Job Information','## Job Information')
            dat.append(datastr)
    for x in soup.findAll('div', attrs = {'class':'description-text'}):
        #print(x.get_text())
        datastr = x.get_text().replace('Description','**Description**').replace('Requirements', '**Requirements**')
        dat.append(datastr)
    fname = url.split('/')[-2] + '.txt'    
    for x in dat:
        writeTxt(x, path, fname)
        delblankline(path + fname, path + fname.split('.')[0] + '.md')
