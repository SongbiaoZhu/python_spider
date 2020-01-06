# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:55:44 2019

@author: samsung
"""

'''
    windows + r   cmd   输入 pip install selenium 回车
    或者 console输入 conda install selenium
    selenium 可以用来自动操作浏览器的包，也可以用来做爬虫
'''
 
from selenium import webdriver 
 
browser = webdriver.Firefox() 
 
browser.get("http://www.baidu.com")
 
browser.find_element_by_id("kw").send_keys("selenium") 
browser.find_element_by_id("su").click() 
 
browser.quit()
