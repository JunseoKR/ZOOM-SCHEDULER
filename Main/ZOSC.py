# -*- conding: utf-8 -*-


import sys
import time
import os
import ftplib
import urllib.request
from urllib.parse import quote
import configparser    # configparser
import os.path
import requests    # requests
import threading
import datetime
from tendo import singleton    # tendo
from win10toast import ToastNotifier    # win10toast
from datetime import datetime
from datetime import timedelta

import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
me = singleton.SingleInstance()    # 중복 실행 방지

""" -----------------------------------------------------------------------------------------------------------------------------------"""

# ======================================================================================== #
# =================================== [ ZOSC 버전 확인 ] ====================================== #
# ======================================================================================== #

curVer = "2.2"

# ======================================================================================== #
# ==================================== [ 버전 꼭 확인! ] ======================================= #
# ======================================================================================== #

""" -----------------------------------------------------------------------------------------------------------------------------------"""

# Method Section =========================================================================

# 버전 체크
def Version():

    # 경로 지정
    FTP_version = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Version/Version.txt"    # Version Check 파일 경로 ( FTP 서버 )
    FTP_verPath = "C:\\ZOOM SCHEDULER\\version.txt"    # Version.txt 저장 경로
    # 서버 요청
    urllib.request.urlretrieve(FTP_version, FTP_verPath)
    # 파일 읽기
    FTPread = open(FTP_verPath, 'r')
    UpdateVer = FTPread.read()
    FTPread.close()
    # 파일 제거
    os.remove(FTP_verPath)

    # 버전 판별
    if curVer == UpdateVer:
        print("최신 버전입니다.\n")
        pass

    else:
        print("업데이트가 있습니다.\n")

# 공지 로딩
def Notice():
    NoticeLink = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Notice/Notice_Ex.txt"
    NoticePath = "C:\\ZOOM SCHEDULER\\Notice.txt"
    urllib.request.urlretrieve(NoticeLink, NoticePath)
    # 파일 읽기
    NoticeRead = open(NoticePath, 'r', encoding='UTF8')
    Read = NoticeRead.readlines()

    NoticeA = Read[0]
    NoticeB = Read[1]
    NoticeC = Read[2]
    NoticeD = Read[3]
    NoticeE = Read[4]
    NoticeF = Read[5]
    NoticeG = Read[6]
    NoticeH = Read[7]
    NoticeI = Read[8]
    NoticeJ = Read[9]
    NoticeK = Read[10]
    NoticeL =  Read[11]
    NoticeM = Read[12]
    NoticeRead.close()
    Notice = NoticeA+NoticeB+NoticeC+NoticeD+NoticeE+NoticeF+NoticeG+NoticeH+NoticeI+NoticeJ+NoticeK+NoticeL+NoticeM
    os.remove(NoticePath)
    return Notice


# ========================================================================================

# FTP Section =============================================================================

def FTP_StatusCheck():    # FTP 서버 상태 확인
    Checkurl = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Check/Status.txt"
    CheckPath = "C:\\ZOOM SCHEDULER\\FTP Status.txt"
    urllib.request.urlretrieve(Checkurl, CheckPath)
    Checktxt = open(CheckPath, 'r')
    Check = Checktxt.read()
    Checktxt.close()
    os.remove(CheckPath)

    def Warn():
        toaster = ToastNotifier()
        toaster.show_toast("ZOOM SCHEDULER", "데이터 서버 오류\n개발자에게 문의하세요.", icon_path="C:\\ZOOM SCHEDULER\\Include\\Main.ico", duration=7, threaded=True)

    if Check == "Running":
        return
    else:
        Warn()
        sys.exit()
        
def FTP_UserCheck(Name, FTPPath, Local):
    # FTP Server 로그인
    FTP_host = "DataJunseo.ipdisk.co.kr"
    FTP_user = "ZOSC"
    FTP_password = "ZOSC"

    FTP_Check = ftplib.FTP(FTP_host, FTP_user, FTP_password)
    FTP_Check.cwd(FTPPath)    # FTP File Path
    FTP_List = FTP_Check.nlst()    # FTP 목록 불러옴

    if Name in FTP_List:    # 사용자 판단
        return

    else:
        FTP_Upload(Name, FTPPath, Local)    # FTP_Upload 함수 호출

def FTP_Upload(Name, FTPPath, Local):
    # FTP Server 로그인
    FTP_host = "DataJunseo.ipdisk.co.kr"
    FTP_user = "ZOSC"
    FTP_password = "ZOSC"

    #FTP Connect
    FTP_Upload = ftplib.FTP(FTP_host, FTP_user, FTP_password)
    FTP_Upload.cwd(FTPPath)    #FTP File Path

    FTP_Open = open(Local, 'rb')    #Upload File Open
    FTP_Upload.storbinary('STOR '+Name, FTP_Open)    #FTP File Upload
    FTP_Open.close()    #FTP Close
    FTP_Upload.close()    #File Close



""" [ Method ] --------------------------------------------------------------------------------------------------------------------"""

FTP_StatusCheck()

Version()




""" [ RunTime ] ------------------------------------------------------------------------------------------------------------------- """

class Worker(QObject):
    sig_numbers = pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    @pyqtSlot()
    def Server_Connect(self, parent=None):
        
        def day_check():
            check_day = datetime.today().weekday()
            return check_day

        def alert():
            toaster = ToastNotifier()
            toaster.show_toast("ZOOM SCHEDULER", "주말에는 실행할 수 없습니다.", icon_path="C:\\ZOOM SCHEDULER\\Include\\Main.ico", duration=2, threaded=False)

        def today():
            today = datetime.today().weekday()
            today = today + 1
            return today


        def Run():
            self.sig_numbers.emit("서버 연결중")
            if today() == 3:
                Subject_1 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) + "_"+str(today())+"_1"    # 서버 주소 지정
                Subject_2 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) + "_"+str(today())+"_2"
                Subject_3 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) + "_"+str(today())+"_3"
                Subject_4 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) +  "_"+str(today())+"_4"
                ZOSCA_1 = requests.get(Subject_1)    # 서버 요청
                ZOSCA_2 = requests.get(Subject_2)
                ZOSCA_3 = requests.get(Subject_3)
                ZOSCA_4 = requests.get(Subject_4)
                ZOSC_1 = ''.join(filter(str.isalnum, ZOSCA_1.text))    # 모든 특수문자 제거
                ZOSC_2 = ''.join(filter(str.isalnum, ZOSCA_2.text))
                ZOSC_3 = ''.join(filter(str.isalnum, ZOSCA_3.text))
                ZOSC_4 = ''.join(filter(str.isalnum, ZOSCA_4.text))
                Z1_TrA = ZOSC_1[13:15]    # 문자열 처리
                Z1_SjA = ZOSC_1[22:32]
                Z2_TrA = ZOSC_2[13:15]
                Z2_SjA = ZOSC_2[22:32]
                Z3_TrA = ZOSC_3[13:15]
                Z3_SjA = ZOSC_3[22:32]
                Z4_TrA = ZOSC_4[13:15]
                Z4_SjA = ZOSC_4[22:32]

                configread = configparser.ConfigParser()
                configread.read('C:\\ZOOM SCHEDULER\\SEXY.ini', encoding='utf-8')
                configread.sections()
                # 선생님 성함 읽어오기
                Z1_Tr = configread['TrName'][Z1_TrA]
                Z2_Tr = configread['TrName'][Z2_TrA]
                Z3_Tr = configread['TrName'][Z3_TrA]
                Z4_Tr = configread['TrName'][Z4_TrA]
                Z1_Sj = configread['Subject'][Z1_SjA]
                Z2_Sj = configread['Subject'][Z2_SjA]
                Z3_Sj = configread['Subject'][Z3_SjA]
                Z4_Sj = configread['Subject'][Z4_SjA]
                # 링크 변수 처리
                Z1_Link = Z1_Sj + "_" + Z1_Tr
                Z2_Link = Z2_Sj + "_" + Z2_Tr
                Z3_Link = Z3_Sj + "_" + Z3_Tr
                Z4_Link = Z4_Sj + "_" + Z4_Tr
                # 링크 읽어오기
                Link1 = configread['Link'][Z1_Link]
                Link2 = configread['Link'][Z2_Link]
                Link3 = configread['Link'][Z3_Link]
                Link4 = configread['Link'][Z4_Link]

                # Time Information Scraping
                Time = requests.get('https://zosc-server.run.goorm.io/Time')
                Time1 = Time.text[4:9]
                Time2 = Time.text[15:20]
                Time3 = Time.text[26:31]
                Time4 = Time.text[37:42]


            else:
                Subject_1 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) + "_"+str(today())+"_1"    # 서버 주소 지정
                Subject_2 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) + "_"+str(today())+"_2"
                Subject_3 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) + "_"+str(today())+"_3"
                Subject_4 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) +  "_"+str(today())+"_4"
                Subject_5 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) +  "_"+str(today())+"_5"
                Subject_6 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) +  "_"+str(today())+"_6"
                Subject_7 = "https://zosc-server.run.goorm.io/" + str(Middle.Grade) + "_" + str(Middle.ClassR) +  "_"+str(today())+"_7"
                ZOSCA_1 = requests.get(Subject_1)    # 서버 요청
                ZOSCA_2 = requests.get(Subject_2)
                ZOSCA_3 = requests.get(Subject_3)
                ZOSCA_4 = requests.get(Subject_4)
                ZOSCA_5 = requests.get(Subject_5)
                ZOSCA_6 = requests.get(Subject_6)
                ZOSCA_7 = requests.get(Subject_7)
                ZOSC_1 = ''.join(filter(str.isalnum, ZOSCA_1.text))    # 모든 특수문자 제거
                ZOSC_2 = ''.join(filter(str.isalnum, ZOSCA_2.text))
                ZOSC_3 = ''.join(filter(str.isalnum, ZOSCA_3.text))
                ZOSC_4 = ''.join(filter(str.isalnum, ZOSCA_4.text))
                ZOSC_5 = ''.join(filter(str.isalnum, ZOSCA_5.text))
                ZOSC_6 = ''.join(filter(str.isalnum, ZOSCA_6.text))
                ZOSC_7 = ''.join(filter(str.isalnum, ZOSCA_7.text))
                Z1_TrA = ZOSC_1[13:15]    # 문자열 처리
                Z1_SjA = ZOSC_1[22:32]
                Z2_TrA = ZOSC_2[13:15]
                Z2_SjA = ZOSC_2[22:32]
                Z3_TrA = ZOSC_3[13:15]
                Z3_SjA = ZOSC_3[22:32]
                Z4_TrA = ZOSC_4[13:15]
                Z4_SjA = ZOSC_4[22:32]
                Z5_TrA = ZOSC_5[13:15]
                Z5_SjA = ZOSC_5[22:32]
                Z6_TrA = ZOSC_6[13:15]
                Z6_SjA = ZOSC_6[22:32]
                Z7_TrA = ZOSC_7[13:15]
                Z7_SjA = ZOSC_7[22:32]

                # Read Class Information ini
                configread = configparser.ConfigParser()
                configread.read('C:\\ZOOM SCHEDULER\\SEXY.ini', encoding='utf-8')
                configread.sections()
                # 선생님 성함 읽어오기
                Z1_Tr = configread['TrName'][Z1_TrA]
                Z2_Tr = configread['TrName'][Z2_TrA]
                Z3_Tr = configread['TrName'][Z3_TrA]
                Z4_Tr = configread['TrName'][Z4_TrA]
                Z5_Tr = configread['TrName'][Z5_TrA]
                Z6_Tr = configread['TrName'][Z6_TrA]
                Z7_Tr = configread['TrName'][Z7_TrA]
                # 과목명 읽어오기
                Z1_Sj = configread['Subject'][Z1_SjA]
                Z2_Sj = configread['Subject'][Z2_SjA]
                Z3_Sj = configread['Subject'][Z3_SjA]
                Z4_Sj = configread['Subject'][Z4_SjA]
                Z5_Sj = configread['Subject'][Z5_SjA]
                Z6_Sj = configread['Subject'][Z6_SjA]
                Z7_Sj = configread['Subject'][Z7_SjA]
                # 링크 변수 처리
                Z1_Link = Z1_Sj + "_" + Z1_Tr
                Z2_Link = Z2_Sj + "_" + Z2_Tr
                Z3_Link = Z3_Sj + "_" + Z3_Tr
                Z4_Link = Z4_Sj + "_" + Z4_Tr
                Z5_Link = Z5_Sj + "_" + Z5_Tr
                Z6_Link = Z6_Sj + "_" + Z6_Tr
                Z7_Link = Z7_Sj + "_" + Z7_Tr
                # 링크 읽어오기
                Link1 = configread['Link'][Z1_Link]
                Link2 = configread['Link'][Z2_Link]
                Link3 = configread['Link'][Z3_Link]
                Link4 = configread['Link'][Z4_Link]
                Link5 = configread['Link'][Z5_Link]
                Link6 = configread['Link'][Z6_Link]
                Link7 = configread['Link'][Z7_Link]

                # Time Information Scraping
                Time = requests.get('https://zosc-server.run.goorm.io/Time')
                Time1 = Time.text[4:9]
                Time2 = Time.text[15:20]
                Time3 = Time.text[26:31]
                Time4 = Time.text[37:42]
                Time5 = Time.text[48:53]
                Time6 = Time.text[59:64]
                Time7 = Time.text[70:75]


            def RunTime(result, Link):  # 메인 런타임

                def Notification(): # win10toast 수업시간 알림
                    toaster = ToastNotifier()
                    toaster.show_toast("ZOOM SCHEDULER", "수업이 5초 후에 켜집니다.", icon_path="C:\\ZOOM SCHEDULER\\Include\\Main.ico", duration=5, threaded=True)

                def Start_Check():  # 줌 LINK 실행(OS)
                    Notification()
                    time.sleep(5)
                    os.system("start "+Link)


                threading.Timer(result, Start_Check).start()
                print("Timer Ready")

            def Time_Set(Time, Link):   # 시간 판별 - 타이머

                # 현재 시간 불러오기
                now = time.localtime()
                now_times = ("%02d:%02d" % (now.tm_hour, now.tm_min))

                # 시간 값 형식 판별
                HM = '%H:%M'

                # 남은 시간 계산 ( 단위 | 시:분:초)
                time_dif = datetime.strptime(Time, HM) - datetime.strptime(now_times, HM)

                # 시간 판별 ( 0 미만일 시 내일로 넘어감 ( 오류 처리 ) )
                if time_dif.days < 0:
                    time_dif = timedelta(days=0,seconds=time_dif.seconds, microseconds=time_dif.microseconds)

                # 시:분:초 형식에서 시, 분 받아오기
                hour, minute, null = str(time_dif).split(":")

                # 남은 시간, 분 모두 초로 변환
                result_min = int(hour)*3600 + int(minute)*60 - 120


                RunTime(result_min, Link)   # 런타임 호출



            # Time_Set() → RunTime() 함수 호출
            self.sig_numbers.emit("서버 연결 완료")
            self.sig_numbers.emit("시간표 불러오기 완료")
            if today() == 3:
                Time_Set(Time1, Link1)
                Time_Set(Time2, Link2)
                Time_Set(Time3, Link3)
                Time_Set(Time4, Link4)

            else:
                Time_Set(Time1, Link1)
                Time_Set(Time2, Link2)
                Time_Set(Time3, Link3)
                Time_Set(Time4, Link4)
                Time_Set(Time5, Link5)
                Time_Set(Time6, Link6)
                Time_Set(Time7, Link7)

            self.sig_numbers.emit("RunTime Ready")
            time.sleep(2)
            self.sig_numbers.emit("ZOSC 백그라운드 실행중")

        if day_check() == 0:
            alert()
            print(quit)

        elif day_check() == 6:
            alert()
            print(quit)

        else:
            Run()



""" [ UI ] --------------------------------------------------------------------------------------------------------------------------- """


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
        self.RunState.setGeometry(QtCore.QRect(740, 515, 320, 40)) # (x, y, w, h)
        self.RunState.setFont(QtGui.QFont("Noto Sans CJK KR Medium",15))
        self.RunState.setStyleSheet("Color : Black")
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

        self.btn_hide.clicked.connect(self.Tray)

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


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Notice_Check(self):
        self.label.setText(Notice())


    def Tray(self):
        self.hide()
        self.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC가 백그라운드에서 실행됩니다.",
                QSystemTrayIcon.Information,
                2000
            )


    def quit(self):
        self.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC의 모든 프로세스가 종료됩니다.",
                QSystemTrayIcon.Information,
                2000
            )
        time.sleep(2)
        self.close()

    def Running(self):
        self.tray_icon.showMessage(
            "ZOOM SCHEDULER",
            "ZOSC가 이미 실행중입니다.",
            QSystemTrayIcon.Information,
            2000
        )
        self.hide()



    def Activation_Reason(self, reason):
        if  reason == QSystemTrayIcon.DoubleClick:
            self.show()


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

    @pyqtSlot(str)
    def updateStatus(self, status):

        self.RunState.setText('{}'.format(status))
        if status == "ZOSC 백그라운드 실행중":
            self.Tray()

  
class UI_User(QMainWindow):    # User Setting UI

    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def setupUi(self, MainWindow):

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setObjectName("사용자 설정")
        self.resize(800, 500)
        self.setMinimumSize(QtCore.QSize(800, 500))
        self.center()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/landscape/ID-Name.png"))
        self.background.setObjectName("background")

        self.setting_title = QtWidgets.QLabel(self.centralwidget)
        self.setting_title.setGeometry(QtCore.QRect(-10, 0, 811, 41))
        self.setting_title.setText("")
        self.setting_title.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/userset.title.png"))
        self.setting_title.setObjectName("setting_title")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-10, 35, 811, 141))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/welcome.png"))
        self.title.setObjectName("title")

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

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "사용자 설정"))

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


class UI_Setting(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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


# import zosc_resource_rc

""" [ Connect ] -------------------------------------------------------------------------------------------------------------------- """
class Middle(QObject):

    # Class 변수 선언
    Grade = 0
    Class = 00
    ClassR = 0
    Number = 00
    Name = "기본값"
    ID = 00000
    Premium = 0

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_Userset = UI_User()

    # 입력 처리 수정 필요
    def User_New(self):
        Setting_ini = 'C:\\ZOOM SCHEDULER\\Setting.ini'
        config_User = configparser.ConfigParser()
        config_User['User'] = {}
        config_User['User']['Grade'] = Middle.ID[0:1]
        config_User['User']['Class'] = Middle.ID[1:3]
        config_User['User']['Number'] = Middle.ID[3:5]
        config_User['User']['Name'] = Middle.Name
        Middle.Grade = Middle.ID[0:1]
        Middle.Class = Middle.ID[1:3]
        Middle.Number = Middle.ID[3:5]
        Middle.ClassR = Middle.Class.strip("0")

        with open(Setting_ini, 'w', encoding='utf-8') as configfile:
            config_User.write(configfile)

        # FTP Server Upload
        User_Temp = "C:\\ZOOM SCHEDULER\\"+str(Middle.ID)+" "+str(Middle.Name)+".ini"

        config_FTP = configparser.ConfigParser()
        config_FTP['User'] = {}
        config_FTP['Premium'] = {}
        config_FTP['User']['Grade'] = Middle.ID[0:1]
        config_FTP['User']['Class'] = Middle.ID[1:3]
        config_FTP['User']['Number'] = Middle.ID[3:5]
        config_FTP['User']['Name'] = Middle.Name
        config_FTP['Premium']['Premium'] = "0"

        with open(User_Temp, 'w', encoding='utf-8') as configfile:
            config_FTP.write(configfile)

        # FTP Upload
        FTP_UpPath = "./HDD1/DATA/ZOSC/User/"+str(Middle.Grade)+"학년 "+str(Middle.Class)+"반/"    # FTP Path 지정
        FTP_UpName = Middle.ID+" "+Middle.Name+".ini"    # User ini 파일 이름 지정
        FTP_UserCheck(FTP_UpName, FTP_UpPath, User_Temp)    # 사용자 확인
        os.remove(User_Temp)    # Upload Temp File Delete
        Middle.Premium = "0"    # Premium = None
        


class Connect(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_main = UI_MainWindow()
        self.gui_userset = UI_User()

        # 창 setupUi
        self.gui_main.setupUi(MainWindow)
        self.gui_userset.setupUi(MainWindow)
        

        # Worker() 쓰레드
        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        # Middle() 쓰레드
        self.middle = Middle()
        self.middle_thread = QThread()
        self.middle.moveToThread(self.middle_thread)
        self.middle_thread.start()

        # 신호 연결
        self._connectSignals()

        # 시스템 트레이
        self.gui_main.tray_icon.show()
        self.gui_main.show()   # |  → 메인 창 로딩
        self.gui_main.hide()     # |
        # 사용자 체크
        self.Check()



    
    def _connectSignals(self):
        self.gui_main.btn_run.clicked.connect(self.worker.Server_Connect)
        self.gui_main.btn_notice.clicked.connect(self.gui_main.Notice_Check)
        self.gui_userset.btn_yes.clicked.connect(self.Bridge)
        self.gui_userset.btn_close.clicked.connect(self.CloseA)
        self.worker.sig_numbers.connect(self.gui_main.updateStatus)
        
        

    def Check(self):
        Setting_ini = 'C:\\ZOOM SCHEDULER\\Setting.ini'

        if os.path.isfile(Setting_ini):
            config_User = configparser.ConfigParser()
            config_User.read(Setting_ini, encoding='utf-8')    # ini 파일 설정
            config_User.sections()    # Section 값 읽어오기

            Middle.Grade = config_User['User']['Grade']    # Grade 값 읽기
            Middle.Class = config_User['User']['Class']    # Class 값 읽기  :  [ 0n ] 으로 저장됨
            Middle.Number = config_User['User']['Number']    # Number 값 읽기
            Middle.Name = config_User['User']['Name']    # Name 값 읽기
            Middle.ClassR = Middle.Class.strip("0")    # Class의 "0" 제거
            Middle.ID = Middle.Grade+Middle.Class+Middle.Number    # 학번 조합

            # [ Premium Tier Check ]
            SCName = quote(Middle.Name)    # [ 중요 ] : 한글 → ASCII로 변환 필요!
            User_Get = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/DATA/ZOSC/User/"+str(Middle.Grade)+"%ed%95%99%eb%85%84%20"+str(Middle.Class)+"%eb%b0%98/"+str(Middle.ID)+"%20"+SCName+".ini"
             # 경로 지정
            UserPrCheck = "C:\\ZOOM SCHEDULER\\PrCheck.ini"
            # 서버 요청
            urllib.request.urlretrieve(User_Get, UserPrCheck)
            config_PrCheck = configparser.ConfigParser()
            config_PrCheck.read(UserPrCheck, encoding='utf-8')
            config_PrCheck.sections()
            Middle.Premium = config_PrCheck['Premium']['Premium']
            # 파일 제거
            os.remove(UserPrCheck)
            self.gui_main.show()

        else:
            self.gui_userset.show()
            self.Hello()


    def Bridge(self):
        Middle.ID = self.gui_userset.input_id.text()
        Middle.Name = self.gui_userset.input_name.text()

        self.middle.User_New()
        self.gui_main.show()
        self.gui_userset.close()
        self.Inf()

    def CloseA(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "학번, 이름을 입력하지 않으시면 ZOSC 사용이 불가합니다.",
                QSystemTrayIcon.Warning,
                2000
            )
        time.sleep(4)
        sys.exit()

    def Hello(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "만나서 반가워요!\n학번과 이름을 입력해 주세요.",
                QSystemTrayIcon.Information,
                2000
            )

    def Inf(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC를 사용해주셔서 감사합니다!",
                QSystemTrayIcon.Information,
                2000
            )

        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC 사용 방법은 개발자 페이지에서 확인 가능합니다.",
                QSystemTrayIcon.Information,
                2000
            )


""" -----------------------------------------------------------------------------------------------------------------------------------"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Connect(app)
    sys.exit(app.exec_())