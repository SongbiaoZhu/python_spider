# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:15:32 2020

@author: samsung
"""

import requests
import os
from bs4 import BeautifulSoup

class plmmSpider:
    def __init__(self):
        self.params={
            'category': 'qingchun',
            'page': '2'}
        self.out_dir='./'
        self.page = 'https://www.plmm.com.cn/'       
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
        if self.page ==1:
            self.page = 'index.html'
        else:
            self.page = 'index_' + str(self.page) + '.html'
        html = self.getHTMLText(self.page)
        soup = BeautifulSoup(html, "html.parser")
        albumCovers = []
        for tag in soup.find('div', class_ = 'goods-item'):
            print(tag.div.a['href'])
            albumCovers.append(tag.div.a['href'])
        return albumCovers
    def getImgurl(self, url):
        html = self.getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        imgurl = []
        for x in soup.find('a', class_ = 'demo-gallery__img--main'):
            print(x['href'])
            imgurl.append(x['href'])
        return imgurl
    def getImgTitle(self, url):
        html = self.getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        imgTitle = ''
        imgTitle = soup.find('title').string.split('_')[0]
        return imgTitle
    
    def downloadImage(self, imgurl, imgTitle):
        path = self.out_dir + imgTitle
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + '//' + imgurl.split('/')[-1].split('@')[0]
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
        print('set category as one of: xinggan, qingchun, meinv, chemo, qipao')
        albumCovers = self.getCoverURL()
        for url in albumCovers:
            imgTitle = self.getImgTitle(url)
            imgurl = self.getImgurl(url)
            self.downloadImage(imgurl, imgTitle)
                
 
outDir = 'F:/LifeLibrary/pics/pythonSpider/mzitu/'
mzitu = mzituSpider()
mzitu.setOutDir(outDir)
mzitu.showParams()
mzitu.setParams({'year':'2019', 'month':'4'})
mzitu.query()

list1 = [1,2]
for i in list1:
    mzitu.params['month'] = str(i)
    mzitu.query()