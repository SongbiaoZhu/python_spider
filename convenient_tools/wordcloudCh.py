# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:59:38 2019
modified from
https://blog.csdn.net/u012735708/article/details/81532407
"""

# Chinese wordcloud
from wordcloud import WordCloud
 
# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
text = open("santi.txt", encoding='UTF-8').read()
 
# Generate a word cloud image
wordcloud = WordCloud(font_path='C:\Windows\Fonts\simkai.ttf').generate(text) 
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
 
# lower max_font_size
wordcloud = WordCloud(font_path='C:\Windows\Fonts\simkai.ttf',max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")