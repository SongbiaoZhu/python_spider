# -*- coding: utf-8 -*-
"""
crawGPBDates
Created on Sun Aug 18 13:06:33 2019

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import json


def getIssue(month):
    month = int(month)
    if month % 2 == 0:
        issue = int(month/2)
    if month % 2 != 0:
        issue = int((month+1)/2)
    else:
        pass
    return issue


def getHTMLText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        r = requests.get(url, headers = header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
    
def getIssuePii(page):
    html = getHTMLText(page)
    soup = BeautifulSoup(html, "html.parser")
    issuePiis = []
    for i in soup.find_all('input', attrs = {'name':'pii'}):
        print(i.get('value'))
        issuePiis.append(i.get('value'))
    return issuePiis


def getpiiURL(pii):
    piiURL = 'https://www.sciencedirect.com/science/article/pii/{}'.format(pii)
    return piiURL


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
    years = list(range(2012,2019))
    months = list(range(2,14,2))
    '''
    Process:爬取每卷每期的每篇文献的publication info
    Output: 按期写入text文档
    '''
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