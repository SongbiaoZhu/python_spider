# 复制所有子文件夹中的图片到新文件夹中 python

## IPO

Input:请键入需要整理的文件夹地址： E:\myprojectnew\jupyter\整理文件夹\示例

以及 请键入要复制到的文件夹地址：

Process: 遍历所有子文件夹中的图片.jpg, .JPG, .png，然后复制到新的目标文件夹中

Output:存放所有已经复制的图片的文件夹

## Code

```python
# -*- coding: utf-8 -*-
"""
mergePicFolder.py
复制所有子文件夹中的图片到新文件夹中
汇编成exe文件可以任意使用
Created on Sun Aug 18 12:30:43 2019

@author: samsung
"""

import os  
import shutil 
 
print('输入格式：E:\myprojectnew\jupyter\整理文件夹\示例')
path = input('请键入需要整理的文件夹地址：')
new_path = input('请键入要复制到的文件夹地址：')
 
for root, dirs, files in os.walk(path):
    for i in range(len(files)):
        #print(files[i])
        if (files[i][-3:] == 'jpg') or (files[i][-3:] == 'png') or (files[i][-3:] == 'JPG'):
            file_path = root+'/'+files[i]  
            new_file_path = new_path+ '/'+ files[i]  
            shutil.copy(file_path,new_file_path) 
```

## 思考

* 本代码中通过设定图片文件的后缀名进行定位所有的符合条件的图片文件，所以可以修改后缀名的条件选择其他后缀名的图片文件，如.tiff文件
* 这种通过后缀名选择文件的形式，是否可以通过修改，比如只复制文件名中符合某些条件的文件，可以结合正则表达式实现。

## 致谢

[csdn blog](https://blog.csdn.net/xuan314708889/article/details/79619732)