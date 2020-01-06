# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:46:22 2019

@author: samsung
"""

import time
from selenium import webdriver

query = ['Q6XQN6', 'P43490']
funcs = []
symbol = []

# driver = webdriver.Firefox() #如此1行代码即是显示firefox界面。
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)#如此3行代码即不显示firefox界面。

for e in query:
    time.sleep(1)
    url = "https://www.uniprot.org/uniprot/{}".format(e)
    #print(url)
    driver.get(url)
    try:
        gene = driver.find_element_by_xpath('//*[@id="content-gene"]/h2').text
        #print(gene)
    except:
        gene = ''
    symbol.append(gene)
    try:
        function = driver.find_element_by_class_name('annotation').text
        #print(function)
    except:
        function = ''
    funcs.append(function)
        
driver.quit()
