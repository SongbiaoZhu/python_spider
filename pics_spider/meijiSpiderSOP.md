# meijiSpiderSOP

[TOC]

## 1. robots.txt
User-agent: *
Disallow: /data
Disallow: /include
Disallow: /install
Disallow: /plus/search.php
Disallow: /templets

Sitemap: http://www.zipdsl.com/sitemap.xml

**SOP means the workflow of the script.**

## 2. view the source of the sitemap url, so start from the sitemap

## 3. steps:
First， crawl all the urls in the sitemap. 
Second, filterd out the album urls (remove the homepage urls of ecery category). 
Third, based on the input albumNum (set 5)，crawl the first 5 ablums. Crawl all the image URLs of ervery ablum url. 
Fourth, crawl every picture.

## Time

1 hour later, finish script。
20 minutes later, finished the object oritation programming version script.