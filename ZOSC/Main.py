# -*- conding: utf-8 -*-

import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ZOSC import *
from Setting import *
from UserReset import *



class UI_MainWindow(QMainWindow):    # Main UI

    def __init__(self):
        super().__init__()
        self.setupUi(self)



    def setupUi(self, MainWindow):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(1100, 650)
        self.center()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-10, -10, 1121, 61))
        self.title.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/zosc.png"))
        self.title.setObjectName("title")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 40, 1111, 611))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/landscape/Main.png"))
        self.background.setObjectName("background")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 150, 645, 382)) # (x, y, w, h)
        self.label.setFont(QtGui.QFont("Noto Sans CJK KR Medium",15))
        self.label.setStyleSheet("Color : Black")
        self.label.setText(Notice())

        self.RunState = QtWidgets.QLabel(self.centralwidget)
        self.RunState.setGeometry(QtCore.QRect(765, 515, 280, 40)) # (x, y, w, h)
        self.RunState.setFont(QtGui.QFont("Noto Sans CJK KR Medium",15))
        self.RunState.setStyleSheet("Color : Black")
        self.RunState.setAlignment(Qt.AlignHCenter)
        self.RunState.setStyleSheet("color: #5E56FF; border-style: solid; border-width: 3px; border-color: #9EA9FF; border-radius: 10px; ")

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)

        quit_action = QAction("종료", self)
        quit_action.triggered.connect(self.quit)
        self.tray_icon.activated.connect(self.Activation_Reason)
        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        
        

        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """RunTime""" 
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(865, 575, 151, 61))
        self.btn_run.setStyleSheet('''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.run.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.run.active.png); border:0px;}
            ''')

        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(28)
        self.btn_run.setFont(font)
        self.btn_run.setObjectName("btn_run")

        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """Notice"""
        self.btn_notice = QtWidgets.QPushButton(self.centralwidget)
        self.btn_notice.setGeometry(QtCore.QRect(15, 80, 101, 71))
        self.btn_notice.setStyleSheet('''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/notice.refresh.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/notice.refresh.active.png); border:0px;}
            ''')

        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.btn_notice.setFont(font)
        self.btn_notice.setObjectName("btn_notice")

        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """Setting"""
        self.btn_setting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setting.setGeometry(QtCore.QRect(10, 5, 30, 30))
        self.btn_setting.setStyleSheet('''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.setting.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.setting.active.png); border:0px;}
            ''')

        self.btn_setting.setObjectName("btn_setting")
        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """Hide"""
        self.btn_hide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hide.setGeometry(QtCore.QRect(990, 10, 40, 20))
        self.btn_hide.setStyleSheet('''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/line.hide.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/line.hide.active.png); border:0px;}
            ''')


        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """Close"""
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(1045, 10, 40, 20))
        self.btn_close.setStyleSheet('''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.close.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.close.active.png); border:0px;}
            ''')
        self.btn_close.setObjectName("btn_close")

        self.btn_close.clicked.connect(self.quit)
        """end"""


        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZOOM SCHEDULER"))

        

    def quit(self):
        self.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC의 모든 프로세스가 종료됩니다.",
                QSystemTrayIcon.Information,
                2000
            )
        time.sleep(2)
        sys.exit()

    def Running(self):
        self.tray_icon.showMessage(
            "ZOOM SCHEDULER",
            "ZOSC가 이미 실행중입니다.",
            QSystemTrayIcon.Information,
            2000
        )
        self.hide()



    # App/UI Interactions ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    def Activation_Reason(self, reason):
        if  reason == QSystemTrayIcon.DoubleClick:
            self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # PyqtSlot ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    @pyqtSlot(str)
    def updateStatus(self, status):

        self.RunState.setText('{}'.format(status))
        if status == "ZOSC 백그라운드 실행중":
            self.Tray()