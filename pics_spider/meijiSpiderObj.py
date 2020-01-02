# -*- coding: utf-8 -*-
"""
OOP programming

pics_spider

http://www.zipdsl.com
input the category and album date to crawl
WARNING: Do not use the images crawled with this script for commercial use!!

Created on Thu Jan  2 16:38:25 2020

@author: samsung
"""

import requests
import os
from bs4 import BeautifulSoup 
import bs4

class meijiSpider:
    def __init__(self):
        self.params={
            'albumNum': 5
            }
        self.out_dir= './'
        self.page = 'http://www.zipdsl.com/sitemap.xml' 
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

    def getCoverURL(self):
        html = self.getHTMLText(self.page)
        soup = BeautifulSoup(html, "html.parser")
        albumCovers = []
        for x in soup.findAll('url'):
            if x.loc.string.endswith('.html'):
                print(x.loc.string)
                albumCovers.append(x.loc.string)
        return albumCovers
    
    def getImgurl(self, url):
        html = self.getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        imgurl = []
        for child in soup.find("div",{"class":"art_body"}).children:
            if isinstance(child,bs4.element.Tag):
                print(child.get('src'))
                imgurl.append(child.get('src'))
        return imgurl
    
    def getImgTitle(self, url):
        html = self.getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        imgTitle = ''
        imgTitle = soup.find('title').string[0:-6]
        return imgTitle
    
    def downloadImage(self, imgurl, imgTitle):
        path = self.out_dir + imgTitle
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + '//' + imgurl.split('/')[-1]
        try:
            if not os.path.exists(path):
                r = requests.get(imgurl, 
                                 headers = {
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
                                            })
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print('图片保存成功')
            else:
                print('图片已存在')
        except:
            print("图片保存失败")  
                
    def query(self):
            albumCovers = self.getCoverURL()
            num = int(self.params['albumNum'])
            for url in albumCovers[0:num]:
                imgTitle = self.getImgTitle(url)
                imgurl = self.getImgurl(url)
                for x in imgurl:
                    self.downloadImage(x, imgTitle)
                
outDir = 'F:/LifeLibrary/pics/pics_spider/meiji/'
meiji = meijiSpider()
meiji.setOutDir(outDir)
meiji.showParams()
meiji.setParams({'albumNum':6})
meiji.query()
