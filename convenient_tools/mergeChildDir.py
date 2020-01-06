# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25

@author: samsung
"""

import os
import easygui
import shutil

def main(fromdir, todir):
    for root,dirs,files in os.walk(fromdir):
        for file in files:
            print(file)
            oldpath = os.path.join(root, file)
            newpath = os.path.join(todir, file)
            shutil.copyfile(oldpath, newpath)
    print('所有"{}"下的文件和其子文件夹中的文件都已复制到"{}"文件夹中。'.format(fromdir, todir))
    input("Press Enter to exit...")

if __name__ == "__main__":
    print('请选择要包含要合并子文件夹的目录：')
    fromdir = easygui.diropenbox()
    print('请选择存放所有子文件夹中文件的目录：')
    todir = easygui.diropenbox()
    main(fromdir, todir)
