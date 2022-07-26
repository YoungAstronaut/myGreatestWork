# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\myGreatestwork\books.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, gotBooks, bookdir):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.gotBooks = gotBooks
        self.bookdir = bookdir
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("#centralwidget{background-image: url("+"src/1.jpg"+");}")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 40, 1140, 720))
        self.listWidget.setStyleSheet("background-color: rgba(255, 255, 255, 150);")
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setIconSize(QtCore.QSize(300, 300))
        self.listWidget.setObjectName("listWidget")
        for gotbook in self.gotBooks:
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(18)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(os.path.join(bookdir, str(gotbook.index)+".jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            item.setText(_translate("MainWindow", gotbook.title))
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.getIndividualBook)    
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def getIndividualBook(self):
        import Ui_individual_book
        currentIndex = self.listWidget.currentIndex().row()
        self.mainWindow = QMainWindow()
        individualBookWindow = Ui_individual_book.Ui_MainWindow()
        individualBookWindow.setupUi(self.mainWindow, self.gotBooks[currentIndex], self.bookdir)
        self.mainWindow.show()
