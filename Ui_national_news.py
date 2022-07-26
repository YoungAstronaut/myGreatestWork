# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\myGreatestwork\national_news.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, gotNationNews, key):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1247, 766)
        MainWindow.setStyleSheet("")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(src/1.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        
        self.gotNationNews = gotNationNews
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 1241, 691))
        self.listWidget.setStyleSheet("background-color: rgba(255, 255, 255, 150);")
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setIconSize(QtCore.QSize(200, 200))
        self.listWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setBatchSize(101)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        
        self.filecase = {"brief":"national_brief_pictures",
                         "economy":"economy_news_pictures",
                         "society":"national_society_pictures"}
        _translate = QtCore.QCoreApplication.translate
        self.key = key
        for news in self.gotNationNews[self.key]:
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(18)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.filecase[self.key]+"/"+str(news.index)+".jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            item.setIcon(icon)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            item.setText(_translate("MainWindow", news.title))
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.getIndividualNews)
        
        self.economyNews = QtWidgets.QPushButton(self.centralwidget)
        self.economyNews.setGeometry(QtCore.QRect(260, 10, 181, 41))
        self.economyNews.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.economyNews.setObjectName("economynews")
        self.economyNews.clicked.connect(self.clickEconomyNews)
        
        self.societyNews = QtWidgets.QPushButton(self.centralwidget)
        self.societyNews.setGeometry(QtCore.QRect(500, 10, 181, 41))
        self.societyNews.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.societyNews.setObjectName("societynews")
        self.societyNews.clicked.connect(self.clickSocietyNews)
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 181, 41))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.textBrowser.setObjectName("textBrowser")
        self.returnBack = QtWidgets.QPushButton(self.centralwidget)
        self.returnBack.setGeometry(QtCore.QRect(190, 10, 71, 31))
        self.returnBack.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.returnBack.setObjectName("returnback")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionshuaxin = QtWidgets.QAction(MainWindow)
        self.actionshuaxin.setObjectName("actionshuaxin")
        self.actionkankan = QtWidgets.QAction(MainWindow)
        self.actionkankan.setObjectName("actionkankan")
        self.menu.addSeparator()
        self.menu.addAction(self.actionshuaxin)
        self.menu.addAction(self.actionkankan)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">国内要闻</span></p></body></html>"))
        self.returnBack.setText(_translate("MainWindow", "返回"))
        self.economyNews.setText(_translate("MainWindow", "经济资讯"))
        self.societyNews.setText(_translate("MainWindow", "社会资讯"))
        
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.actionshuaxin.setText(_translate("MainWindow", "shuaxin"))
        self.actionshuaxin.setIconText(_translate("MainWindow", "刷新"))
        self.actionkankan.setText(_translate("MainWindow", "kankan"))
    
    def getIndividualNews(self):
        import Ui_individual_news
        currentIndex = self.listWidget.currentIndex().row()
        self.mainWindow = QMainWindow()
        individualNewsWindow = Ui_individual_news.Ui_MainWindow()
        individualNewsWindow.setupUi(self.mainWindow, self.gotNationNews[self.key][currentIndex], self.filecase[self.key])
        self.mainWindow.show()

    def clickEconomyNews(self):
        self.mainWindow = QMainWindow()
        self.economyNewsWindow = Ui_MainWindow()
        self.economyNewsWindow.setupUi(self.mainWindow, self.gotNationNews, "economy")
        self.mainWindow.show()
        
    def clickSocietyNews(self):
        self.mainWindow = QMainWindow()
        self.societyNewsWindow = Ui_MainWindow()
        self.societyNewsWindow.setupUi(self.mainWindow, self.gotNationNews, "society")
        self.mainWindow.show()