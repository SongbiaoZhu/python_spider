# -*- coding: utf-8 -*-
"""
爬取王者荣耀所有英雄的皮肤图片
Created on Sun Jan  5 17:15:47 2020
参考博客：https://blog.csdn.net/yuan_yang/article/details/83716315
@author: samsung
警告：本代码所爬取的图片仅供个人学习，严谨用于任何商业用途！
"""
import requests
import os
import re

def getHTMLText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        r = requests.get(url, headers = header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None

def getHeroList(url):
    html = getHTMLText(url)
    heroList = re.findall('"ename":(\d+),"cname":"(\S+?)".*?skin_name":"(.*?)"', html)
    return heroList

def getSkinInfo(heroList):
    skinName = []
    skinUrl = []
    for x in heroList:
        skins = x[2].split('|')
        for s in skins:
            name = x[0] + '_' + x[1] + '_' + s + '.jpeg'
            skinName.append(name)
        num = len(skins)
        for i in range(1,num+1):
            url =  'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(x[0], x[0], str(i))
            skinUrl.append(url)
    skinInfo = dict(zip(skinName, skinUrl))
    return skinInfo

def downloadImage(imgurl, imgTitle):
    path = out_dir + imgTitle
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    try:
        if not os.path.exists(path):
            r = requests.get(imgurl, 
                             headers = {
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
                                        })
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print(imgTitle + '图片保存成功')
        else:
            print(imgTitle + '图片已存在')
    except:
        print(imgTitle + "图片保存失败") 

def main():
    heroList = getHeroList(url)
    skinInfo = getSkinInfo(heroList)
    for k, v in skinInfo.items():
        imgTitle = k
        imgurl = v
        downloadImage(imgurl, imgTitle)
        
if __name__ == '__main__':
    url = 'http://pvp.qq.com/web201605/js/herolist.json'
    out_dir = 'F:/LifeLibrary/pics/pics_spider/KingSkin/'
    main()