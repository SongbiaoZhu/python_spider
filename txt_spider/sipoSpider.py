# -*- coding: utf-8 -*-
"""
sipoSpider
Created on Tue Sep 10 10:50:57 2019
@author: samsung
"""
from selenium import webdriver
import xlwt
import time

login = 'http://pss-system.cnipa.gov.cn/sipopublicsearch/portal/uilogin-forwardLogin.shtml'
account = 'songbiao'
pwd = 'Zhswwx150819'
pasearch = "发明名称=(嵌合抗原受体)"

driver = webdriver.Firefox()
driver.get(login)
driver.find_element_by_xpath('//*[@id="j_username"]').send_keys(account)
driver.find_element_by_xpath('//*[@id="j_password_show"]').send_keys(pwd)
'''手动输入验证码，并点击登录'''

# click高级检索
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/ul/li[2]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="searchExpDisplay"]').send_keys(pasearch)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div[3]/a[3]').click()
time.sleep(5)
# 点击过滤
driver.find_element_by_xpath('//*[@id="tool_filter"]').click()
time.sleep(5)
# 点击按文献类型过滤
driver.find_element_by_xpath('/html/body/div[21]/div/table/tbody/tr[2]/td/div/div/ul/li[2]/a').click()
# 勾选授权公开文献
driver.find_element_by_xpath('/html/body/div[21]/div/table/tbody/tr[2]/td/div/div/div/div[2]/table/tbody/tr[1]/td[3]/input').click()
# 勾选发明类型为发明
driver.find_element_by_xpath('/html/body/div[21]/div/table/tbody/tr[2]/td/div/div/div/div[2]/table/tbody/tr[2]/td[2]/input').click()
# 勾选有效专利
driver.find_element_by_xpath('/html/body/div[21]/div/table/tbody/tr[2]/td/div/div/div/div[2]/table/tbody/tr[3]/td[2]/input').click()
# 点击 应用 上述勾选的筛选参数
driver.find_element_by_xpath('/html/body/div[21]/div/table/tbody/tr[3]/td/div[2]/button[1]').click()
time.sleep(5)
# 点击 列表式显示
driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/a[2]').click()
time.sleep(5)
  
def loadTable(i):
    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
    fname = 'patentResPage{}.xls'.format(i)
    table_rows = driver.find_element_by_xpath("//*[@id='tbody']").find_elements_by_tag_name('tr')
    for x, tr in enumerate(table_rows):
        table_cols1 = tr.find_elements_by_tag_name('td')
        for j, tc in enumerate(table_cols1):
            sheet.write(x, j, tc.text)
            wbk.save(fname)
    print('Page_{}保存完成'.format(i))
            
i = 1
loadTable(i)
pages = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[1]/div[2]/div[4]/div/div[2]/div/div/div/div/p[1]").text.strip().split(' ')[1]
if int(pages) > 1:
    for p in range(2,int(pages)+1):
        driver.find_element_by_link_text('下一页').click()
        print('page{}加载中'.format(p))
        time.sleep(20)
        loadTable(p)
        
driver.close()

