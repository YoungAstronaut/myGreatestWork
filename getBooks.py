import urllib.request as urll

from fake_useragent import UserAgent
from lxml import etree
import os
import time
from settings import Book
import random


'''
获取豆瓣图书上的新书内容
'''
def getBooks(userSettings):
    
    # 豆瓣图书的网页
    url = "https://book.douban.com/"
    count = 1
    # 从设置中获取存放书籍图片的地址
    books_img_path = userSettings.books_img_path
    # 伪装表头
    headers= {'User-Agent':str(UserAgent().random)}
    request = urll.Request(url=url, headers=headers)
    
    try:
        # 获取网页源码
        response = urll.urlopen(request ,timeout= 5)
        result = response.read().decode('utf-8')
        
        # 使用xpath选择器解析源码内容
        html = etree.HTML(result)
        
        # 获取了全部书籍所在源码块的列表
        booksets = html.xpath('//ul[@class="list-col list-col5 list-express slide-item"]')
        
        # 循环遍历列表，从每个源码块里提取信息
        for bookset in booksets:
            books = bookset.xpath('./li')
            for book in books:
                
                # 获取书籍标题
                book_title = book.xpath('div[@class="info"]/div[@class="more-meta"]/h4/text()')[0].strip()
                
                # 获取书籍作者信息
                book_author = book.xpath('div[@class="info"]/div[@class="more-meta"]/p[1]/span[@class="author"]/text()')[0].strip()
                
                # 获取书籍出版年份
                book_year = book.xpath('div[2]/div[3]/p[1]/span[2]/text()')[0].strip()
                # book_year = book.xpath('div[@class="info"]/div[class="more-meta"]/p[1]/span[@class="year"]/text()')[0].strip()
                
                # 获取书籍出版社信息
                book_pubulisher = book.xpath('div[@class="info"]/div[@class="more-meta"]/p[1]/span[@class="publisher"]/text()')[0].strip()
                
                # 获取书籍详细信息的url
                book_url = book.xpath('div[@class="cover"]/a/@href')[0].strip()
                
                # 获取书籍封面图片的url
                book_img_url = book.xpath('div[@class="cover"]/a/img/@src')[0].strip()
                
                # 尝试获取书籍封面图片
                try:
                    book_img_path = os.path.join(books_img_path, str(count)+'.jpg')
                    urll.urlretrieve(book_img_url, book_img_path)
                except:
                    print("error occurs in picture catching !")
                
                # 进入到书籍的详细介绍的页面
                try:
                    # 获取源码并解析
                    request = urll.Request(url=book_url, headers=headers)
                    response = urll.urlopen(request, timeout=5)
                    result = response.read().decode('utf-8')
                    html = etree.HTML(result)
                    
                    # 定义空列表，储存书籍简介的全部段落，列表每个元素代表一个段落
                    book_abstract = []
                    
                    # 获取段落
                    book_abstract_elements = html.xpath('//div[@class="intro"]')[1].xpath('p')
                    for book_abstract_element in book_abstract_elements:
                        book_abstract.append(book_abstract_element.xpath('text()')[0])
                    
                    # 定义空列表，储存书籍作者简介的全部段落，列表每个元素代表一个段落
                    book_author_intro = []   
                    
                    # 获取段落
                    book_author_intro_elements = html.xpath('//div[@class="intro"]')[-1].xpath('p')
                    for book_author_intro_element in book_author_intro_elements:
                        book_author_intro.append(book_author_intro_element.xpath('text()')[0])
                    
                    # 添加书籍
                    userSettings.gotBooks.append(Book(count, book_title, book_author, book_author_intro, book_pubulisher, book_abstract, book_year))
                    count += 1
                    userSettings.gotBooksNums += 1
                    time.sleep(random.randint(1, 10))
                except:
                    print("error occurs in entering individual book !")
                
    except:
        pass