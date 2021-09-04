# -*- conding: utf-8 -*-


import os
import os.path
import sys
import time
import threading
import wmi
import json
import datetime
from datetime import datetime
from datetime import timedelta
import webbrowser
import ftplib
import requests    # requests
import urllib.request
from urllib.parse import quote
import configparser    # configparser
from win32com.client import GetObject
from tendo import singleton    # tendo
from win10toast import ToastNotifier    # win10toast
from win10toast_click import ToastNotifier    # win10toast-click

import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Main import *
from UserSet import *
from Setting import *
from UserReset import *




""" -----------------------------------------------------------------------------------------------------------------------------------"""

# ======================================================================================== #
# =================================== [ ZOSC 버전 확인 ] ====================================== #
# ======================================================================================== #

curVer = "3.0"

# ======================================================================================== #
# ==================================== [ 버전 꼭 확인! ] ======================================= #
# ======================================================================================== #

# [ JSON ]
# 버전 / 공지 / 




""" -----------------------------------------------------------------------------------------------------------------------------------"""

# Method Section =========================================================================

# 버전 체크
def Version():

    # 경로 지정
    REQURL = "http://zosc.iptime.org/ZOSC/Data/Set"    # Version Check 파일 경로 ( NodeJS 서버 )
    REQPATH = "C:\\ZOOM SCHEDULER\\REQUEST.json"
    urllib.request.urlretrieve(REQURL, REQPATH)
    
    with open(REQPATH, 'r') as J:
        JSON_VERSION = json.load(J)
    UpdateVer = JSON_VERSION['zosc']['version']
    J.close()
    os.remove(REQPATH)

    # 버전 판별
    if curVer == UpdateVer:
        print("최신 버전입니다.\n")
        pass

    else:
        print("업데이트가 있습니다.\n")    # NodeJS 서버

# 공지 로딩
def Notice():
    REQURL = "http://zosc.iptime.org/ZOSC/Data/Notice"
    REQPATH = "C:\\ZOOM SCHEDULER\\Notice.txt"
    urllib.request.urlretrieve(REQURL, REQPATH)
    # 파일 읽기
    NoticeRead = open(REQPATH, 'r', encoding='UTF8')
    Notice = NoticeRead.read()
    NoticeRead.close()
    os.remove(REQPATH)
    return Notice    # NodeJS 서버

# 지원
def Support():
    SupportChat = "https://open.kakao.com/o/s2HyPjpc"
    webbrowser.open(SupportChat)


# FTP Section =============================================================================
# MySQL 수정 필요
# FTP → MySQL

def Server_Check():

    def FTP_Warn():
        toaster = ToastNotifier()
        toaster.show_toast("ZOSC FTP 서버 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=7, threaded=True, callback_on_click=Support)

    def SERVER_Warn():
        toaster = ToastNotifier()
        toaster.show_toast("ZOSC 서버 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=7, threaded=True, callback_on_click=Support)

    # FTP Check
    FTPURL = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Check/Status.txt"
    FTPPATH = "C:\\ZOOM SCHEDULER\\FTP Status.txt"
    urllib.request.urlretrieve(FTPURL, FTPPATH)
    FTPTXT = open(FTPPATH, 'r')
    FTPCHECK = FTPTXT.read()
    FTPTXT.close()
    os.remove(FTPPATH)

    # SERVER Check
    SERVERURL = 'http://zosc.iptime.org/ZOSC'
    try:
        RES = requests.head(url=SERVERURL, timeout=10)
        CHECK = RES.status_code
        pass

    except requests.exceptions.Timeout:
        FTP_Warn()
        sys.exit()
    except requests.exceptions.TooManyRedirects:
        FTP_Warn()
        sys.exit()
    except requests.exceptions.RequestException as e:
        FTP_Warn()
        sys.exit()

    if FTPCHECK == "Running":
        return

    else:
        FTP_Warn()
        sys.exit()    # SERVER 상태 확인 [ 완료 ] / 이전 후 FTP 상태 확인 코드 제거 필요
        
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
        FTP_Upload(Name, FTPPath, Local)    # FTP 미사용 예정 → MySQL

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
    FTP_Upload.close()    # FTP 미사용 예정 → MySQL

# MySQL 수정 필요


""" [ ZOSC RunTime ] ------------------------------------------------------------------------------------------------------------------- """

class Analysis(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)


    def NowTime(self):
        now = time.localtime()
        today = ("%04d.%02d.%02d" % (now.tm_year, now.tm_mon, now.tm_mday))
        return today


    def Analysis(self):
        Analysis_Result = "C:\\ZOOM SCHEDULER\\Analysis\\Analysis Result.txt"

        def String(String):
            String = String.replace(" ", "")
            return String


        def RunTime():
            with open("C:\\ZOOM SCHEDULER\\Analysis_Process.txt", 'w') as PL:
                Process = os.popen('wmic process get description').read().split()
                PL.write(str(Process))
            i = 0
            with open("C:\\ZOOM SCHEDULER\\Analysis_Process.txt", 'r') as PL:
                for i, line in enumerate(PL):
                    Process_List = String(line)
                    i += 2
            #os.remove("C:\\ZOOM SCHEDULER\\Analysis_Process.txt")
            if "chrome.exe" in Process_List:
                print("Chrome Running")



        if os.path.isfile(Analysis_Result):
            RunTime()

        else:
            New = open(Analysis_Result, 'w')
            New.close()
            RunTime()




""" [ ZOSC RunTime ] ------------------------------------------------------------------------------------------------------------------- """

class Worker(QObject):
    sig_numbers = pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_main = UI_MainWindow()
        self.analysis = Analysis()

    @pyqtSlot()
    def Server_Connect(self, parent=None):

        def today():
            today = datetime.today().weekday()
            today = today + 1
            return today

        # RunTime ===============================================================================

        def Run():

            #self.analysis.Analysis()

            self.sig_numbers.emit("서버 연결중")
            
            # Alert ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            def Server_Warn():
                toaster = ToastNotifier()
                toaster.show_toast("서버 연결 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=5, threaded=True, callback_on_click=Support)
                self.sig_numbers.emit("AWS 서버 연결 오류")
                time.sleep(5)
                self.sig_numbers.emit("")


            
            # Time Function ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            Inf_Request = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Data/SEXY.ini"
            Inf_Save = "C:\\ZOOM SCHEDULER\\SEXY.ini"
            urllib.request.urlretrieve(Inf_Request, Inf_Save)

            if today() == 3:
                Subject_1 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) + "/"+str(today())+"/1"    # 서버 주소 지정
                Subject_2 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) + "/"+str(today())+"/2"
                Subject_3 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) + "/"+str(today())+"/3"
                Subject_4 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) +  "/"+str(today())+"/4"
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
                try:
                    Z1_Tr = configread['TrName'][Z1_TrA]
                    Z2_Tr = configread['TrName'][Z2_TrA]
                    Z3_Tr = configread['TrName'][Z3_TrA]
                    Z4_Tr = configread['TrName'][Z4_TrA]
                    Z1_Sj = configread['Subject'][Z1_SjA]
                    Z2_Sj = configread['Subject'][Z2_SjA]
                    Z3_Sj = configread['Subject'][Z3_SjA]
                    Z4_Sj = configread['Subject'][Z4_SjA]

                except KeyError:
                    os.remove(Inf_Save)
                    Server_Warn()
                    return

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
                Time = requests.get('http://zosc.iptime.org/ZOSC/Data/Time')
                Time1 = Time.text[4:9]
                Time2 = Time.text[15:20]
                Time3 = Time.text[26:31]
                Time4 = Time.text[37:42]
                os.remove(Inf_Save)


            else:
                Subject_1 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) + "/"+str(today())+"/1"    # 서버 주소 지정
                Subject_2 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) + "/"+str(today())+"/2"
                Subject_3 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) + "/"+str(today())+"/3"
                Subject_4 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) +  "/"+str(today())+"/4"
                Subject_5 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) +  "/"+str(today())+"/5"
                Subject_6 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) +  "/"+str(today())+"/6"
                Subject_7 = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.ClassR) +  "/"+str(today())+"/7"
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
                try:
                    Z1_Tr = configread['TrName'][Z1_TrA]
                    Z2_Tr = configread['TrName'][Z2_TrA]
                    Z3_Tr = configread['TrName'][Z3_TrA]
                    Z4_Tr = configread['TrName'][Z4_TrA]
                    Z5_Tr = configread['TrName'][Z5_TrA]
                    Z6_Tr = configread['TrName'][Z6_TrA]
                    Z7_Tr = configread['TrName'][Z7_TrA]

                except KeyError:
                    os.remove(Inf_Save)
                    Server_Warn()
                    return

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
                Time = requests.get('http://zosc.iptime.org/ZOSC/Data/Time')
                Time1 = Time.text[4:9]
                Time2 = Time.text[15:20]
                Time3 = Time.text[26:31]
                Time4 = Time.text[37:42]
                Time5 = Time.text[48:53]
                Time6 = Time.text[59:64]
                Time7 = Time.text[70:75]
                os.remove(Inf_Save)

            
            # Main ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            def RunTime(result, Link):  # 메인 런타임

                def Notification(): # win10toast 수업시간 알림
                    toaster = ToastNotifier()
                    toaster.show_toast("ZOOM SCHEDULER", "수업이 5초 후에 켜집니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\icon.ico", duration=5, threaded=True)

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
            


        # DayCheck ==============================================================================
        
        def alert():
            toaster = ToastNotifier()
            toaster.show_toast("ZOOM SCHEDULER", "주말에는 실행할 수 없습니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Error.ico", duration=2, threaded=False)

        if today() == 6:
            alert()

            return

        elif today() == 7:
            alert()
            return

        else:
            Run()




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
        return

    def User_Reset(self):
        Setting_ini = 'C:\\ZOOM SCHEDULER\\Setting.ini'
        os.remove(Setting_ini)
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
        return




class Connect(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_main = UI_MainWindow()
        self.gui_userset = UI_User()
        self.gui_setting = UI_Setting()
        self.gui_UserReset = UI_UserReSet()

        Server_Check()

        Version()

        # 창 setupUi
        self.gui_main.setupUi(MainWindow)
        

        
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
        # Worker() 쓰레드
        self.analysis = Analysis()
        self.analysis_thread = QThread()
        self.analysis.moveToThread(self.analysis_thread)
        self.analysis_thread.start()

        # 신호 연결
        self._connectSignals()

        # 시스템 트레이
        self.gui_main.tray_icon.show()

        # 사용자 체크
        self.Check()


    
    def _connectSignals(self):
        # Main GUI
        self.gui_main.btn_hide.clicked.connect(self.gui_main.Tray)     # Tray
        self.gui_main.btn_run.clicked.connect(self.worker.Server_Connect)     # Runtime
        self.gui_main.btn_notice.clicked.connect(self.Notice_Refresh)     # Notice
        self.gui_main.btn_setting.clicked.connect(self.gui_setting.show)     # Setting UI

        # Setting GUI
        self.gui_setting.btn_reset.clicked.connect(self.Reset_show)     # UserReset UI
        self.gui_setting.btn_info.clicked.connect(self.Information)     # Information Webpage
        self.gui_setting.btn_close.clicked.connect(self.Setting_Close)     # Setting UI Close
        
        # UserSetting GUI
        self.gui_userset.btn_yes.clicked.connect(self.User_Save)     # UserSetting
        self.gui_userset.btn_close.clicked.connect(self.User_Cancel)     # UserSet Cancel
        
        # UserReset GUI
        self.gui_UserReset.btn_yes.clicked.connect(self.Resetting)     # User Resetting
        self.gui_UserReset.btn_close.clicked.connect(self.gui_UserReset.hide)

        # PyqtSlot
        self.worker.sig_numbers.connect(self.gui_main.updateStatus)     # PyqtSlot Connect
        


    

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
            try:
                urllib.request.urlretrieve(User_Get, UserPrCheck)
                
            except urllib.error.HTTPError:
                self.ERROR_User()
                
            config_PrCheck = configparser.ConfigParser()
            config_PrCheck.read(UserPrCheck, encoding='utf-8')
            config_PrCheck.sections()
            Middle.Premium = config_PrCheck['Premium']['Premium']
            # 파일 제거
            os.remove(UserPrCheck)
            self.gui_main.show()
            self.Welcome()

        else:
            self.gui_userset.show()
            self.Hello()

    def Notice_Refresh(self):
        self.gui_main.label.setText(Notice())
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "공지사항이 새로고침되었습니다.",
                QSystemTrayIcon.Information,
                2000
            )

    def Setting_Close(self):
        self.gui_UserReset.hide()
        self.gui_setting.hide()

    def Information(self):
        InfoURL = 'http://nwjun.com'
        webbrowser.open(InfoURL)

    def Reset_show(self):
        self.gui_UserReset.show()
        self.gui_main.tray_icon.showMessage(
                "사용자 재설정 주의",
                "사용자를 잘못 등록한 경우에만\n재설정하시기 바랍니다.",
                QSystemTrayIcon.Warning,
                2000
            )

    def User_Save(self):
        Middle.ID = self.gui_userset.input_id.text()
        Middle.Name = self.gui_userset.input_name.text()

        self.middle.User_New()
        self.gui_main.show()
        self.gui_userset.close()
        self.Awesome()
        
    def User_Cancel(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "학번, 이름을 입력하지 않으시면 ZOSC 사용이 불가합니다.",
                QSystemTrayIcon.Warning,
                2000
            )
        time.sleep(2)
        sys.exit()

    def Resetting(self):
        Middle.ID = self.gui_UserReset.input_id.text()
        Middle.Name = self.gui_UserReset.input_name.text()

        self.middle.User_Reset()
        self.gui_UserReset.hide()
        self.Reset_Complete()

    def Welcome(self):
        self.gui_main.tray_icon.showMessage(
                "또 만났네요!",
                "{}님 안녕하세요!".format(Middle.Name),
                QSystemTrayIcon.Information,
                2000
            )

    def Hello(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "만나서 반가워요!\n학번과 이름을 입력해 주세요.",
                QSystemTrayIcon.Information,
                2000
            )

    def Awesome(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC를 사용해주셔서 감사합니다!",
                QSystemTrayIcon.Information,
                2000
            )
        
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC 사용 방법은 공식 페이지에서 확인 가능합니다.",
                QSystemTrayIcon.Information,
                2000
            )

    def Reset_Complete(self):
        self.gui_main.tray_icon.showMessage(
                "사용자 재설정 완료",
                "사용자가 재설정 되었습니다.\n{} {}".format(Middle.ID, Middle.Name),
                QSystemTrayIcon.Information,
                2000
            )

    def ERROR_User(self):
        os.remove("C:\\ZOOM SCHEDULER\\Setting.ini")
        self.gui_main.tray_icon.showMessage(
                "사용자 정보 오류",
                "문제를 해결했습니다.\nZOSC를 다시 실행하세요.",
                QSystemTrayIcon.Warning,
                2000
            )
        time.sleep(3)
        sys.exit()




""" -----------------------------------------------------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Connect(app)
    sys.exit(app.exec_())