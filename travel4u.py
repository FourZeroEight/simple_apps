# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def add_page(url,page):
    return f"{url}&page={page}"

output = list()
url = 'http://www.travel4u.com.tw/oversea/list_custom.aspx?MGRUP_CD=SHA05BR712B-SHA05BR758-SHA05BRTTE-SHA05CI00-SHA05CI501B-SHA05CI509-SHA05CI98902-SHA06AE987'
driver = webdriver.Chrome('chromedriver.exe')
for page in range(1,26): # TODO get the actual pages.
    if page == 1:
        driver.get(url)
    else:
        driver.get(add_page(url, page))
    elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctrlGroup")
    source_code = elem.get_attribute('innerHTML')
    output.append(source_code)


columns=['序', '出發日期', '團型名稱', '機場', '天數', 
         '機位', '可售', '優惠價', '訂金', '狀況']
df = pd.DataFrame(columns=columns)
for test in output:
    soup = BeautifulSoup(test, 'html.parser')
    routes = soup.find_all('div',{'class':'c_tr'})
    for index_, r in enumerate(routes):
        if index_ in [0]:
            continue
        route = r.find_all('div')
        row = list()
        for index, data in enumerate(route):
            if index in [4,5,6,7,11]:
                continue
            row.append(data.text)
        row_data=pd.Series(row,columns)
        df = df.append([row_data],ignore_index=True)

df = df[df['狀況'] != '滿團']
df['天數'] = df['天數'].astype('int')
df['機位'] = df['機位'].astype('int')
df['可售'] = df['可售'].astype('int')
df['優惠價'] = df['優惠價'].astype('int')
df['訂金'] = df['訂金'].astype('int')

# 挑星期
dates = ['四']
df = df[df['出發日期'].str.contains('|'.join(dates))]

# 挑月份
def f(text):
    # 2018/05/16(三)
    s = text.split('/')[1]
    if s in ['07', '08']:
        return True
    else:
        return False
df = df[df['出發日期'].apply(f)]

# 挑天數
df = df[df['天數']<=5]

# 挑座位數
df = df[df['可售']>=15]

df.to_csv('jianan.csv', index=False)
