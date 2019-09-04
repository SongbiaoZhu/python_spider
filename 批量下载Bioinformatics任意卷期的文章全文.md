# 批量下载Bioinformatics任意卷期的文章全文

[TOC]

## 目的

批量下载[Bioinformatics](https://academic.oup.com/bioinformatics/) （impact factor: 4.5,  Mathematical & Computational Biology
4 out of 59)杂志的某一卷期的全文pdf文档，便于学习bioinformatics的前沿技术和方法。

## 策略

1. 输入卷 期信息
2. 在页面中提取每一篇文章的 href，（每一篇文章的题目、年份、doi等信息，本代码暂不爬取）
3. 在每一篇文章的href打开的页面中找到 citation_pdf_url的content
4. 对于每一个citation_pdf_url获取pdf全文

## 脚本

`bioinformaticSpider.py`，完整代码如下：

本代码主要分为解决两个问题的内容，如下：

1. 爬取指定卷期的所有文章的pdfURLs，并将该pdfURLs写入txt文档。
2. 将pdfURLs中每一篇文章对应的pdf全文链接的url，使用selenium进行下载pdf全文至本地存储。

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:06:16 2019

@author: samsung
"""

import requests
from bs4 import BeautifulSoup
import os

import random
from selenium import webdriver
from time import sleep

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
        #print(i.get('href'))
        docURLs.append('https://academic.oup.com' + i.get('href'))
    return docURLs
	
def getpdfURL(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    pdfURL = soup.find('meta', attrs = {'name':'citation_pdf_url'}).get('content')
    #print(pdfURL)
    return pdfURL

def main(page, fname):
    html = getHTMLText(page)
    docURLs = getDocURL(html)
    pdfURLs = []
    for url in docURLs:
        pdfURL = getpdfURL(url)
        pdfURLs.append(pdfURL)
    with open(fname,'w') as f:
        for line in pdfURLs:
            f.write(line)
            f.write('\n')
    return pdfURLs
            
if __name__ == '__main__':
    vol = 34
    iss = 2
    page = 'https://academic.oup.com/bioinformatics/issue/{}/{}'.format(vol, iss)
    root = "D:\\ProgramFiles\\bioinformatics"
    fname = os.path.join(root, 'pdfURLs_{}_{}.txt'.format(vol, iss))
    pdfURLs = main(page, fname)
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', 'D:\\ProgramFiles\\bioinformatics')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
    driver = webdriver.Firefox(firefox_profile=profile)
    for i in pdfURLs:
        try:
            print(i)
            driver.get(i)
            sleep(random.randint(5,10))
            driver.find_element_by_id("download").click()
            sleep(random.randint(30,45))
        except:
            continue
    driver.quit()
```

本脚本中，

* 第一个问题（爬取指定卷期的所有文章的pdfURLs，并将该pdfURLs写入txt文档）的解决比较容易，是使用requests进行常规爬取的方法；

* 第二个问题（将pdfURLs中每一篇文章对应的pdf全文链接的url，使用selenium进行下载pdf全文至本地存储。）的解决破费了一番周折，因为我首先是参考`gepia.py`脚本中的方法用`urllib.urlretrieve`的方法进行保存pdf文档，结果发现在爬取第一篇之后就被对方主机断开连接，我检查问题发现，保存的pdfURL地址，粘贴到浏览器中去访问时就发现url会多出token 的字段，很长的随机字段，浏览器可以根据输入的pdfURL自动跳转到含有token 的url，然后打开页面显示pdf全文，而`urllib.urlretrieve`设置了sleep 以及request中设置了timeout 都无法解决这个问题，总是被对方主机主动断开链接（`ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。`）。
* 为了解决第二个问题，查阅了图书馆书籍，发现可能通过selenium可以解决这一问题，因为selenium就是操作浏览器来访问，而上述尝试时知道浏览器是可以跳转到含有token 的url地址的。所以就自学了selenium的方法，首先取一个pdfURL进行测试，发现可以打开显示全文，可是第二次再打开时就马上被断开连接了。这说明对方主机也侦查到了爬虫行为，然后就将我的IP地址加入了黑名单。所以我第二天就设置了sleep时间，见代码中`sleep(random.randint(5,10))`, `sleep(random.randint(30,45))`，就是尽量1min左右下载一篇pdf ，如此虽然时间边长，但是成功的下载了整期的pdf全文，没有被断开连接。这也说明之前嵩天老师说的，爬虫不被禁止的办法就是让爬虫像正常人一样的访问频率，不给对方造成访问负担。如此虽然慢了时间，但是多出来的时间还是解放了劳动力的自由支配之间。

## 示例含有token 的url链接

看起来是没有什么规律的，所以判断是随机生成的。

```
https://watermark.silverchair.com/bty462.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAnEwggJtBgkqhkiG9w0BBwagggJeMIICWgIBADCCAlMGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMkwUjAntYukvUIXgNAgEQgIICJFA43b9GG1Dx2wAAkwBwa_hMgRsPnrehOHe6rhMAjeNcZb-L8xBOdWD8kSR0zN-ij_ScRpsmI4fxHrp5vNMwFLco6vkJIYetyoOXoX2Ipoht0aIMleiQqq0e6XtMVepW3o7E3NCQwbDZSWC9nviqyM36h2t_MTPTPXTb2NwdlqKuvOLupElFAj2jgrst3ai1dj-3b2swRXY5X4wsAUQOYjTbuIavqDubWQhO3Dk3UhLDE0J0dtSf9_yc3unNxLPZmMRtsC4i6aTUpet1kR2Ebd0T8cdwYOcrlhKnbik_4nIBqXcqLpEUobK6k7fwSzWp2Mv7DzarlKFfYMXDmgPk9bPd2B9eIY6GEJcAIk4ZSSvzPMe8wEoyliFE1bpxwlEY0glqQtKSPe2nWxN5l1NDxcjEu1KsipgU8kGOzyWCaxGLF6HAeTpAcury8oBSul7jLhoKhIyPo7SM6vX6_hi6djWxCVnwWitofcQNTx9UM_-q7XpB_c7IxUA3delQ9vdzgE7SF6g5cjRMJ5IgGDk3AhVf9wl91ZKelGmtSFVLbCABW-RH0-ztPPEgvlFLvh9AI5W_vm8OQmMNfaol6Vc0wvs_ajoQTKw3AK76e0XsGYaEV6ykYOy7c7ux7X-h2dnJRQrvIsY5fy-vDV_V6ZIt2AouWTqVXoeUhH8GlRptERuJ6f4eMjqi-VVpYhoQHjzVi22UIfIAvzNklTi6Pd-TiEIrxbuS
https://watermark.silverchair.com/bty511.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAnEwggJtBgkqhkiG9w0BBwagggJeMIICWgIBADCCAlMGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMXy36dXViDVhidIuAAgEQgIICJDVsMybV8ysgG9-Foinppg-Bpw0oN2dzUR2DsSfkF1H9CVzRtRChL7g953YIdMGXY93UHMJ-YVhv4JRYdcoZOGq5sMCmEsSzGGrX_g237e_diuq7vaBl6thvEPcLAav5MLK-CAaJFjSNsE8k9zmZgG3MgunYiiFAVYTAPDL2Dywiiy8MKVP49i9ssva5OpmqexAgMY_qkUK0RPzWNYrRe0AL40JLZzylL1IZtlGn3Y-Q8mgmeM10GbiLV0mxWvHWC4oFRoeLrzuqN6q-2DfqoyNOCxFHy1YkU9XpstwpbI5PASFzQqJXlmPrI_6BBzYLRZaeS7Yanypbl6Wni_FPEjGH_mp5sKbKU6bFSyAazoGcdloD-Qx10uG435URtb7oouDAskAmnwO97d7X4hABO-YYH4toQfFCAr8bnJyThILoP4WqjA3Y-A-7FdoIKf_Y8lPGpm3u5Tv9uW4rT2ndYxg6S179TivmwHJufhqRY4GQxHl0GYXcbCVpl8UPVzh_zVc2SUTYN5ebkmMbG2aJ9-8u06vCgNtQHCMf8lvWavS2Pbbfkbx5UFMKzM0C-Cp5wb67N2xJPuJASUiWKZGd8KHxRKEAfDyUiXakjVOvuXOIBlGpotlx7J_9sMRFnL5a-mbsc-5Ba1ke2vKdHjE_H8kqFrw20FSQS2EWCn2c7wvjy4YixuAAe54nBpdWChWjR8k_m2cMLAMbjWMf9va4AVyGjaBT

```

## 知识点总结

- python selenium， 另外总结了一份文档`Selenium 报错提示.md`，本文不再赘述。
- selenium使用时，对于第一篇文章的下载，会提示一个保存文档的窗口，对于第一篇文章，需要用鼠标操作勾选上均使用同样的操作，然后再点击保存。之后，后续的pdfURL下载时就可以不弹出窗口自动下载pdf了。

