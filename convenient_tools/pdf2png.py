# -*- coding: utf-8 -*-
"""
1. pip install pymupdf
[https://blog.csdn.net/qq_43145035/article/details/83270501]
Created on Thu Aug 29 23:25:57 2019
@author: samsung
"""

import fitz
import os
import easygui
        
def main(path):
    items = os.listdir(path) 
    pdfs = []
    for f in items:
        if f.endswith(".pdf"):
            pdfs.append(f)
    for pdf in pdfs:
        doc = fitz.open(os.path.join(path, pdf))
        fname = pdf.split('.')[0]
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG('{}\\{}_{}.png'.format(path,fname,pg))
    print('转换完成')
    input("Press Enter to exit...")

if __name__ == "__main__":
    print('请选择要转为图片的pdf存储路径')
    path = easygui.diropenbox()
    main(path)
