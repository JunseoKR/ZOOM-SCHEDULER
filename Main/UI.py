# -*- conding: utf-8 -*-


import sys
import time
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

""" [ SubProcess ] --------------------------------------------------------------------------------------------------- """
print("실행")

class RunTime(QObject):
    Process = pyqtSignal(int)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    print("호출")
    @pyqtSlot()
    def Run(self):
        _cnt = 0
        while _cnt < 10000:
            _cnt += 1
            self.sig_numbers.emit(_cnt) # pyqtSignal 에 숫자데이터를 넣어 보낸다
            print(_cnt)                 # consol에서 어떻게 진행 되는지 보기 위해서 넣어준다
            time.sleep(1)









""" [ UI ] --------------------------------------------------------------------------------------------------- """

class UI_MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 150, 645, 382)) # (x, y, w, h)
        self.label.setFont(QtGui.QFont("Noto Sans CJK KR Medium",15))
        self.label.setStyleSheet("Color : Black")
        self.label.setText("1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1")

        self.RunState = QtWidgets.QLabel(self.centralwidget)
        self.RunState.setGeometry(QtCore.QRect(740, 515, 320, 40)) # (x, y, w, h)
        self.RunState.setFont(QtGui.QFont("Noto Sans CJK KR Medium",15))
        self.RunState.setStyleSheet("Color : Black")
        self.RunState.setStyleSheet("color: #5E56FF; border-style: solid; border-width: 3px; border-color: #9EA9FF; border-radius: 10px; ")
        


        self.show()
        
        



    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setMinimumSize(1100, 650)



        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

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



        





        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """RunTime""" 
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(865, 575, 151, 61))
        self.btn_run.setStyleSheet(
            '''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.run.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.run.active.png); border:0px;}
            '''
        )

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
        self.btn_notice.setStyleSheet(
            '''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/notice.refresh.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/notice.refresh.active.png); border:0px;}
            '''
        )

        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.btn_notice.setFont(font)
        self.btn_notice.setObjectName("btn_notice")

        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """Setting"""
        self.btn_setting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setting.setGeometry(QtCore.QRect(10, 5, 30, 30))
        self.btn_setting.setStyleSheet(
            '''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.setting.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.setting.active.png); border:0px;}
            '''
        )

        self.btn_setting.setObjectName("btn_setting")
        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """Hide"""
        self.btn_hide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hide.setGeometry(QtCore.QRect(990, 10, 40, 20))
        self.btn_hide.setStyleSheet(
            '''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/line.hide.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/line.hide.active.png); border:0px;}
            '''
        )

        self.btn_hide.clicked.connect(MainWindow.showMinimized)

        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """Close"""
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(1045, 10, 40, 20))
        self.btn_close.setStyleSheet(
            '''
            QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.close.png); border:0px;}
            QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.close.active.png); border:0px;}
            '''
        )
        
        self.btn_close.setObjectName("btn_close")


        self.btn_close.clicked.connect(self.close)
        # QCoreApplication.instance().quit
        """end"""



        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    

    

    def RunTime(self):
        print("호출됨")


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

    @pyqtSlot(int)
    def updateStatus(self, status):
        self.RunState.setText('{}'.format(status))

    
# import zosc_resource_rc

class Test(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.gui = UI_MainWindow()
        self.RunTime = RunTime()
        self.RunTime_thread = QThread()
        self.RunTime.moveToThread(self.RunTime_thread)
        self.RunTime_thread.start()
        print("실행")

        self.connectSignals()

        self.gui.show()

    def connectSignals(self):
        self.gui.btn_run.clicked.connect(self.RunTime.Run)
        self.RunTime.sig_numbers.connect(self.gui.updateStatus)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())