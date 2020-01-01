# -*- coding: utf-8 -*-
"""
pics_spider
https://www.plmm.com.cn
input category and index
WARNING: Do not use the images crawled with this script for commercial use!!
Created on Wed Jan  1 22:23:43 2020

@author: samsung
"""

import requests
import os
from bs4 import BeautifulSoup 

def getHTMLText(url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        try:
            r = requests.get(url, headers = header, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return None

def getpageUrl(category, index):
    pageUrl = page + category
    if index ==1:
        pageUrl +=  '/index.html'
    else:
        pageUrl += '/index_' + str(index) + '.html'
    return pageUrl
       
def getCoverURL(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    albumCovers = []
    for x in soup.findAll(attrs = {'class':'figure figure-img'}):
        print(x.a['href'])
        albumCovers.append('https:' + x.a['href'])
    return albumCovers

def getImgurl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgurl = []
    for x in soup.findAll(attrs = {'class':'demo-gallery__img--main'}):
        print(x['href'])
        imgurl.append('https:' + x['href'])
    return imgurl

def getImgTitle(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgTitle = ''
    imgTitle = soup.find('title').string.split('_')[0]
    return imgTitle

def downloadImage(imgurl, imgTitle):
    path = out_dir + imgTitle
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
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
        
def main():
    pageUrl = getpageUrl(category, index)
    albumCovers = getCoverURL(pageUrl)
    for url in albumCovers:
        imgTitle = getImgTitle(url)
        imgurl = getImgurl(url)
        for x in imgurl:
            downloadImage(x, imgTitle)
                
CATEGORY = ['xinggan', 'qingchun', 'meinv', 'chemo', 'qipao']
page = 'https://www.plmm.com.cn/'  
out_dir = 'F:/LifeLibrary/pics/pics_spider/plmm/'
category = 'qingchun'
index = 1

if __name__ == '__main__':
    main()