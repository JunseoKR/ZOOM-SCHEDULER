# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QEvent
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QMouseEvent, QCursor


class Ui_MainWindow(QMainWindow):
    # self 메인 창 생성
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()



    # 메인 창 구성요소 설정
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)    # 창 프레임, 버튼 삭제
        MainWindow.setMinimumSize(1100, 650)    # 최대화, 최소화 창 고정


        # 창 기본 구성 설정
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-10, -10, 1121, 61))
        self.title.setPixmap(QtGui.QPixmap("C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/elements/zosc.png"))
        self.title.setObjectName("title")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 40, 1111, 611))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/landscape/Main.png"))
        self.background.setObjectName("background")



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """실행 버튼"""
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(840, 570, 171, 71))
        self.btn_run.setStyleSheet(
            '''
            QPushButton{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.run.png); border:0px;}
            QPushButton:hover{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.run.active.png); border:0px;}
            '''
        )

        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(28)
        self.btn_run.setFont(font)
        self.btn_run.setObjectName("btn_run")
        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """공지 버튼"""
        self.btn_notice = QtWidgets.QPushButton(self.centralwidget)
        self.btn_notice.setGeometry(QtCore.QRect(15, 80, 101, 71))
        self.btn_notice.setStyleSheet(
            '''
            QPushButton{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/notice.refresh.png); border:0px;}
            QPushButton:hover{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/notice.refresh.active.png); border:0px;}
            '''
        )

        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.btn_notice.setFont(font)
        self.btn_notice.setObjectName("btn_notice")
        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """설정 버튼"""
        self.btn_setting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setting.setGeometry(QtCore.QRect(10, 5, 30, 30))
        self.btn_setting.setStyleSheet(
            '''
            QPushButton{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.setting.png); border:0px;}
            QPushButton:hover{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.setting.active.png); border:0px;}
            '''
        )

        self.btn_setting.setObjectName("btn_setting")
        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """최소화 버튼"""
        self.btn_hide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hide.setGeometry(QtCore.QRect(990, 10, 40, 20))
        self.btn_hide.setStyleSheet(
            '''
            QPushButton{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/line.hide.png); border:0px;}
            QPushButton:hover{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/line.hide.active.png); border:0px;}
            '''
        )

        self.btn_hide.clicked.connect(MainWindow.showMinimized)

        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """종료 버튼"""
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(1045, 10, 40, 20))
        self.btn_close.setStyleSheet(
            '''
            QPushButton{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.close.png); border:0px;}
            QPushButton:hover{image:url(C:/Users/Develop/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.close.active.png); border:0px;}
            '''
        )

        self.btn_close.setObjectName("btn_close")

        # 메인창 종료
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)    # 종료 함수 호출
        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZOOM SCHEDULER"))



        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    


# import zosc_resource_rc


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
