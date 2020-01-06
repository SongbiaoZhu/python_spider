# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:20:47 2019

@author: samsung

https://blog.csdn.net/liucc09/article/details/82775797
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

query = 'P2P'
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kw")))
driver.find_element_by_id("kw").clear()         #清空里面已有的输入
driver.find_element_by_id("kw").send_keys(query)    #在里面输入P2P搜索词
driver.find_element_by_id("su").click()          #点击搜索按钮

for i in range(2,5,1): # 爬取第1页到第4页的搜索结果条目
    time.sleep(1)
    e_item = driver.find_elements_by_xpath('//div[@class="result c-container "]')
    print('\npage:{}'.format(i-1))
    for x in enumerate([e.find_element_by_tag_name('a').text for e in e_item]):
        print(x)
    #print('\n'.join([e.find_element_by_tag_name('a').get_attribute('href') for e in e_item]))
    driver.find_element_by_xpath(f"//div[@id='page']/descendant::span[text()='{i}']").click()
        
driver.quit()

