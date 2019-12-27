# -*- coding: utf-8 -*-
"""
7160图片大全--输入图片分类和要爬取页数，即开始爬取。
校花分类有点bug,只下载专辑封面图片。
Created on Thu Aug 15 21:56:44 2019

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

def getCoverURL(page, oriPage):
    html = getHTMLText(page)
    soup = BeautifulSoup(html, "html.parser")
    albumCovers = []
    for x in soup.find_all('a',target="_blank"):
        if x.parent.name == 'li':
            print(x.get('href'))
            albumCovers.append(oriPage + x.get('href')[1:])
        else:
            pass
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
    for i in range(2,int(imgNum)+1):
        albumURLs.append(url + 'index_' + str(i) + '.html')
    return albumURLs


def getImgurl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgurl = ""
    try:
        imgurl= soup.find(attrs = {'class':'picsbox picsboxcenter'}).img.get('src')
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
    pages = []
    if pinyin(category) == "qingchunmeinv":
        for i in range(1, pageNum+1):
            pages.append(oriPage + pinyin(category) + "/" + "list_2_" + str(i) + ".html")
    elif pinyin(category) == "meinvmingxing":
        for i in range(1, pageNum+1):
            pages.append(oriPage + pinyin(category) + "/" + "list_5_" + str(i) + ".html")
    elif pinyin(category) == "weimeitupian":
        for i in range(1, pageNum+1):
            pages.append(oriPage + pinyin(category) + "/" + "list_13_" + str(i) + ".html")
    elif pinyin(category) == "fengjing":
        for i in range(1, pageNum+1):
            pages.append(oriPage + pinyin(category) + "/" + "list_14_" + str(i) + ".html")
    elif pinyin(category) == "meishitupian":
        for i in range(1, pageNum+1):
            pages.append(oriPage + pinyin(category) + "/" + "list_15_" + str(i) + ".html")
    elif pinyin(category) == "xiaohua":
        for i in range(1, pageNum+1):
            pages.append(oriPage + pinyin(category) + "/" + "list_6_" + str(i) + ".html")
    elif pinyin(category) == "rentiyishu":
        for i in range(1, pageNum+1):
            pages.append(oriPage + pinyin(category) + "/" + "list_1_" + str(i) + ".html")
    else:
        print("没有该分类图片")
            
    return pages


def main():
    category = str(input("请输入一个专题分类汉字或拼音（清纯美女、美女明星、唯美图片、风景、美食图片、校花、人体艺术）:")) 
    pageNum = int(input("Enter pages:"))
    root = "F://pics//pics7160//" + pinyin(category) + "//"
    oriPage = "https://www.7160.com/"
    pages = getPages(oriPage, pageNum, category)
    for page in pages:
        albumCovers = getCoverURL(page, oriPage)
        for url in albumCovers:
            imgNum = getImgNum(url)
            albumURLs = getAlbumSet(url,imgNum)
            for url in albumURLs:
                imgurl = getImgurl(url)
                downloadImage(imgurl,root)

if __name__ == '__main__':
    main()