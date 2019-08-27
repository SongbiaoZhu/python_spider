# 合并同一个文件夹下多个txt python

[TOC]

## IPO

Input，输入要合并的txt所在的文件夹路径和合并后生成的txt文档名称。

Process，遍历读取该文件夹下所有txt文档的内容，并且逐个换行写入merged.txt。

Output，合并后生成的txt文档和耗时。

Below both codes worked.

## code

```python
# -*- coding:utf-8*-
'''
mergeTextContent
python3
'''
import os
import os.path
import time

time1=time.time()
##########################合并同一个文件夹下多个txt################
def MergeTxt(filepath,outfile):
  k = open(filepath + '/' +outfile, 'a+')
  for parent, dirnames, filenames in os.walk(filepath):
    for filepath in filenames:
      txtPath = os.path.join(parent, filepath) # txtpath就是所有文件夹的路径
      f = open(txtPath)
      ##########换行写入##################
      k.write(f.read()+"\n")
  k.close()
  print("finished")
if __name__ == '__main__':
  filepath="C:/Users/samsung/Desktop/txts"
  outfile="merged.txt"
  MergeTxt(filepath,outfile)
  time2 = time.time()
  print('总共耗时：' ,str(time2 - time1) ,'s')
```

## 第二种code

```python
'''
mergeTxtContent_2
'''
import os
import os.path #文件夹遍历函数  
#获取目标文件夹的路径
filedir = 'C:/Users/samsung/Desktop/txts'
#获取当前文件夹中的文件名称列表  
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open(filedir + '/' + 'result.txt','w')
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath):
        f.writelines(line)
    f.write('\n')
#关闭文件
f.close()
```



## 致谢

* [python2_code](https://www.jb51.net/article/138936.htm)

* [blog](https://www.cnblogs.com/wxj1129549016/p/9533797.html)