import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
 
import Ui_main
import getNews
import getMagzines
import getBooks
import threading
import settings

userSettings = settings.Settings()

def interNewsSpider(userSettings):
    getNews.interNewsMain(userSettings=userSettings)
    
def nationNewsEconomySpider(userSettings):
    getNews.nationalNewsEconomyMain(userSettings=userSettings)
    
def nationNewsBriefSpider(userSettings):
    getNews.nationalNewsBriefMain(userSettings=userSettings)
    
def nationNewsSocietySpider(userSettings):
    getNews.nationalNewsSocietyMain(userSettings=userSettings)
    
def magzinesSpider(userSettings):
    getMagzines.getMagzines(userSettings=userSettings)
    
def booksSpider(userSettings):
    getBooks.getBooks(userSettings=userSettings)
 
thread1 = threading.Thread(target=interNewsSpider, args=(userSettings,))
thread1.start()
thread2 = threading.Thread(target=nationNewsEconomySpider, args=(userSettings,))
thread2.start() 
thread3 = threading.Thread(target=nationNewsBriefSpider, args=(userSettings,))
thread3.start()
thread4 = threading.Thread(target=nationNewsSocietySpider, args=(userSettings,))
thread4.start()
thread5 = threading.Thread(target=magzinesSpider, args=(userSettings,))
thread5.start()
thread6 = threading.Thread(target=booksSpider, args=(userSettings,))
thread6.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_main.Ui_MainWindow()
    ui.setupUi(MainWindow, userSettings)
    MainWindow.show()
    sys.exit(app.exec_())
