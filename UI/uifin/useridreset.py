# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qtpj\uifin\useridreset.ui'
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
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(""))
        self.background.setObjectName("background")

        self.setting_title = QtWidgets.QLabel(self.centralwidget)
        self.setting_title.setGeometry(QtCore.QRect(-10, 0, 811, 41))
        self.setting_title.setText("")
        self.setting_title.setPixmap(QtGui.QPixmap("D:/AdobePJ/XD/ZOSC UI/elements/userset.title.png"))
        self.setting_title.setObjectName("setting_title")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-10, 35, 811, 141))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap("D:/AdobePJ/XD/ZOSC UI/elements/reset.welcome.png"))
        self.title.setObjectName("title")

        self.userid_input = QtWidgets.QLabel(self.centralwidget)
        self.userid_input.setGeometry(QtCore.QRect(170, 210, 461, 181))
        self.userid_input.setText("")
        self.userid_input.setPixmap(QtGui.QPixmap("D:/AdobePJ/XD/ZOSC UI/elements/get.id.name.png"))
        self.userid_input.setObjectName("userid_input")

        """input: student id"""
        self.input_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(312, 218, 307, 40))
        self.input_id.setObjectName("input_id")
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoL00")
        font.setPointSize(25)               
        self.input_id.setFont(font)

        """input: student name"""
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(312, 342, 307, 40))
        self.input_name.setObjectName("input_name")
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoL00")
        font.setPointSize(25)               
        self.input_name.setFont(font)

        """yes button"""
        self.btn_yes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yes.setGeometry(QtCore.QRect(550, 430, 135, 55))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_yes.setStyleSheet(
            '''
            QPushButton{image:url(D:/AdobePJ/XD/ZOSC UI/button/normal/btn.yes.png); border:0px;}
            QPushButton:hover{image:url(D:/AdobePJ/XD/ZOSC UI/button/active/btn.yes.active.png); border:0px;}
            '''
        )
        """end"""

        """close button"""
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(745, 10, 40, 20))
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setStyleSheet(
            '''
            QPushButton{image:url(D:/AdobePJ/XD/ZOSC UI/button/normal/btn.close.png); border:0px;}
            QPushButton:hover{image:url(D:/AdobePJ/XD/ZOSC UI/button/active/btn.close.active.png); border:0px;}
            '''
        )

        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        """end"""

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-9, -6, 811, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/elements/reset.welcome.png"))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#import zosc_user_reset_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())