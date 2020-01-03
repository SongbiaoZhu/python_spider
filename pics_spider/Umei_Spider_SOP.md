# Umei_Spider_SOP

[TOC]

## Start Crawl preparation

http://www.umei.cc/

1. http://www.umei.cc/robots.txt
User-agent:*
Disallow: /?*
Disallow: /#*

2. Next, pick a picture, try the downloadImage(imgurl, imgTitle) function

    ```python
    import requests
    import os
    from bs4 import BeautifulSoup 
    import bs4
    
    def getHTMLText(url):
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
            try:
                r = requests.get(url, headers = header, timeout=30)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                return r.text
            except:
                return None
    def downloadImage(imgurl, imgTitle):
        path = out_dir + imgTitle
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + '//' + imgurl.split('/')[-1]
        try:
            if not os.path.exists(path):
                r = requests.get(imgurl, 
                                 headers = {
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
                                            })
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print('图片保存成功')
            else:
                print('图片已存在')
        except:
            print("图片保存失败")
    out_dir = 'F:/LifeLibrary/pics/pics_spider/Umei/'
    imgTitle = 'test.jpeg'
    imgurl = 'http://i1.shaodiyejin.com/uploads/tu/201911/9999/9d2d9c35fb.jpg'
    downloadImage(imgurl, imgTitle)
    ```

    Yes, a test picture has been successfully downloaded. So no special anti-robots needed.

## Crawl steps

1. Look into the website, check the pics arrangement structure, start from the sitemap page is the best way. The sitemap page is http://www.umei.cc/about/sitemap.htm, Check the sitemap source code, use the catrgory meinvtupian as example to start crawl.
2. click a sub-category, eg meinvxiezhen,  see the url site.
3. so based on the category and sub-category, construct the url.
4. Crawl the corresponding subcategory page,  get the last page number, 
5. Based on the last page number, construct the Url
6. Crawl every Url , get all the albums URL in each page number
7. Crawl albumCover page, get all the imgUrl
8. Download every picture

