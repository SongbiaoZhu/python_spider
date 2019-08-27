# you-get python视频下载神代码

[TOC]

## 1.项目介绍

### 1).神器库you-get

[source](https://mp.weixin.qq.com/s?__biz=MzI5NDY1MjQzNA==&mid=2247489884&idx=3&sn=cd9a58c76fc125a0a884352095e0ed1f&chksm=ec5ec621db294f3723838170a9bdf800657d2498a7d2da3e379da283890794a4a586a1cf52e5&mpshare=1&scene=24&srcid=&key=447df1e26f054966584eeab3481989defe7c833f55691b9b01d0d5aa8b0577551ec3da7b86a12f333ed1d1e21aff38fcfeff8022b71c42cfa97a8faa902769ef5487aa688b33b8c3c2a4727025d721f2&ascene=14&uin=MTIyODMwMTYxOQ%3D%3D&devicetype=Windows+7&version=62060833&lang=zh_CN&pass_ticket=I1zvUYEN7H4vavRf81KtCjM2oe8JM7saUFo4uH30mKbrrfReMj%2Fkpk72S8iMugIR)

在进入主题之前，先来吐槽下现在的视频网站。各个视频网站内容越来越多，平台强大了就会有诸多的限制，比如超长的广告等待时间、部分内容不允许缓存等，另外对于经常坐飞机或长期处于弱信号条件下的人来说也是个比较头疼的问题。

对于上述问题，今天介绍的这个项目提供了一个很好的解决方案——**只需要1行命令**就能够从各大视频网站中下载想要的视频，而且不必安装视频网站专用APP或者第三方缓存工具。

**You-Get**是GitHub上一个评分很高的python项目，作为一款精巧的命令行应用程序，可以很方便地从web网站下载视频。其下载的视频文件可以直接打开播放，不需要安装特定的网络浏览器，也免去了在线观看广告太长的烦恼。


事实上，you-get不仅能够下载视频文件，还能下载音乐、图片等其他媒体文件，只要你能提供目标资源的URL。只不过，you-get用于下载音乐和图片的功能并不十分完善，而且意义也没有视频下载那样明显，因此本文仅以视频下载为例进行介绍演示。

### 2).支持的网站

you-get的优势之一就是支持包括优酷、爱奇艺、Bilibili、YouTube等几十个国内外知名视频网站（下图只是其中一部分），对于每一个想要下载的视频，都能够使用同一条命令进行直接下载，需要调整的只有目标视频的URL而已。

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tibhoJflIticicX8m5MRBxmJaGZAMPhZHIwHRp8kA5XhV4AnS9PtWQ7R7A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



当然，you-get的使用也有一些注意事项，比如受网页格式调整或反爬措施更改等因素影响，可能会出现部分网站或部分视频源无法下载的问题，对于已经发现的问题会在这里列出，在使用前可以提前查阅；还有就是各视频网站的VIP视频通过you-get是没有办法下载的。



**更重要的是，千万不要使用you-get去做一些可能构成侵犯版权等违法行为的事，对于这一点，you-get已经专门做出了说明**。

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45t69pvWKVviarazmZOfNjt99L4B67C75N48GU1buFgXU2q73ufdSC0SfA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)





## 2.初级应用

### 1).安装与试用

you-get的安装也是老套路了，直接使用"pip install you-get"。

you-get的使用同样简单，只要在终端输入形如"you-get URL(目标视频的url)"的命令就能够自动下载对应的视频。当然，you-get命令还有一些功能参数，其中最为常用的有两个：

- **--info/-i：**加了这个参数，you-get命令仅会显示目标视频的基本信息，而不会开始下载视频。
- **--output-dir/-o：**用于指定下载视频的存储路径。

另外还有其他一些参数，用于实现诸如设置代理、加载cookie、提取目标源URL等功能，详情参见官方文档。下面我们找一段视频试验下you-get的效果，视频网址如下：

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45twcBy2jrtDWWC2WkldzUqS5Xpj7K0BXeFHScqDzUpVdDMsFaEJ1qSoA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

首先使用“-i”参数获取视频的基本信息，按照文档中的示例，在终端中输入：

```
you-get -i 'https://www.bilibili.com/bangumi/play/ss26284'
```

回车后却出现了下图中的提示，很明显是发生了错误，那么该如何解决呢？我们接着往下看。

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tuu6T11B0S08yz6rtsWw4Lq6kPBLrQHECnc15aicI0aMVBLtrywmhOkQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

###  2).问题与调试

按照you-get给出的提示，当下载视频遇到问题时应该分四步来解决：一是排除网络问题；二是确保you-get更新到最新版本；三是检查目标视频是否已经确认无法爬取。很遗憾，这次的问题并不是上面三个原因造成的，所以只能使用第四个方法--debug参数进行调试，调试结果如下图：

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tBbQZ9ic0aCFl7rib7F1wZLeeFtNmWm1jFE8rZDdqL41uCop7FRMEs7BA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



根据debug的调试结果，出现问题的原因是<urlopen error [Errno 11001] getaddrinfo failed>，这个问题通常是由单引号引起的，我们尝试把上面you-get指令中的单引号替换为双引号，输入：

```
you-get -i "https://www.bilibili.com/bangumi/play/ss26284"
```



结果成功获取了目标视频的基本信息：

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45ttgUev8F7ibS5dtJLX84bFbvzeqJB5SwnE5YOFWSdGYzQvGPyicGrxtGw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



可见，目标视频有4种清晰度的格式，接着去掉-i参数正式下载视频（默认会采用第一种视频格式），结果如下：

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45t1QmfpQrXZZ974m7uubDyBrApjTLKAYH4MeDI9r4wlzniaqIW3tgticTw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

只用了十几秒，300多M的视频就下载完毕，速度还是很快的。



##  3.高级用法

上面这种方法一次只能下载一个视频，文档中并没有说明如何批量下载视频，按照目前的方法如果想要批量下载需要多次操作，有点不方便，另外文档中也没有讲如何在代码中以函数的形式调用you-get接口，不过由于项目是开源的，我们可以通过阅读源代码来寻找答案。

### 1).查阅源码

通过查阅项目文件，我们发现在tests目录下有几个py文件：

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tIlGIC9xydhW2UTGI3bEzIqoApxGSrU0ONecib62CBzpeTuhIml0NgSg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

阅读test.py中的代码（下图），初步判定you-get的核心功能存在于“you_get.extractors”之中，形如XXXX.download的函数就是下载接口函数。



![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tdRD7KicJ6Jkrq6fBpYQJ6ZicRhPZb9P0vNAcMSIT7roOqOiadxN7uaurQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

进入到extractors目录，发现里面有很多py文件，每个文件的名称都是一个网站，由此可以推测每个文件中的代码所实现的功能是对应网站中视频/音乐/图片的爬取和下载。

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45trzib56WuuCCjxGoxicMrtOTrhSTqlLG5KtiaHx3L1s1lfXkpIqgcrYQTg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



随便打开一个文件(比如bilibili.py)，看一下代码内容。虽然代码内容很多，但结构还是很清晰的，具体细节暂且略过，直接看代码底部，bilibili.py共定义了两个函数接口——download和download_playlist，通过阅读代码可以得知这两个函数分别用于单个视频下载和批量视频下载。

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45truVYrfRhuZ6tnnzvpQ9PoLjRrGLENLDsxSsZTAef0xdlDhZVEo7LwA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

### 2).批量下载

you-get的命令行参数中并没有对单个视频或者批量视频的甄别，可以推测you-get在封装时已经添加了对单个视频和多个视频进行识别的功能。为了验证，还是用《盾勇》这部动画来进行试验，下图是动画的列表页。

![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tziatLEiaLHHP1Eqic8XJepNKSiagQC5lvBEl6Gicpn8qONYuiascg6GHQrFQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在终端输入下面的下载指令：

```
you-get "https://www.bilibili.com/bangumi/media/md4316482/?from=search&seid=6151030679368490778"
```

you-get会逐个下载列表中的视频，而且对于目录中已经存在的视频还会自动跳过（下图），原来批量下载视频如此简单。



![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tV38Fo73tuuibrxAyIa2vEFmKOHwzeUzpSwAKCx9togoXibPtjsaYRwrQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

###  3).函数调用

虽然顺利找到了批量下载的方法，不过总是在命令行中使用you-get还是感觉有点受限，基于我们前面已经找到了函数接口，不妨试试在python代码中调用you-get的下载函数。



还是以bilibili模块为例，在bilibili.py文件中并没有发现相关的参数设置部分，但是在代码的开头调用了extractor.VideoExtractor函数（下图）。我们顺藤摸瓜，在这个函数中找到了参数设置的相关内容，比如info_only对应的是命令行参数-i，outpath_dir对应的是命令行参数-o，另外在调用函数下载时merge参数是必须设置的(这个参数决定了下载后的媒体文件是否合并，例如有些网站下载的视频文件和音频文件是分开的，merge为True时，下载后会自动将两个文件合并)。



![img](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp0Uupn6DN4Bpicic3QI28t45tSJuyMmpFQCxKI2aBru7Rqeib3yeMQtTCrrKnbHoYnYqM6QOicA4B5IHw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

将下面几行代码保存为python脚本进行运行测试，发现其效果和在终端使用you-get命令行几乎一模一样。

```
from you_get.extractors import bilibilibilibili.download('https://www.bilibili.com/bangumi/play/ep259692', info_only=True)bilibili.download('https://www.bilibili.com/bangumi/play/ep259692', merge=True, output_dir='your dir')
```



现在，我们可以在自己的程序中使用you-get了，感觉灵活性一下子提升了好多。you-get中还有很多神器的功能和设定，就有待于大家自己去挖掘了。

## 学习记录songbiao

### 亲测很好用！

```Python
pip install you-get
# 然后就是命令行终端中输入 you-get "视频url"即开始下载
# you-get --help有选项帮助，很多实用设置选项。--playlist可以直接下载整套播放列表！
```

已经测试了bilibili网站的“生信服务器配置教学视频”可以批量下载(https://www.bilibili.com/video/av31349855),

对于下载的Flv格式的视频，下载官网的射手影音或者VLC 可以很方便的播放。

### Detail 参考信息

[You-Get](https://you-get.org/)

```Python
# Set the path and name of downloaded file
you-get -o F:\video_download "https://v.qq.com/x/cover/o3l4t2nttlyshx8.html"

# Watch a video
$ you-get -p vlc 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
$ you-get -p chromium 'https://www.youtube.com/watch?v=jNQXAC9IVRw'

```

## Known bugs

[find_answer_here](https://github.com/soimort/you-get/wiki/Known-Bugs)