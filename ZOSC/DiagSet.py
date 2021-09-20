# -*- coding: utf-8 -*-

import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class UI_DiagSet(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)



    def setupUi(self, MainWindow):

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setObjectName("자가진단 설정")
        self.resize(800, 500)
        self.setMinimumSize(QtCore.QSize(800, 500))
        self.center()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/landscape/userchecksign.png"))
        self.background.setObjectName("background")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(130, 147, 201, 41))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(130, 195, 201, 41))
        self.graphicsView_2.setObjectName("graphicsView_2")

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
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)

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

        self.level = QtWidgets.QComboBox(self.centralwidget)
        self.level.setGeometry(QtCore.QRect(160, 297, 121, 22))
        self.level.setObjectName("comboBox")
        self.level.addItem("유치원")
        self.level.addItem("초등학교")
        self.level.addItem("중학교")
        self.level.addItem("고등학교")

        self.city = QtWidgets.QComboBox(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(160, 255, 121, 22))
        self.city.setObjectName("comboBox_2")
        self.city.addItem("서울특별시")
        self.city.addItem("부산광역시")
        self.city.addItem("대구광역시")
        self.city.addItem("인천광역시")
        self.city.addItem("광주광역시")
        self.city.addItem("대전광역시")
        self.city.addItem("울산광역시")
        self.city.addItem("세종특별자치시")
        self.city.addItem("경기도")
        self.city.addItem("강원도")
        self.city.addItem("충청북도")
        self.city.addItem("충청남도")
        self.city.addItem("전라북도")
        self.city.addItem("전라남도")
        self.city.addItem("경상북도")
        self.city.addItem("경상남도")
        self.city.addItem("제주특별자치도")

        self.input_birth = QtWidgets.QLineEdit(self.centralwidget)
        self.input_birth.setGeometry(QtCore.QRect(150, 335, 121, 41))
        self.input_birth.setObjectName("input_birth")

        self.input_dspw = QtWidgets.QLineEdit(self.centralwidget)
        self.input_dspw.setGeometry(QtCore.QRect(150, 385, 121, 41))
        self.input_dspw.setObjectName("input_dspw")
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setFamily("AppleSDGothicNeoL00")
        self.input_birth.setFont(font)
        self.input_dspw.setFont(font)



        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "자가진단 설정"))



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
