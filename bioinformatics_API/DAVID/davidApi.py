# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:47:09 2019

@author: samsung
自写的DAVID API做功能富集分析
https://david.ncifcrf.gov/content.jsp?file=DAVID_API.html
"""

import pandas as pd
from selenium import webdriver
import time
DAVID = 'http://david.abcc.ncifcrf.gov/'
class funcAnnotChart:
    def __init__(self):
        self.params={
        'type':'UNIPROT_ACCESSION',
          'ids':'P00561,P02359,P02413,P0A7L3,P0A7M2,P0A7R5,P0A7R9,P0A7S9',
          'tool':'chartReport',
          'annot':'GOTERM_BP_FAT,GOTERM_CC_FAT,GOTERM_MF_FAT'
          }
        self.out_dir='./'
        self.flist='dep100_0_list.txt'
    def setOutDir(self,s):
        self.out_dir=s
    def setFlist(self, s):
        self.flist=s
    def setParam(self,key,value):
        self.params[key]=value
    def setParams(self,params):
        self.params=params
    def trans(self,s):
        if type(s)==str:
            s=[s]
        if type(s)!=list:
            return str(s)
        return ','.join(s)
    def showParams(self):
        for i in self.params:
            print(i+':',end=' ')
            print(self.params[i])
    def readIds(self):
        with open(self.flist,'r') as f:
            deps = [x.strip() for x in f.readlines()]
        deps = ','.join(deps)
        self.setParam('ids',deps)
        return None
    def query(self):
        PHP='api.jsp?'
        self.readIds()
        params=self.params
        req=DAVID+PHP
        for i in self.params:
            req+='&'+i+'='+self.trans(params[i])
        req.replace('jsp?&','jsp?')
        driver = webdriver.Firefox()
        driver.get(req)
        time.sleep(15)
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table[3]/tbody/tr/td[2]/font/a').click()
        time.sleep(3)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        resurl = driver.current_url
        res=pd.read_csv(resurl, sep='\t')
        res.to_csv(self.flist.replace('.txt','_GOFAT.csv'),sep=',',index=None)
        driver.close()
        driver.quit()
        return None

flist = ['deps_accession.txt']
for i in flist:
    annotChart = funcAnnotChart()
    annotChart.setFlist(i)
    annotChart.showParams()
    annotChart.query()