# -*- coding: utf-8 -*-
"""
crawCellAbstract
Not finished
因为我也不知道这个代码要实现什么功能，以后再看需求写。
Created on Mon Aug 19 16:08:13 2019

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import calendar
import datetime

def getHTMLText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        r = requests.get(url, headers = header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
    
def getIssueInfo(url):
    '''
    get every issue's date,issue No, issue URL, and Volume No on the Archive page
    '''
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    issDate = []
    issURL = []
    issNo = []
    for x in soup.find_all(class_ = 'issueLinkCon'):
        issDate.append(x.strong.string)
        issURL.append('https://www.cell.com' + x.get('href'))
        issNo.append(x.contents[-1])
    return issDate, issURL, issNo
    
        
def getIssueItem(url):
    '''
    get every article's URL, title, brief on each issue page
    title and brief was contents, are list containing list.
    '''
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    textURL = []
    for x in soup.find_all(class_ = 'toc__item__title'):
        print(x.a.get('href'))
        textURL.append('https://www.cell.com' + x.a.get('href'))
    title = []
    for x in soup.find_all(class_ = 'toc__item__title'):
        print(x.a.contents)
        title.append(x.a.contents)
    brief = []
    for x in soup.find_all(class_ = 'toc__item__brief'):
        print(x.contents)
        brief.append(x.contents)
    return textURL, title, brief


def getDocInfo(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        content = soup.find('script', type="application/json").string
        contentDic = json.loads(content)
        docType = contentDic['article']['document-subtype']
        doi = contentDic['article']['doi']
        '''
        一般pubDate一定有,若没有则赋值'31 January 2000'(便于后面识别数据异常)；recDate若没有则取pubDate；revDate若没有则取recDate；accDate若没有则取revDate。
        revise Date可能有多个，这里只取一审revise date
        '''
        try:    
            pubDate = contentDic['article']['dates']['Publication date']
        except:
            pubDate = '31 January 2000'
        try:
            recDate = contentDic['article']['dates']['Received']
        except:
            recDate = pubDate
        try:
            revDate = contentDic['article']['dates']['Revised'][0]
        except:
            revDate = recDate
        try:
            accDate = contentDic['article']['dates']['Accepted']
        except:
            accDate = revDate
        try:
            title = contentDic['article']['title']['content'][-1]['_']
        except:
            title = "Not found title"
        return [docType, doi, recDate, accDate, pubDate,revDate, title]
    except:
        return ["No string found in tag"*7]
        
        
def main():
    '''
    Input:年份和月份，输出txt的名称
    '''
    #year = input('Please input the publication year (2012-present):')
    #month = input('Please input the publication month:')
    #Mon = calendar.month_name[int(month)]
    #yearMon= '{} {}'.format(Mon, year)
    lateThu = getLateThu()
    
    
    years = list(range(2010,2019))
    months = list(range(1,12))
    '''
    Process:爬取指定卷和期的cell paper题目 full-text链接和文章的brief
    '''
    url = 'https://www.cell.com/cell/archive'
    
    
    dataList = [['docType', 'doi', 'recDate', 'accDate', 'pubDate','revDate', 'title','year', 'vol', 'issue']]
    for year in years:
        vol = int(year) - 2002
        for month in months:
            issue = getIssue(month)
            outFname = str(vol) + "_" + str(issue) + "_" + 'pubInfoGPB.txt' 
            page = "https://www.sciencedirect.com/journal/genomics-proteomics-and-bioinformatics/vol/{}/issue/{}".format(vol,issue)
            issuePiis = getIssuePii(page)
            for pii in issuePiis:
                piiURL = getpiiURL(pii)
                dataList.append(getDocInfo(piiURL)+[year, vol, issue])
            with open(outFname, 'w') as f:
                for item in dataList:
                    for i in item:
                        try:
                            f.write("%s\t" % i)
                        except:
                            f.write("\n")
                    f.write("\n")
     
   
if __name__ == '__main__':
    main()