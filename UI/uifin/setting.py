# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qtpj\uifin\setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QEvent
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QMouseEvent, QCursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.offset = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("D:/AdobePJ/XD/ZOSC UI/exclude/Setting.png"))
        self.background.setObjectName("background")

        self.dot = QtWidgets.QLabel(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(70, 130, 21, 61))
        self.dot.setText("")
        self.dot.setPixmap(QtGui.QPixmap("D:/AdobePJ/XD/ZOSC UI/elements/•.png"))
        self.dot.setObjectName("dot")

        """close button"""
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(535, 7, 55, 25))
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setStyleSheet(
            '''
            QPushButton{image:url(D:/AdobePJ/XD/ZOSC UI/button/normal/btn.close.png); border:0px;}
            QPushButton:hover{image:url(D:/AdobePJ/XD/ZOSC UI/button/active/btn.close.active.png); border:0px;}
            '''
        )

        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        """end"""

        self.btn_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_info.setGeometry(QtCore.QRect(500, 440, 41, 23))
        self.btn_info.setObjectName("btn_info")
        self.btn_info.setStyleSheet(
            '''
            QPushButton{image:url(D:/AdobePJ/XD/ZOSC UI/button/normal/info.png); border:0px;}
            QPushButton:hover{image:url(D:/AdobePJ/XD/ZOSC UI/button/active/info.active.png); border:0px;}
            '''
        )

        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(70, 143, 170, 40))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.setStyleSheet(
            '''
            QPushButton{image:url(D:/AdobePJ/XD/ZOSC UI/button/normal/user.reset.png); border:0px;}
            QPushButton:hover{image:url(D:/AdobePJ/XD/ZOSC UI/button/active/user.reset.active.png); border:0px;}
            '''
        )

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#import setting_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())