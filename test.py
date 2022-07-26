import urllib.request as urll
import re
import getBooks
from peewee import *
from fake_useragent import UserAgent
from lxml import etree
import os
import settings
import getMagzines
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.common.keys import Keys
import zipfile


# url = "https://vk.com/doc448173336_640096029?hash=a3hNfgwKlm3GDbfM41vj3Zm1tFRz2e19ufZ0omUrsOX&dl=GQZDGNBSGQ2DGNQ:1657533692:NMyGrXRJeVw5ESy73kwgIBZdh8P9C2dFnzdISK4F23o&api=1&no_preview=1"
# # url = "https://vk.com/doc448173336_640447523?hash=K81HZUQ8aiJqwL57T3zqal3lVdV6p4TsVLnKbjBLmYw&dl=GQZDGNBSGQ2DGNQ:1657791988:bqjkZ4WZAMLdqFhH3yQFRzWzT8Fhe9J1PFZgYGMZmDL&api=1&no_preview=1"
# headers= {'User-Agent':str(UserAgent().random)}
# opener = urll.build_opener()
# opener.addheaders = [('User-Agent', headers["User-Agent"])]
# urll.install_opener(opener)
# urll.urlretrieve(url, "got_magzines/test.pdf")
# # request = urll.Request(url, headers=headers)

# print(os.getcwd())
# os.remove(os.path.join( os.getcwd(), "got_magzines", "test.pdf"))

userSettings = settings.Settings()
def booksSpider(userSettings):
    getBooks.getBooks(userSettings=userSettings)
thread6 = threading.Thread(target=booksSpider, args=(userSettings,))
thread6.start()

# options = Options()    
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# out_path = os.path.join(os.getcwd(), "got_magzines")
# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': out_path}
# options.add_experimental_option('prefs', prefs)
# browser = webdriver.Chrome(options=options)
# browser.get("https://yigeplus.lanzouy.com/b00vvkrwh")
# element = browser.find_element(by=By.ID, value="pwd")
# element.send_keys("dqpk")
# time.sleep(1)
# current_window = browser.current_window_handle  
# print(browser.find_element(by=By.ID, value='sub').get_attribute('value'))
# browser.find_element(by=By.ID, value='sub').click()
# time.sleep(3)
# for window in browser.window_handles:
#     if window != current_window:
#         browser.switch_to.window(window)
# current_window = browser.current_window_handle 
# new_element = browser.find_elements(by=By.XPATH, value='//a[@target="_blank"]')[3]
# print(new_element)
# downloadurl = new_element.get_attribute('href')
# #print(len(browser.find_elements(by=By.XPATH, value='//a[@target="_blank"]')))
# # page = browser.page_source
# # with open("test.html", "w", encoding="utf-8")as fp:
# #     fp.write(page)
# # myhtml = etree.HTML(page)
# # # https://yigeplus.lanzouy.com/
# # downloadurl = "https://yigeplus.lanzouy.com/"+myhtml.xpath('//a[@target="_blank"]/@href')[0]
# browser.get(downloadurl)
# zipname = browser.page_source
# # print("zipname: "+zipname)
# zipname_message = re.compile(r'title>(.*?) - 蓝奏云')
# zipname = zipname_message.findall(zipname)[0]
# time.sleep(3)
# frame = browser.find_elements(by=By.CLASS_NAME, value="ifr2")
# browser.switch_to.frame(frame[0])
# url = browser.find_elements(by=By.XPATH, value='//a[@target="_blank"]')[0].click()
# time.sleep(10)

# zip_path = 'got_magzines/'+zipname
# zip_file = zipfile.ZipFile(zip_path)
# zip_list = zip_file.namelist()
# for f in zip_list:
# 	zip_file.extract(f, 'got_magzines/',pwd="www.yigeplus.xyz".encode("utf-8"))
# zip_file.close()

# os.remove(zip_path)
# os.rename(zip_path.replace(".zip", ".pdf"), "/got_magzines"+"my.pdf")
# # browser.get(url)
# # page = browser.page_source
# # print(page)


   