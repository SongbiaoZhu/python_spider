# Python开发环境Anaconda3使用

[TOC]

## IDLE简介

* Python IDLE，快捷，略显简陋，对Python内功（代码编写和调试）要求也高，并且每个扩展库都需要自己安装和配置。

* Anaconda3、PyCharm或其他开发环境，而在众多Python开发环境中，Anaconda3因为集成安装大量扩展库，受人欢迎。

## Anaconda3介绍

下载安装Python3.7版本的[Anaconda3](https://www.anaconda.com/distribution/#download-section)

有推荐的[Anaconda Documentation](https://docs.anaconda.com/anaconda/user-guide/getting-started/)

安装完成以后，开始菜单栏打开Anaconda3文件夹就可以看到同时安装的Spyder IDLE，点击既可以运行Spyder.

## Spyder 界面简介

打开spyder界面，主要分为三个窗口，简介：

1. Editor窗口：即左边的窗口。可以用来写代码，之后用菜单栏的绿色按钮运行。
2. python console/history log/ipython console窗口：即右下角的窗口。python console/ipython console是控制台，分别相当于python和ipython的命令行窗口，可以直接在窗口里输入代码，敲回车就能执行上一行。可以参考[python和ipython的区别博文](http://blog.sina.com.cn/s/blog_6fb8aa0d0101r5o1.html)
简而言之就是ipython在python的基础上添加了若干功能。history log相当于历史记录，记录之前在命令行输入过的代码。
3. variable explorer/file explorer/help 分别显示现有的变量、文件，和帮助。

## Spyder中安装第三方库

Spyder中安装第三方库：在控制台输入 !pip install 包的名称

```python
!pip install pypinyin
```

