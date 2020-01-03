# -*- coding: utf-8 -*-
"""
Object Oritation Programming
Umei_spider
http://www.umei.cc/tags/

WARNING: Do not use the images crawled with this script for commercial use!!
Created on Fri Jan  3 16:15:33 2020

@author: samsung
"""

import requests
import os
from bs4 import BeautifulSoup 
import bs4
import re

class umeiSpider:
    def __init__(self):
        self.params={
            'category', 'meinvtupian',
            'subcategory', 'meinvxiezhen'
            }
        self.out_dir= './'
        self.page = 'http://www.umei.cc/' 
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
        
    def getHTMLTextRefer(self, url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Referer':url}
        try:
            r = requests.get(url, headers = header, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return None
        
    def getSubPage(self):
        url = self.page + str(self.params['category']) + '/' + str(self.params['subcategory']) + '/'
        # print(url)
        return url   

    def getPageNum(self, url):
        html = self.getHTMLTextRefer(url)
        soup = BeautifulSoup(html, "html.parser")
        pageNum = 1
        x = soup.find('div', {'class':'NewPages'})
        for child in x.ul.children:
            if isinstance(child,bs4.element.Tag):
                # print(child.string)
                if child.string == '末页':
                    # print(child.a.get('href').split('.')[-2])
                    pageNum = child.a.get('href').split('.')[-2]
        return pageNum

    def getPageUrl(self, url, pageNum):
        pageNum = int(pageNum)
        pageUrl = [url]
        if pageNum ==1:
            pass
        else:
            for i in range(2, pageNum+1):
                x = url + str(i) + '.htm'
                pageUrl.append(x)
        return pageUrl
    
    def getCoverURL(self, url):
        html = self.getHTMLTextRefer(url)
        soup = BeautifulSoup(html, "html.parser")
        albumCovers = []
        for x in soup.findAll('a',  {'class':'TypeBigPics'}):
            if isinstance(x,bs4.element.Tag):
                # print(x.get('href'))
                albumCovers.append(x.get('href'))
        return albumCovers
    
    def getImgNum(self, url):
        html = self.getHTMLTextRefer(url)
        soup = BeautifulSoup(html, "html.parser")
        imgNum = 1
        try:
            x = soup.find('div',  {'class':'NewPages'}).ul.li.a.string
            # print(x)
            imgNum = int(re.findall(r"\d+\.?\d*",x)[0])
        except:
            pass
        print(imgNum)
        return imgNum
    
    def getImgPageUrl(self, url, imgNum):
        imgPageUrl = [url]
        if imgNum ==1:
            pass
        else:
            for i in range(2, imgNum+1):
                x = url[0:-4] + '_' + str(i) + '.htm'
                imgPageUrl.append(x)
        return imgPageUrl
    
    def getImgurl(self, url):
        html = self.getHTMLTextRefer(url)
        soup = BeautifulSoup(html, "html.parser")
        imgurl = ''
        x = soup.find("div",{"class":"ImageBody"})
        # print(x)
        try:
            imgurl = x.p.a.img.get('src')
        except:
            imgurl = x.p.img.get('src')
        # print(imgurl)
        return imgurl
    
    def getImgTitle(self, url):
        imgTitle = ''
        imgTitle = re.findall(r"\d+", url)[0]
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
            