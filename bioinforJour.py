from urllib import request
import requests
from bs4 import BeautifulSoup
import os
import socket
import urllib.error
import time

def getHTMLText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        r = requests.get(url, headers = header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
		
def getDocURL(html):
    soup = BeautifulSoup(html, "html.parser")
    docURLs = []
    for i in soup.find_all('a', attrs = {'class':'viewArticleLink'}):
        print(i.get('href'))
        docURLs.append('https://academic.oup.com' + i.get('href'))
    return docURLs
	
def getpdfURL(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    pdfURL = soup.find('meta', attrs = {'name':'citation_pdf_url'}).get('content')
    return pdfURL

def pdfDown(url, root):
    pdfURL = getpdfURL(url)
    if not os.path.exists(root):
        os.makedirs(root)
    fname = root + '//' + pdfURL.split('/')[-1]
    request.urlretrieve (pdfURL, fname)

def main(vol, iss):
    page = 'https://academic.oup.com/bioinformatics/issue/{}/{}'.format(vol, iss)
    html = getHTMLText(page)
    docURLs = getDocURL(html)
    for url in docURLs:
        pdfURL = getpdfURL(url)
        pdfDown(pdfURL, root)
        time.sleep(5)
            
if __name__ == '__main__':
    root = "D://ProgramFiles//bioinformatics"
    vol = 35
    iss = 2
    main(vol, iss)