# python爬取美桌网图片

## 代码功能

[美桌](http://www.win4000.com/)

点击查看这个网站中的页面分类，发现有一些分类下有重复，从页面存放的规整性下看，以下三个大分类下的图片可以方便抓取。

* 首页--桌面壁纸 可以选一个分类，如美女壁纸。(craw_win4000_bizhi.py)

* 首页--壁纸专题下可以选一个分类，如写真壁纸，清纯美女壁纸。（craw_win4000_xiezhen.py）

* 首页--明星图片 下可以点击选任一个明星，进行爬取该明星的图片。(craw_win4000_mingxing.py) 

以上三个分类的python代码我已经写完，并且都已成功运行。

## 程序主体结构

以上三个程序，主体结构一样，不同的是起始网页url，以及query关键词，和对应的标签筛选过程。

1. 打开上述份分类页面
2. 爬取页面中每一套图的网址（一般每页24套图）
3. 每一套图的网址中爬取套图下每张图的网页地址（每套图下有数量不等的图片，每个图片对应一个网址）
4. 每张图的网页地址中爬取每张图片的图片网址
5. 根据每张图片的图片网址下载并保存图片
6. 循环以上2-5步，爬取第1步打开的该分类下的后续页面（美桌网每个分类下一般都是有5页，所以pageNum = 5）
