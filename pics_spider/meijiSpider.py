# -*- coding: utf-8 -*-
"""
pics_spider
http://www.zipdsl.com
input the category and album date to crawl
WARNING: Do not use the images crawled with this script for commercial use!!

Created on Thu Jan  2 13:48:14 2020

@author: samsung
"""

import requests
import os
from bs4 import BeautifulSoup 
import bs4

def getHTMLText(url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        try:
            r = requests.get(url, headers = header, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return None

def getCoverURL(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    albumCovers = []
    for x in soup.findAll('url'):
        if x.loc.string.endswith('.html'):
            print(x.loc.string)
            albumCovers.append(x.loc.string)
    return albumCovers

def getImgurl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgurl = []
    for child in soup.find("div",{"class":"art_body"}).children:
        if isinstance(child,bs4.element.Tag):
            print(child.get('src'))
            imgurl.append(child.get('src'))
    return imgurl

def getImgTitle(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgTitle = ''
    imgTitle = soup.find('title').string[0:-6]
    return imgTitle

def downloadImage(imgurl, imgTitle):
    path = out_dir + imgTitle
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
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
        
def main():
    albumCovers = getCoverURL(page)
    for url in albumCovers[0:albumNum]:
        imgTitle = getImgTitle(url)
        imgurl = getImgurl(url)
        for x in imgurl:
            downloadImage(x, imgTitle)
                
page = 'http://www.zipdsl.com/sitemap.xml'
out_dir = 'F:/LifeLibrary/pics/pics_spider/meiji/'
albumNum = 5

if __name__ == '__main__':
    main()