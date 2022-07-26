import json
import urllib.request as urll
from urllib.error import URLError

from fake_useragent import UserAgent
from lxml import etree
import os
from settings import Magzine
from socket import timeout
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import zipfile
import fitz

def getMagzines(userSettings):
    '''
    获取杂志
    '''
    
    # magzinelib的网址
    base_url = "https://magazinelib.com/?s="
    
    # 用来判断是否获取到了pdf的参数
    magzineMiniumSize = userSettings.magzineMiniumSize
    
    # 储存magzine的字典
    storedMagzines = {}
    
    # 从json文件中获取已经保存了的杂志
    with open("magzines_stored_path.json", "r", encoding='utf-8') as fp:
        storedMagzines = json.load(fp)
    userSettings.gotMagzinesNums = len(storedMagzines.keys())
    if userSettings.gotMagzinesNums > 0:
        for storedMagzine in storedMagzines.keys():
            userSettings.gotMagzines.append(Magzine(storedMagzine, storedMagzines[storedMagzine]["magzine_path"], storedMagzines[storedMagzine]["magzine_cover_path"]))
    
    # 获取最新the economist
    the_economist_url = "https://yigeplus.xyz/2021/08/02/%e6%9c%80%e6%96%b0%e7%bb%8f%e6%b5%8e%e5%ad%a6%e4%ba%bathe-economist%e5%85%8d%e8%b4%b9%e4%b8%8b%e8%bd%bd%e5%88%86%e4%ba%ab/"
    the_economist = getTheEconomistByWeb(userSettings, getLink(the_economist_url)[0], getLink(the_economist_url)[1], getLink(the_economist_url)[2], getLink(the_economist_url)[3])
    
    if the_economist.name == None or the_economist.name in storedMagzines.keys():
        pass
    else: 
        storedMagzines[the_economist.name] = {"magzine_path":the_economist.magzine_path,"magzine_cover_path":the_economist.magzine_cover_path}
        userSettings.gotMagzines.append(the_economist)
        userSettings.gotMagzinesNums += 1
        userSettings.isMagzinesUpdated = True
        with open("magzines_stored_path.json", "w", encoding='utf-8') as fp:
            json.dump(storedMagzines, fp=fp)
    
    # 获取其他杂志
    for magzine in userSettings.magzines:
        search_url = base_url + magzine
        # print("connecting to " + search_url)
        headers = {'User-Agent':str(UserAgent().random)}
        request = urll.Request(url=search_url, headers=headers)
        response = urll.urlopen(request ,timeout= 20)
        result = response.read().decode('utf-8')
        # print("connected " + search_url)
        
        html = etree.HTML(result)
        magzineurls = html.xpath('//h2[@class="g1-mega g1-mega-1st entry-title"]/a/@href')
        
        if len(magzineurls)>0:
            for magzineurl in magzineurls:
                headers = {'User-Agent':str(UserAgent().random)}
                opener = urll.build_opener()
                opener.addheaders = [('User-Agent', headers["User-Agent"])]
                request = urll.Request(url=magzineurl, headers=headers)
                urll.install_opener(opener)
                try:
                    response = urll.urlopen(request ,timeout= 5)
                    magzinepage = response.read().decode('utf-8')
                    
                    magzinehtml = etree.HTML(magzinepage)
                    magzinename = magzinehtml.xpath('//a[@target="_blank"]/text()')[1].replace(".pdf", "")
                    # print(magzinename)
                    magzine_cover_url = magzinehtml.xpath('//div[@class="vkwpb_img_wrap"]/img/@data-lazy-src')[0]
                    # print(magzine_cover_url)
                    magzine_cover_path = userSettings.magzines_path+"/"+magzinename+".jpg"
                    # print(magzine_cover_path)
                    
                    urll.urlretrieve(magzine_cover_url, magzine_cover_path)
                    downloadurl = magzinehtml.xpath('//div[@class = "vk-att-item"]/a/@href')[0]
                    magzine_path =userSettings.magzines_path +"/"+ magzinename + ".pdf"
                    urll.urlretrieve(downloadurl, magzine_path)
                    # print("magzines: ")
                    # print(userSettings.gotMagzines)
                    
                    if(os.path.getsize(magzine_path) < magzineMiniumSize):
                        os.remove(magzine_cover_path)
                        os.remove(magzine_path)
                    else:
                        if magzinename in list(storedMagzines.keys()):
                            os.remove(magzine_cover_path)
                            os.remove(magzine_path)
                        else:
                            storedMagzines[magzinename] = {"magzine_path":magzine_path,"magzine_cover_path":magzine_cover_path}
                            userSettings.gotMagzines.append(Magzine(magzinename, magzine_path, magzine_cover_url))
                            userSettings.gotMagzinesNums += 1
                            userSettings.isMagzinesUpdated = True
                            with open("magzines_stored_path.json", "w", encoding='utf-8') as fp:
                                json.dump(storedMagzines, fp=fp)
                except URLError:
                    print(magzineurl+" connection failed")
                    pass
                except timeout:
                    print(magzineurl+" connecting waiting for too long")

def getLink(url):
    """ 获取the economist网盘地址、密码等信息
 
    :param url: 网址
    :return [ ]: 返回相关信息的列表，列表元素依次为：网盘地址、提取密码、日期、是否获取到了信息（布尔值）
    """
    
    try:
        headers = {'User-Agent':str(UserAgent().random)}
        request = urll.Request(url=url, headers=headers)
        response = urll.urlopen(request, timeout=10)
        result = response.read().decode('utf-8')
        # with open("test.txt", 'w', encoding='utf-8') as fp:
        #     fp.write(result)
        urlmessage = re.compile(r'(https:.*?)密码')
        link = urlmessage.findall(result)[0]
        passwordmessage = re.compile(r'密码:(.*?)</p')
        password = passwordmessage.findall(result)[0]
        datemessage = re.compile(r'<p>(20.*?)</p>\n<p>https')
        date = datemessage.findall(result)[0]
        return [link, password, date, True]
    except URLError:
        return ['', '', '', False]
            
def getTheEconomistByWeb(userSettings, link, password, date, isbanned):
    '''
    通过selenium获取the economist
    :param userSettings: 设置类
    :param link: 网址
    :param password: 提取码
    :param date: 日期
    :param isbaned: 爬虫是否被ban
    '''
    
    if isbanned:
        
        # selenium初始化
        options = Options()    
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        out_path = os.path.join(os.getcwd(), userSettings.magzines_path)
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': out_path}#设置chromewebdriver默认下载位置
        options.add_experimental_option('prefs', prefs)
        browser = webdriver.Chrome(options=options)
        
        browser.get(link)
        element = browser.find_element(by=By.ID, value="pwd")
        element.send_keys(password)
        time.sleep(1)
        current_window = browser.current_window_handle  
        browser.find_element(by=By.ID, value='sub').click()
        time.sleep(3)
        for window in browser.window_handles:
            if window != current_window:
                browser.switch_to.window(window)
        current_window = browser.current_window_handle
        new_element = browser.find_elements(by=By.XPATH, value='//a[@target="_blank"]')[3]
        downloadurl = new_element.get_attribute('href')
        browser.get(downloadurl)
        zipname = browser.page_source
        zipname_message = re.compile(r'title>(.*?) - 蓝奏云')
        zipname = zipname_message.findall(zipname)[0]
        time.sleep(3)
        frame = browser.find_elements(by=By.CLASS_NAME, value="ifr2")
        browser.switch_to.frame(frame[0])
        url = browser.find_elements(by=By.XPATH, value='//a[@target="_blank"]')[0].click()
        time.sleep(20)
        
        zip_path = userSettings.magzines_path+'/'+zipname
        zip_file = zipfile.ZipFile(zip_path)
        zip_list = zip_file.namelist()
        for f in zip_list:
            zip_file.extract(f, userSettings.magzines_path+'/', pwd=userSettings.theEconomistPassword.encode("utf-8"))
        zip_file.close()

        os.remove(zip_path)
        renamed_pdf_path = userSettings.magzines_path+'/'+"The Economist - "+date+".pdf"
        os.rename(zip_path.replace(".zip", ".pdf"), renamed_pdf_path)
        pdf = fitz.open(renamed_pdf_path)
        first_page = pdf[0]
        cover = first_page.get_pixmap(alpha = False)
        cover_path = renamed_pdf_path.replace(".pdf", ".jpg")
        cover.save(cover_path)
        
        return Magzine("The Economist - "+date, renamed_pdf_path, cover_path)
    else: 
        return Magzine(None, None, None)