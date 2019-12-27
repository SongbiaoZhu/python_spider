# -*- coding: utf-8 -*-
"""
# crawPicsUmei
# bugs...
# http://www.umei.cc/meinvtupian/meinvxiezhen/
Created on Fri Aug 16 09:29:12 2019

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
    for x in soup.find_all(attrs = {'class':'TypeBigPics'}):
        print(x.get('href'))
        albumCovers.append(x.get('href'))
    return albumCovers
    

def getImgNum(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgNum = ""
    for x in soup.find_all('a', string = re.compile('^共[\d]')):
        print(x)
        imgNum = ("".join(list(filter(str.isdigit,x.string))))
    return imgNum

    

def getAlbumSet(url,imgNum):
    albumURLs = [url]
    for i in range(1,int(imgNum)-1):
        albumURLs.append(url.split(".htm")[0] + "_" + str(i) + ".htm")
    return albumURLs


def getImgurl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgurl = ""
    imgurl= soup.find('p', align="center").img.get('src')
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
    page = ""
    page = oriPage + pinyin(category) + "/"
    pages = [page]
    for i in range(2, pageNum+1):
        pages.append(oriPage + pinyin(category) + "/" + str(i) + ".htm")
    return pages


def main():
    category = str(input("请输入一个专题分类汉字或拼音（美女写真）:")) 
    pageNum = int(input("Enter pages:"))
    root = "F://pics//umei//" + pinyin(category) + "//"
    oriPage = "http://www.umei.cc/meinvtupian/"
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

