# -*- conding: utf-8 -*-

import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class UI_Setting(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)



    def setupUi(self, MainWindow):

            MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)

            self.setObjectName("설정")
            self.resize(600, 500)
            self.setMinimumSize(QtCore.QSize(600, 500))
            self.center()

            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            
            self.background = QtWidgets.QLabel(self.centralwidget)
            self.background.setGeometry(QtCore.QRect(0, 0, 600, 500))
            self.background.setText("")
            self.background.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/landscape/Setting.png"))
            self.background.setObjectName("background")

            """close button"""
            self.btn_close = QtWidgets.QPushButton(self.centralwidget)
            self.btn_close.setGeometry(QtCore.QRect(540, 10, 40, 20))
            self.btn_close.setObjectName("btn_close")
            self.btn_close.setStyleSheet(
                '''
                QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.close.png); border:0px;}
                QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.close.active.png); border:0px;}
                '''
            )

            """end"""

            self.btn_info = QtWidgets.QPushButton(self.centralwidget)
            self.btn_info.setGeometry(QtCore.QRect(515, 440, 41, 23))
            self.btn_info.setObjectName("btn_info")
            self.btn_info.setStyleSheet(
                '''
                QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/info.png); border:0px;}
                QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/info.active.png); border:0px;}
                '''
            )

            self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
            self.btn_reset.setGeometry(QtCore.QRect(40, 150, 140, 61))
            self.btn_reset.setObjectName("btn_reset")
            self.btn_reset.setStyleSheet(
                '''
                QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.reset.png); border:0px;}
                QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.reset.active.png); border:0px;}
                '''
        )

            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)



    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "설정"))



    # UI Interactions ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

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