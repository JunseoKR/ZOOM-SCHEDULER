# -*- coding: utf-8 -*-

import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class UI_Diagnosis(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)



    def setupUi(self, MainWindow):

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        MainWindow.setObjectName("자가진단")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        self.center()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/landscape/usercheck.png"))
        self.background.setObjectName("background")

        self.setting_title = QtWidgets.QLabel(self.centralwidget)
        self.setting_title.setGeometry(QtCore.QRect(-10, 0, 841, 41))
        self.setting_title.setText("")
        self.setting_title.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/userchecktitle.png"))
        self.setting_title.setObjectName("setting_title")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(120, 240, 21, 31))
        self.checkBox.setText("")
        self.checkBox.setIconSize(QtCore.QSize(32, 32))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(280, 240, 21, 31))
        self.checkBox_2.setText("")
        self.checkBox_2.setIconSize(QtCore.QSize(32, 32))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(120, 335, 21, 31))
        self.checkBox_3.setText("")
        self.checkBox_3.setIconSize(QtCore.QSize(32, 32))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(120, 425, 21, 31))
        self.checkBox_4.setText("")
        self.checkBox_4.setIconSize(QtCore.QSize(32, 32))
        self.checkBox_4.setObjectName("checkBox_4")

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(280, 336, 21, 31))
        self.checkBox_5.setText("")
        self.checkBox_5.setIconSize(QtCore.QSize(32, 32))
        self.checkBox_5.setObjectName("checkBox_5")

        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(280, 425, 21, 31))
        self.checkBox_6.setText("")
        self.checkBox_6.setIconSize(QtCore.QSize(32, 32))
        self.checkBox_6.setObjectName("checkBox_6")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 130, 741, 61))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)

        """close button"""
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(745, 10, 40, 20))
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setStyleSheet(
            '''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.close.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.close.active.png); border:0px;}
            '''
        )
        """end"""

        """yes button"""
        self.btn_yes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yes.setGeometry(QtCore.QRect(600, 430, 135, 55))
        self.btn_yes.setObjectName("btn_yes")
        self.btn_yes.setStyleSheet(
            '''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.yes.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.yes.active.png); border:0px;}
            '''
        )



        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "자가진단"))



    # UI Interactions ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
