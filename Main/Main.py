# -*- conding: utf-8 -*-

""" [ Import ] --------------------------------------------------------------------------------------------------- """




# Import [ Ftplib ]
import ftplib

# Import [ OS ]
import os

# Import [ URL Request ]
import urllib.request
from urllib.parse import quote

# Import [ configparser_ini File ]
import configparser

# Import [ File path ]
import os.path

# Imoport requests
import requests

# Import datetime
import threading

# Import time
import time

#Import datetime
import datetime
from datetime import datetime
from datetime import timedelta

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QEvent
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtGui import QMouseEvent, QCursor, QFont, QPainter

#Import win10toast
from win10toast import ToastNotifier


""" [ Function ] --------------------------------------------------------------------------------------------------- """

# Function (def) Section
# 기능 삽입 구역


# ZOSC 버전
# 업데이트 시 변경 필요
curVer = "2.2"




# Version Check
# 프로그램 버전 체크

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





def Notice():
    NoticeLink = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Notice/notice.txt"
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
    print(Notice)
    return Notice






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





# FTP Upload/Download
# FTP ID/Password 꼭 제거 후 Commit !

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





# USER Information Check

def User_New():
    # 변수 전역 설정
    global Grade
    global Class
    global ClassR
    global Number
    global Name
    global ID
    global Premium


    # User Information Setting
    UserSetting_ini = 'C:\\ZOOM SCHEDULER\\Setting.ini'

    # ini File Read
    if os.path.isfile(UserSetting_ini):
        config_User = configparser.ConfigParser()
        config_User.read(UserSetting_ini, encoding='utf-8')    # ini 파일 설정
        config_User.sections()    # Section 값 읽어오기

        Grade = config_User['User']['Grade']    # Grade 값 읽기
        Class = config_User['User']['Class']    # Class 값 읽기  :  [ 0n ] 으로 저장됨
        Number = config_User['User']['Number']    # Number 값 읽기
        Name = config_User['User']['Name']    # Name 값 읽기
        ClassR = Class.strip("0")    # Class의 "0" 제거
        ID = Grade+Class+Number    # 학번 조합

        # [ Premium Tier Check ]
        SCName = quote(Name)    # [ 중요 ] : 한글 → ASCII로 변환 필요!
        User_Get = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/DATA/ZOSC/User/"+str(Grade)+"%ed%95%99%eb%85%84%20"+str(Class)+"%eb%b0%98/"+str(ID)+"%20"+SCName+".ini"
         # 경로 지정
        UserPrCheck = "C:\\ZOOM SCHEDULER\\PrCheck.ini"
        # 서버 요청
        urllib.request.urlretrieve(User_Get, UserPrCheck)
        config_PrCheck = configparser.ConfigParser()
        config_PrCheck.read(UserPrCheck, encoding='utf-8')
        config_PrCheck.sections()
        Premium = config_PrCheck['Premium']['Premium']
        # 파일 제거
        os.remove(UserPrCheck)
        pass




    # Setting.ini Set
    else:
        while True:
            ID = input("학번을 입력하세요 : ")

            if int(ID[0:1]) >= 4:
                print("학번을 제대로 입력해 주세요.\n")
                continue

            elif int(ID[1:3]) >= 14:
                print("학번을 제대로 입력해 주세요.\n")
                continue

            elif int(ID[3:5]) >= 35:
                print("학번을 제대로 입력해 주세요.\n")
                continue

            else:
                config_User = configparser.ConfigParser()
                config_User['User'] = {}
                config_User['User']['Grade'] = ID[0:1]
                config_User['User']['Class'] = ID[1:3]
                config_User['User']['Number'] = ID[3:5]
                Grade = ID[0:1]
                Class = ID[1:3]
                Number = ID[3:5]
                ClassR = Class.strip("0")
                break


        while True:
            Name = input("이름을 입력하세요 : ")

            if len(Name) > 4:
                print("이름을 제대로 입력해 주세요.\n")
                continue

            else:
                config_User['User']['Name'] = Name

                print("[ 설정되었습니다 ]\n")
                break

        with open(UserSetting_ini, 'w', encoding='utf-8') as configfile:
            config_User.write(configfile)



        # FTP Server Upload
        User_Temp = "C:\\ZOOM SCHEDULER\\"+str(ID)+" "+str(Name)+".ini"

        config_FTP = configparser.ConfigParser()
        config_FTP['User'] = {}
        config_FTP['Premium'] = {}
        config_FTP['User']['Grade'] = ID[0:1]
        config_FTP['User']['Class'] = ID[1:3]
        config_FTP['User']['Number'] = ID[3:5]
        config_FTP['User']['Name'] = Name
        config_FTP['Premium']['Premium'] = "0"

        with open(User_Temp, 'w', encoding='utf-8') as configfile:
            config_FTP.write(configfile)


        # FTP Upload
        FTP_UpPath = "./HDD1/DATA/ZOSC/User/"+str(Grade)+"학년 "+str(Class)+"반/"    # FTP Path 지정
        FTP_UpName = ID+" "+Name+".ini"    # User ini 파일 이름 지정
        FTP_UserCheck(FTP_UpName, FTP_UpPath, User_Temp)    # 사용자 확인
        os.remove(User_Temp)    # Upload Temp File Delete
        Premium = "0"    # Premium = None





# FTP Server State Check [ URL Download ]

def State():

    url = 'http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/INF/CHECK_INF.txt'

    res = urllib.request.urlopen(url)

    data = res.read()

    State = data.decode("utf-8")

    if State == "NORMAL":
        print("\nFTP ONLINE\n")

    else:
        print("\nFTP OFFLINE\n")
        print(exit)





# Notification

def Notification():
    toaster = ToastNotifier()
    toaster.show_toast("ZOOM SCHEDULER", "수업이 5초 후에 켜집니다.", icon_path=None, duration=5, threaded=True)





# RunTime

def Server_Get():

    # nodeJS 서버 상태 확인
    # goorm IDE는 실행 중이므로 code 200 발생 ( AWS 이전 필요! )

    nodeJS_Check = requests.get('https://zosc-server.run.goorm.io/Time')
    if nodeJS_Check.status_code == 200:
        print("nodeJS Server Online\n")

    else:
        print("nodeJS Server Offline\n")





        global Z1_Sj
        global Z2_Sj
        global Z3_Sj
        global Z4_Sj
        global Z5_Sj
        global Z6_Sj
        global Z7_Sj

        global Z1_Tr
        global Z2_Tr
        global Z3_Tr
        global Z4_Tr
        global Z5_Tr
        global Z6_Tr
        global Z7_Tr





    # Schedule Scraping
    Subject_1 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_1"    # 서버 주소 지정
    Subject_2 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_2"
    Subject_3 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_3"
    Subject_4 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_4"
    Subject_5 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_5"
    Subject_6 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_6"
    Subject_7 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_7"
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
    Z1_Link = Z1_Sj+"_"+Z1_Tr
    Z2_Link = Z2_Sj+"_"+Z2_Tr
    Z3_Link = Z3_Sj+"_"+Z3_Tr
    Z4_Link = Z4_Sj+"_"+Z4_Tr
    Z5_Link = Z5_Sj+"_"+Z5_Tr
    Z6_Link = Z6_Sj+"_"+Z6_Tr
    Z7_Link = Z7_Sj+"_"+Z7_Tr
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




    def RunTime(result, Link):

        def Start_Check():    # ZOOM Start
            # UI Show Section
            Notification()
            time.sleep(5)
            os.system("start "+Link)


        print("타이머 설정 완료")
        threading.Timer(result, Start_Check).start()

        # Premium/FreeTier 판별
        if Premium == "1":
            ZOOM_Kill()
            
        else:
            pass





    def Time_Set(Time, Link):

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
        result_min = int(hour)*3600 + int(minute)*60
        if result_min >= 37800:
            print("ERROR : 시간 초과")
            os.system("taskkill /F /im Main.exe")
            os._exit(1)    # 실행 종료
            return

        RunTime(result_min, Link)




    




    # Time_Set() → RunTime() 함수 호출
    Time_Set(Time1, Link1)
    Time_Set(Time2, Link2)
    Time_Set(Time3, Link3)
    Time_Set(Time4, Link4)
    Time_Set(Time5, Link5)
    Time_Set(Time6, Link6)
    Time_Set(Time7, Link7)





def ZOOM_Kill():
    print("Out")
    os.system ( "taskkill /F /im Zoom.exe")   # 줌 종료




""" [ UI ] --------------------------------------------------------------------------------------------------- """

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
        

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 150, 645, 382)) # (x, y, w, h)

        self.label.setFont(QtGui.QFont("Noto Sans CJK KR Medium",15)) #폰트,크기 조절
        self.label.setStyleSheet("Color : Black") #글자색 변환
        self.label.setText(str(Notice()))

        





        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        """실행 버튼"""
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(865, 575, 151, 61))
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
        # 버튼 오류 해결 필요
        self.btn_notice.clicked.connect(self.Set)
        
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

    # Notice Set 함수 수정 필요
    def Set(self):
        self.label.setText(Notice()) #텍스트 변환

        
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
    Version()
    State()
    User_New()
    # Server_Get()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())



