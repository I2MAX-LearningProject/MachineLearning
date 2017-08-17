# Day_05_07_naver_login.py
from selenium import webdriver


def getPassword():
    f = open('Data/password.txt', 'r', encoding='utf-8')
    password = f.readline()
    f.close()
    return password.strip()

# print('[{}]'.format(getPassword()))

browser = webdriver.PhantomJS('Data/phantomjs.exe')

url = 'http://www.naver.com'
browser.get(url)

username = browser.find_element_by_name('id')
username.send_keys('applekoong')

password = browser.find_element_by_name('pw')
password.send_keys(getPassword())

form = browser.find_element_by_id('frmNIDLogin')
form.submit()

# ------------------------------------------------ #

url = 'http://mail.naver.com'
browser.get(url)
print(browser.title)
print(browser.name)
print(browser.page_source)
