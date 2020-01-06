# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:40:35 2019

@author: samsung
"""

import os
import easygui

def main(path):
    file_count = 0
    dir_count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_count += 1
        for folder in dirs:
            dir_count += 1
    print('统计完成！')
    print('该路径下共有{}个文件，{}个子文件夹'.format(file_count, dir_count))
    input("Press Enter to exit...")

if __name__ == "__main__":
    print('请选择要统计文件数目的路径')
    path = easygui.diropenbox()
    main(path)
