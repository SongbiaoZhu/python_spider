# --** coding="UTF-8" **--
# 
# author:SueMagic  time:2019-01-01
import os
import re
import sys

folder = r'E:\Project\paperWriting\GPB\GPB_figures_format_edited_20191121\Figures_printed_GPB-D-19-00123'
os.chdir(folder)
for file in os.listdir(folder):
    newName = file.split('_')[0] + '_print.jpg'
    os.rename(file, newName)
    print(file + '---->'+newName)
    
