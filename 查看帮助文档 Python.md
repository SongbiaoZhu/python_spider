# 查看帮助文档 Python

[TOC]

## Code

打开cmd命令窗口,输入python,

```
dir('os')
# 查看对象某个属性的帮助文档,要查看’os’的split属性，可以用__doc__
print(’os’.split.__doc__)
# 查看对象的某个属性还可以用help函数，使用方法为help(‘os’.split)
help(‘os’.split)
help('os'.strip)
# 查看某个对象的详细文档用help
#如查看str类型的详细文档可以用help(‘os’)。如果文档的内容很多，help会列出全部文档的一部分，并#在左下角提示“-- More --”，按Enter键盘会显示更多的信息，要回到命令行交互模式可按Ctrl + C。
help(‘os’)

```



## 致谢

* [代码帮](https://www.cnblogs.com/IT-LearnHall/p/9426362.html)