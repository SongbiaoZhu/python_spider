# 反爬虫技术-Python

[TOC]

## 概述

网络爬虫，是一个自动提取网页的程序，它为搜索引擎从万维网上下载网页，是搜索引擎的重要组成。

但是当网络爬虫被滥用后，互联网上就出现太多同质的东西，原创得不到保护。

于是，很多网站开始反网络爬虫,想方设法保护自己的内容。

他们根据ip访问频率，浏览网页速度，账户登录，输入验证码，flash封装，ajax混淆，js加密，图片等技术，来应对网络爬虫。

## 四种主要策略

一： User-Agent +Referer检测
二： js混淆和渲染
三：IP限制频次
四：验证码

[参考博客](https://www.cnblogs.com/xiao-apple36/p/8746730.html)

## 伪装并且随机使用不同的header

**What is http request header?**

Generally speaking, http requestion header are some messages which  are sent to web servers. Web servers will check them and implement  different process.

For example, some web severs will check the **user-agent** header, if your application does not send it to server, the server may refuse your request and you will not get web page data.

**What headers we shoud use?**

The simple way to know what http request header you can use is to open your browser. and press ***F12***, then open a site, such as google.com.

You will find some http request header in your browser.

![http request header](https://www.tutorialexample.com/wp-content/uploads/2019/07/http-request-header.png)

**Here we list some common used headers.**

| Name            | Value                                                        |
| --------------- | ------------------------------------------------------------ |
| Accept          | text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8 |
| Accept-Encoding | gzip, deflate, br                                            |
| Accept-Language | en-US                                                        |
| Cache-Control   | no-cache                                                     |
| Cookie          | get and save it                                              |
| Host            | such as tutorialexample.com                                  |
| Referer         | such as https://www.tutorialexample.com                      |
| User-Agent      | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 |

**轮换User-Agent**：[如何伪装并轮换User-Agent 使用 Python 3](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)

User-Agent的列表，最好去该[网站](https://developers.whatismybrowser.com/useragents/explore/)下载比较新的还在使用的，推荐的做法就是在爬取开始之前，先去爬取比较新的User-Agent list。

同时收藏一个stackoverflow优质问答，提供了一个随机获得User-Agent的第三方库的使用方法，[stackOverflow](https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit)

```python
# Provide a User-Agent header:
import requests

url = 'http://www.ichangtou.com/#company:data_000008.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
print(response.content)


# a pretty useful third-party package called fake-useragent that provides a nice abstraction layer over user agents:

from fake_useragent import UserAgent
import requests

ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)
url = "https://www.hybrid-analysis.com/recent-submissions?filter=file&sort=^timestamp"
htmlContent = requests.get(url, headers=header)
print(htmlContent)
```

**修改Referer**

收藏一个stackoverflow优质问答，提供了如何[Changing the referer URL in python requests](https://stackoverflow.com/questions/20837786/changing-the-referer-url-in-python-requests)



**注意**：如果在不改变IP地址的情况下，去使用不同的header反而更容易被反爬技术识别出来，所以改变header应该和随机使用不同的IP address结合使用。

## 随机使用不同的代理和IP地址

Perfect介绍：[How To Rotate Proxies and IP Addresses using Python 3](https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/)

Using **proxies** and **rotating IP addresses** in combination with **rotating user agents** 可以很有效的帮你克服反爬技术。

推荐一个提供了免费代理的网站， https://free-proxy-list.net/.好的做法是每次爬取之前先爬取新的代理地址。