# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:29:49 2019

@author: samsung
"""

import requests
import os
import re
from bs4 import BeautifulSoup

class mzituSpider:
    def __init__(self):
        self.params={
            "year": "2019",
            "month": "2"}
        self.out_dir='./'
        self.page = 'https://www.mzitu.com/all/'       
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
        year = self.params['year']
        month = self.params['month']
        yearTag = soup.find('div', class_ = 'year', string = re.compile(r"^(%s)年$" %year)).find_next_sibling()
        monthTag = yearTag.find('em', string = re.compile(r"(%s)月$" %month)).parent.find_next_sibling('p', class_ = 'url')
        albumCovers = []
        for tag in monthTag.find_all('a', target = '_blank'):
            print(tag['href'])
            albumCovers.append(tag['href'])
        return albumCovers
    def getImgNum(self, url):
        html = self.getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        imgNum = ''
        try:
            imgNum = soup.find('span', string = re.compile('下一页')).parent.previous_sibling.span.string
        except:
            pass
        return imgNum
    def getImgTitle(self, url):
        imgTitle = url.split('/')[-1]
        return imgTitle
    def getAlbumURL(self, url, imgNum):
        albumURL = [url]
        for i in range(2,int(imgNum)+1):
            albumURL.append(url + '/' + str(i))
        return albumURL
    def getImgurl(self, url):
        html = self.getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        imgurl = ''
        imgurl = soup.find('div', class_ = 'main-image').img['src']
        return imgurl
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
                                 headers = {'Host': 'i5.meizitu.net',
                                            'Pragma': 'no-cache',
                                            'Accept-Encoding': 'gzip, deflate',
                                            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                                            'Cache-Control': 'no-cache',
                                            'Connection': 'keep-alive',
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                                            'Referer': '{}'.format(imgurl),
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
        for url in albumCovers:
            imgNum = self.getImgNum(url)
            imgTitle = self.getImgTitle(url)
            albumURL = self.getAlbumURL(url, imgNum)
            for url in albumURL:
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