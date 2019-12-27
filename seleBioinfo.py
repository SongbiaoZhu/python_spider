# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:38:09 2019

@author: samsung
"""
import random
from selenium import webdriver
from time import sleep

pdfURLs = []
with open('pdfurl.txt', 'r') as f:
    for line in f:
        pdfURLs.append(line)

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', 'D:\\ProgramFiles\\bioinformatics')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')

driver = webdriver.Firefox(firefox_profile=profile)

for i in pdfURLs:
    try:
        print(i)
        driver.get(i)
        sleep(random.randint(5,10))
        driver.find_element_by_id("download").click()
        sleep(random.randint(30,45))
    except:
        continue

driver.quit()






