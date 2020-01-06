# -*- coding: utf-8 -*-
"""
1. pip install pymupdf
[https://blog.csdn.net/qq_43145035/article/details/83270501]
Created on Thu Aug 29 23:25:57 2019
@author: samsung
path is the pdfs directory.
"""

import fitz
import os

path = 'D:\\ProgramFiles\\PythonScripts\\gepia'
items = os.listdir(path) 
pdfs = []
for f in items:
    if f.endswith(".pdf"):
        pdfs.append(f)
#  打开PDF文件，生成一个对象
for pdf in pdfs:
    doc = fitz.open(os.path.join(path, pdf))
    fname = pdf.split('.')[0]
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG('{}\\{}_{}.png'.format(path,fname,pg))