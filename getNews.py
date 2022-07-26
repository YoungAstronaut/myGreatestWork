import urllib.request as urll
import re
from settings import interNews
from settings import NationNews
from peewee import *
from fake_useragent import UserAgent
from lxml import etree
from urllib.error import URLError

def interNewsMain(userSettings):
    
    '''
    获取国际新闻
    '''
    
    interNewsPicturesPath = userSettings.interNewsPicturesPath
    count = 1
    for i in range(1,6):
        url = "https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/world_"+str(i)+".jsonp"

        headers= {'User-Agent':str(UserAgent().random)}
        request = urll.Request(url=url, headers=headers)
        try:
            response = urll.urlopen(request ,timeout= 5)
            result = response.read().decode('utf-8')
                
            news_message = re.compile(r'\{(\"id\".*?)\},')
            news = news_message.findall(result)
                        
            url_message = re.compile(r'\"(https:.*?)\",')
            title_message = re.compile(r'\"title\":\"(.*?)\",')
            brief_message = re.compile(r'\"brief\":\"(.*?)\",')
            pictureurl_message = re.compile(r'\"image\":\"(.*?)\",')
            
            for new in news:
                temp_title = title_message.findall(new)[0]
                temp_url = url_message.findall(new)[0]
                temp_brief = brief_message.findall(new)[0]
                temp_pictureurl = pictureurl_message.findall(new)[0]
                temp_details = ""
                
                if temp_url.find("https://photo") == -1:
                    temp_details = getNewsDetails(temp_url)
                
                userSettings.gotInterNews.append(interNews(count, temp_title, temp_url, temp_brief, temp_pictureurl, temp_details))

                try:
                    urll.urlretrieve(temp_pictureurl, r'{}\\{}'.format(interNewsPicturesPath, str(count)+".jpg"))
                except:
                    pass
                userSettings.gotInterNewsNums = count
                count+=1
        except URLError:
            pass        

            
def nationalNewsBriefMain(userSettings):
    
    '''
    获取国内主要新闻
    '''
    
    nationNewsBriefPicturesPath = userSettings.nationNewsBriefPicturesPath
    if userSettings.isShowedBriefNews:
        for i in range(1,3):
            url = "https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/china_"+str(i)+".jsonp"

            headers= {'User-Agent':str(UserAgent().random)}
            request = urll.Request(url=url, headers=headers)
            try:
                response = urll.urlopen(request ,timeout= 5)
                result = response.read().decode('utf-8')

                # with open('news.txt','w',encoding='utf-8') as fp:
                #     fp.write(result)
                    
                news_message = re.compile(r'\{(\"id\".*?)\},')
                news = news_message.findall(result)
                            
                url_message = re.compile(r'\"(https:.*?)\",')
                title_message = re.compile(r'\"title\":\"(.*?)\",')
                brief_message = re.compile(r'\"brief\":\"(.*?)\",')
                pictureurl_message = re.compile(r'\"image\":\"(.*?)\",')
                
                for new in news:
                    temp_title = title_message.findall(new)[0]
                    temp_url = url_message.findall(new)[0]
                    temp_brief = brief_message.findall(new)[0]
                    temp_pictureurl = pictureurl_message.findall(new)[0]
                    temp_details = ""
                
                    if temp_url.find("https://photo") == -1:
                        temp_details = getNewsDetails(temp_url)
                    
                    userSettings.gotNationNews["brief"].append(NationNews(userSettings.gotNationNewsNums["brief"]+1, temp_title, temp_url, temp_brief, temp_pictureurl, temp_details))
                    
                    opener = urll.build_opener()
                    opener.addheaders = [('User-Agent', headers["User-Agent"])]
                    urll.install_opener(opener)
                    try:
                        urll.urlretrieve(temp_pictureurl, r'{}\\{}'.format(nationNewsBriefPicturesPath, str(userSettings.gotNationNewsNums["brief"]+1)+".jpg"))
                    except:
                        pass
                    userSettings.gotNationNewsNums["brief"] +=1
            except:
                pass
                
                
def nationalNewsEconomyMain(userSettings):
    
    '''
    获取国内经济新闻
    '''
    
    nationNewsEconomyPicturesPath = userSettings.nationNewsEconomyPicturesPath
    if userSettings.isShowedEconomyNews:
        for i in range(1,3):
            url = "https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/economy_zixun_"+str(i)+".jsonp"

            headers= {'User-Agent':str(UserAgent().random)}
            request = urll.Request(url=url, headers=headers)
            try:
                response = urll.urlopen(request ,timeout= 5)
                result = response.read().decode('utf-8')

                # with open('news.txt','w',encoding='utf-8') as fp:
                #     fp.write(result)
                    
                news_message = re.compile(r'\{(\"id\".*?)\},')
                news = news_message.findall(result)
                            
                url_message = re.compile(r'\"(https:.*?)\",')
                title_message = re.compile(r'\"title\":\"(.*?)\",')
                brief_message = re.compile(r'\"brief\":\"(.*?)\",')
                pictureurl_message = re.compile(r'\"image\":\"(.*?)\",')
                
                for new in news:
                    temp_title = title_message.findall(new)[0]
                    temp_url = url_message.findall(new)[0]
                    temp_brief = brief_message.findall(new)[0]
                    temp_pictureurl = pictureurl_message.findall(new)[0]
                    temp_details = ""
                
                    if temp_url.find("https://photo") == -1:
                        temp_details = getNewsDetails(temp_url)
                    
                    userSettings.gotNationNews["economy"].append(NationNews(userSettings.gotNationNewsNums["economy"]+1, temp_title, temp_url, temp_brief, temp_pictureurl, temp_details))
                    
                    opener = urll.build_opener()
                    opener.addheaders = [('User-Agent', headers["User-Agent"])]
                    urll.install_opener(opener)
                    try:
                        urll.urlretrieve(temp_pictureurl, r'{}\\{}'.format(nationNewsEconomyPicturesPath, str(userSettings.gotNationNewsNums["economy"]+1)+".jpg"))
                    except:
                        pass
                    userSettings.gotNationNewsNums["economy"]+=1
            except:
                pass
                

def nationalNewsSocietyMain(userSettings):   
    
    '''
    获取国内社会新闻
    '''
    
    nationNewsSocietyPicturesPath = userSettings.nationNewsSocietyPicturesPath
    if userSettings.isShowedSocietyNews:
        for i in range(1,3):
            url = "https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/society_"+str(i)+".jsonp"

            headers= {'User-Agent':str(UserAgent().random)}
            request = urll.Request(url=url, headers=headers)
            try:
                response = urll.urlopen(request ,timeout= 5)
                result = response.read().decode('utf-8')

                # with open('news.txt','w',encoding='utf-8') as fp:
                #     fp.write(result)
                    
                news_message = re.compile(r'\{(\"id\".*?)\},')
                news = news_message.findall(result)
                            
                url_message = re.compile(r'\"(https:.*?)\",')
                title_message = re.compile(r'\"title\":\"(.*?)\",')
                brief_message = re.compile(r'\"brief\":\"(.*?)\",')
                pictureurl_message = re.compile(r'\"image\":\"(.*?)\",')
                
                for new in news:
                    temp_title = title_message.findall(new)[0]
                    temp_url = url_message.findall(new)[0]
                    temp_brief = brief_message.findall(new)[0]
                    temp_pictureurl = pictureurl_message.findall(new)[0]
                    temp_details = ""
                
                    if temp_url.find("https://photo") == -1:
                        temp_details = getNewsDetails(temp_url)
                    
                    userSettings.gotNationNews["society"].append(NationNews(userSettings.gotNationNewsNums["society"]+1, temp_title, temp_url, temp_brief, temp_pictureurl, temp_details))
                    
                    opener = urll.build_opener()
                    opener.addheaders = [('User-Agent', headers["User-Agent"])]
                    urll.install_opener(opener)
                    try:
                        urll.urlretrieve(temp_pictureurl, r'{}\\{}'.format(nationNewsSocietyPicturesPath, str(userSettings.gotNationNewsNums["society"]+1)+".jpg"))
                    except:
                        pass
                    userSettings.gotNationNewsNums["society"]+=1
            except:
                pass

def getNewsDetails(url):
    
    '''
    获取新闻的具体内容
    '''
    
    headers= {'User-Agent':str(UserAgent().random)}
    request = urll.Request(url=url, headers=headers)
    try:
        response = urll.urlopen(request ,timeout= 5)
        text = response.read().decode('utf-8')
        html = etree.HTML(text)
        paragraphs = html.xpath('//div[@class="content_area"]/p')
        return_text = []
        
        if len(paragraphs) > 0:
            for paragraph in paragraphs:
                paragraph_texts = paragraph.xpath("text()")
                paragraph_text = ""
                if len(paragraph_texts) > 0:
                    paragraph_text = paragraph.xpath("text()")[0]
                return_text.append(paragraph_text+"\n")    
    except:
        return_text = []
        pass
    return return_text