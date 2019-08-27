# 统计指定路径下文件数量 python

[TOC]

## IPO

目的：统计出指定文件夹下所有的子文件夹的数量、所有子孙文件的数量

Input：要统计的文件夹路径path

Process：遍历所有文件夹并计数子文件夹数量以及子孙文件数量

Output：统计出的路径下所有子文件夹数量、所有子孙文件的数量



## Code

getFilesNum.py

```python
# -*- coding: utf-8 -*-
import os
 
path = 'F:\\pics\\mzitu'
 
num_dirs = 0 #路径下文件夹数量
num_files = 0 #路径下文件数量(包括文件夹)
num_files_rec = 0 #路径下文件数量,包括子文件夹里的文件数量，不包括空文件夹
 
 
for root,dirs,files in os.walk(path):    #遍历统计
        for each in files:
                if each[-2:] == '.o':
                        print(root,dirs,each)
                num_files_rec += 1
        for name in dirs:
                num_dirs += 1
                print(os.path.join(root,name))
 
for fn in os.listdir(path):
        num_files += 1
        print(fn)
 
print(num_dirs)
print(num_files)
print(num_files_rec)
print('该路径下文件总数为{}'.format(num_files_rec-num_dirs))
```



## 思考

* 该方法统计出的子文件夹数量即是实际的子文件夹数量，包含空的子文件夹
* 统计出的路径下的文件总数，并不包含空的子文件夹。

## 致谢

* Python2 code [blog.csdn](https://blog.csdn.net/u011452172/article/details/78846692)