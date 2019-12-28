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

