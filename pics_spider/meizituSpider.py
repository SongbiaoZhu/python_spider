# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:06:14 2019

@author: songbiao

https://www.mzitu.com
"""

import requests
import os
import re
from bs4 import BeautifulSoup

def header(referer):
    headers = {
        'Host': 'i5.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers


def getHTMLText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        r = requests.get(url, headers = header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None
    
    
def getCoverURL(page, year, month):
    html = getHTMLText(page)
    soup = BeautifulSoup(html, "html.parser")
    yearTag = soup.find('div', class_ = 'year', string = re.compile(r"^(%s)年$" %year)).find_next_sibling()
    monthTag = yearTag.find('em', string = re.compile(r"(%s)月$" %month)).parent.find_next_sibling('p', class_ = 'url')
    albumCovers = []
    for tag in monthTag.find_all('a', target = '_blank'):
        print(tag['href'])
        albumCovers.append(tag['href'])
    return albumCovers


def getImgNum(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgNum = ''
    try:
        imgNum = soup.find('span', string = re.compile('下一页')).parent.previous_sibling.span.string
    except:
        pass
    return imgNum


def getImgTitle(url):
    imgTitle = url.split('/')[-1]
    return imgTitle


def getAlbumURL(url, imgNum):
    albumURL = [url]
    for i in range(2,int(imgNum)+1):
        albumURL.append(url + '/' + str(i))
    return albumURL


def getImgurl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    imgurl = ''
    imgurl = soup.find('div', class_ = 'main-image').img['src']
    return imgurl


def downloadImage(imgurl, root, imgTitle):
    path = root + imgTitle
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        os.mkdir(path)
    path = path + '//' + imgurl.split('/')[-1]
    try:
        if not os.path.exists(path):
            r = requests.get(imgurl, headers = header(imgurl))
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('图片保存成功')
        else:
            print('图片已存在')
    except:
        print("图片保存失败")


def main():
    '''
    Input:年份和月份
    '''
    year = str(2019)
    month = str(2)# 2019-6, 2019-7已下载
    
    '''
    Process:爬取mzitu图片
    '''
    root = "F:/LifeLibrary/pics/pythonSpider/mzitu/"
    page = "https://www.mzitu.com/all/"
    albumCovers = getCoverURL(page, year, month)
    for url in albumCovers:
        imgNum = getImgNum(url)
        imgTitle = getImgTitle(url)
        albumURL = getAlbumURL(url, imgNum)
        for url in albumURL:
            imgurl = getImgurl(url)
            downloadImage(imgurl, root, imgTitle)
    
    '''
    Output:分专辑编号的文件夹保存图片
    '''

if __name__ == '__main__':
    main()