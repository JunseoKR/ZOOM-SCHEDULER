import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
# -*- conding: utf-8 -*-

import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ZOSC import *
from Main import *
from UserSet import *
from Setting import *



class UI_UserReSet(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        self.center()

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
        self.setting_title.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/userset.title.png"))
        self.setting_title.setObjectName("setting_title")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-10, 35, 811, 141))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/reset.welcome.png"))
        self.title.setObjectName("title")

        self.userid_input = QtWidgets.QLabel(self.centralwidget)
        self.userid_input.setGeometry(QtCore.QRect(170, 210, 461, 181))
        self.userid_input.setText("")
        self.userid_input.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/get.id.name.png"))
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
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.yes.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.yes.active.png); border:0px;}
            '''
        )
        """end"""

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

        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        """end"""

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-9, -6, 811, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/elements/reset.welcome.png"))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

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