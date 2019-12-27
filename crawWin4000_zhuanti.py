# -*- coding: utf-8 -*-
"""
Craw_win4000_bizhi

首页-壁纸专题-自然风光
修改category 和pageNum即可爬取其他分类的壁纸
Created on Thu Aug 15 16:40:03 2019

@author: samsung

"""

import requests
import os
import re
from bs4 import BeautifulSoup
import pypinyin

def pinyin(query):
    queryEn = ''
    for i in pypinyin.pinyin(query, style = pypinyin.NORMAL):
        queryEn += ''.join(i)
    return queryEn

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def getCoverURL(page):
    html = getHTMLText(page)
    soup = BeautifulSoup(html, "html.parser")
    albumCovers = []
    for x in soup.find_all(href=re.compile("http://www.win4000.com/wallpaper_detail")):
        if x.parent.name == "li":
            print(x.get('href'))
            albumCovers.append(x.get('href'))
    return albumCovers


def getImgNum(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgNum = ""
    imgNum = soup.find("em", string = re.compile("^\\d+$")).string
    return imgNum


def getAlbumSet(url,imgNum):
    albumURLs = [url]
    for i in range(2,int(imgNum)+1):
        albumURLs.append(url.split(".html")[0] + "_" + str(i) + ".html")
    return albumURLs


def getImgurl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgurl = ""
    imgurl= soup.find(attrs = {'class':'pic-large'}).get("src")
    return imgurl
    

def downloadImage(imgurl, root):
    path = root + imgurl.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(imgurl)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('图片保存成功')
        else:
            print('图片已存在')
    except:
        print("图片保存失败")


def getPages(oriPage, pageNum, category):
    pages = []
    for i in range(1, pageNum+1):
        pages.append(oriPage + pinyin(category) + "_" + str(i) + ".html")
    return pages
            

def main():
    category = "自然风光" 
    pageNum = 2
    root = "F://pics//win4000//" + pinyin(category) + "//"
    oriPage = "http://www.win4000.com/zt/"
    pages = getPages(oriPage, pageNum, category)
    for page in pages:
        albumCovers = getCoverURL(page)
        for url in albumCovers:
            imgNum = getImgNum(url)
            albumURLs = getAlbumSet(url,imgNum)
            for url in albumURLs:
                imgurl = getImgurl(url)
                downloadImage(imgurl,root)

if __name__ == '__main__':
    main()
          