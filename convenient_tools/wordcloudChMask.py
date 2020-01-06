# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:56:36 2019
modified from
https://blog.csdn.net/u012735708/article/details/81532407
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import matplotlib
import os
from wordcloud import WordCloud
 
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
mask = np.array(Image.open(path.join(d, "alice_mask.png")))
text = open(path.join(d, 'santi.txt'), encoding='UTF-8').read()
 
text = text.replace(u"汪淼说", u"汪淼")
text = text.replace(u"汪淼问", u"汪淼")
text = text.replace(u"叶文洁说", u"叶文洁")
text = text.replace(u"元首说", u"元首")
 
wc = WordCloud(font_path='C:\Windows\Fonts\simkai.ttf',max_words=200, mask=mask, margin=10,background_color='white',
               min_font_size=4,max_font_size=100,random_state=1,mode='RGBA').generate(text)
default_colors = wc.to_array()
#标题字体设置
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
 
wc.to_file("a_new_hope.png")
 
plt.figure(figsize=(20,20))
plt.title(u"三体-词频统计",fontproperties=myfont,fontsize=100)
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()