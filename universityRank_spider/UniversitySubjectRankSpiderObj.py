# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:56:10 2020

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import bs4

class univRankSpider:
    def __init__(self):
        self.params={
            'startYear':2017,
            'category':'life-sciences'
            }
        self.out_dir= './'
        self.page = 'http://rankings.betteredu.net/THE/' 
    def setOutDir(self,s):
        self.out_dir=s
    def showParams(self):
        for i in self.params:
            print(i+':',end=' ')
            print(self.params[i])
    def setParam(self,key,value):
        self.params[key]=value
    def setParams(self,params):
        self.params=params
        
    def getHTMLText(self, url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        try:
            r = requests.get(url, headers = header, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return None
    
    def fillRankList(self, html):
        rankList = []
        soup = BeautifulSoup(html, "html.parser")
        for tr in soup.find('tbody').children:
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                rankList.append([tds[0].string, tds[1].string, tds[2].get_text().replace('\r\n', '').replace('  ',''), tds[3].string])
        tableHead = ['Rank', 'Name', 'Country/Region', 'Score']
        rankList[0] = tableHead
        return rankList

    def writeTxt(self, rankList):
        name = self.out_dir + str(self.params['startYear']) +'-' + str(self.params['startYear']+1) + '_' + self.params['category'] + '.txt'
        f=open(name, 'w', encoding = 'utf-8')
        for i in rankList:
            for j in i:
                f.write(j)
                f.write('\t')
            f.write('\n')
        f.close()
        print(name + '保存完成')
        
    def query(self):
        url = self.page + str(self.params['startYear']) +'-' + str(self.params['startYear']+1) + '/' + self.params['category'] + '.html'
        html = self.getHTMLText(url)
        rankList = self.fillRankList(html)
        self.writeTxt(rankList)

CATEGORIES = ['business-and-economics',
              'education',
              'computer-science',
              'clinical-health',
              'psychology',
              'social-sciences',
              'law',
              'engineering-and-IT',
              'life-sciences',
              'physical-sciences']
outDir = 'D:/ProgramFiles/PythonScripts/'
univRank = univRankSpider()
univRank.setOutDir(outDir)
univRank.showParams()
univRank.setParams({'startYear':2016,
            'category':'life-sciences'})
univRank.query()

for i in range(2016,2018):
    univRank.setParams({'startYear':i,
        'category':'life-sciences'})
    univRank.query()
    
for i in range(2016,2018):
    univRank.setParams({'startYear':i,
        'category':'clinical-health'})
    univRank.query()