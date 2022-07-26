class interNews():
    
    '''
    国际新闻类
    '''
    
    def __init__(self, index, title, url, brief, pictureurl, details) -> None:
        self.index = index
        self.title = title
        self.url = url
        self.brief = brief
        self.pictureurl = pictureurl
        self.details = details
        
class NationNews():
    
    '''
    国内新闻类
    '''
    
    def __init__(self, index, title, url, brief, pictureurl, details) -> None:
        self.index = index
        self.title = title
        self.url = url
        self.brief = brief
        self.pictureurl = pictureurl
        self.details = details

class Magzine():
    
    '''
    杂志类
    '''
    
    def __init__(self, name, magzine_path, magzine_cover_path) -> None:
        self.name = name
        self.magzine_path = magzine_path
        self.magzine_cover_path = magzine_cover_path

class Book():
    
    '''
    图书类
    '''
    
    def __init__(self, index, title, author, author_intro, publisher, abstract, year) -> None:
        self.index = index
        self.title = title
        self.author = author
        self.author_info = author_intro
        self.publisher = publisher
        self.abstract = abstract
        self.year = year
        
class Settings():
    
    '''
    设置类
    '''
    
    def __init__(self) -> None:
        self.gotInterNews = []
        self.gotInterNewsNums = 0
        self.interNewsPicturesPath = "international_pictures"
        
        self.gotNationNews = {"brief":[], "economy":[], "society":[]}
        self.gotNationNewsNums = {"brief":0, "economy":0, "society":0}
        self.nationNewsBriefPicturesPath = "national_brief_pictures"
        self.nationNewsEconomyPicturesPath = "economy_news_pictures"
        self.nationNewsSocietyPicturesPath = "national_society_pictures"
        
        self.isShowedBriefNews = True
        self.isShowedEconomyNews = True
        self.isShowedSocietyNews = True
        
        self.magzines_path = "got_magzines"
        self.magzines = ["Time+International+Edition",
                         "economist",
                         "the+week",
                         "reader+digest",
                         "atlantic",
                         "national+geographic",
                         "news+week"]
        self.magzinesStroed = "magzines_stored_path.json"
        self.gotMagzines = []
        self.magzineMiniumSize = 1048576
        self.gotMagzinesNums = 0
        self.isMagzinesUpdated = False
        
        self.theEconomistPassword = "www.yigeplus.xyz"
        
        self.gotBooks = []
        self.books_img_path = "douban_books"
        self.gotBooksNums = 0