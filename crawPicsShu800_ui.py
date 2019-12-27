# -*- coding: utf-8 -*-
"""
http://www.shu800.com/?btwaf=71953176

输入要下载的图片分类和要下载的页数即可爬取。

Created on Fri Aug 16 10:49:41 2019

@author: samsung
"""


import requests
import os
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
    
def getCoverURL(page, oriPage):
    html = getHTMLText(page)
    soup = BeautifulSoup(html, "html.parser")
    albumCovers = []
    for x in soup.find_all(attrs = {'class':'dl-pic'}):
        albumCovers.append(oriPage + x.get('href')[1:])
    return albumCovers


def getImgNum(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgNum = ""
    imgNum = soup.find("em").string[2:]
    return imgNum


def getAlbumSet(url,imgNum):
    albumURLs = [url]
    for i in range(2,int(imgNum)+1):
        albumURLs.append(url.split(".html")[0] + "_" + str(i) + ".html")
    return albumURLs

def getAlbumTitle(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    title = ""
    title = soup.find('title').string.split('-')[0]
    return title


def getImgurl(url, title):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgurl = ""
    try:
        imgurl = soup.find('img', alt = title).get('src')
    except:
        pass
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
    pages = [oriPage + pinyin(category) + "/"]
    for i in range(2, pageNum+1):
        pages.append(oriPage + pinyin(category) + "/" + "index_" + str(i) + ".html")
    return pages
            

def main():
    category = str(input("请输入一个专题分类的汉字或拼音（性感、清纯、明星）:")) 
    pageNum = int(input("请输入要下载的页数（大于等于2）:"))
    root = "F://pics//shu800//" + pinyin(category) + "//"
    oriPage = "http://www.shu800.com/"
    pages = getPages(oriPage, pageNum, category)
    for page in pages:
        albumCovers = getCoverURL(page, oriPage)
        for url in albumCovers:
            imgNum = getImgNum(url)
            albumURLs = getAlbumSet(url,imgNum)
            for url in albumURLs:
                title = getAlbumTitle(url)
                imgurl = getImgurl(url, title)
                downloadImage(imgurl,root)

if __name__ == '__main__':
    main()