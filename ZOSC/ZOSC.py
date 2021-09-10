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
import pymysql
import pandas
import ftplib    # ftplib 제거 필요!
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
# 버전 / 공지 / Request Data




""" -----------------------------------------------------------------------------------------------------------------------------------"""

# Method Section =========================================================================

# 지원
def Support():
    SupportChat = "https://open.kakao.com/o/s2HyPjpc"
    webbrowser.open(SupportChat)

# 서버 상태 확인
def Server_Check():
    def Server_Warn():
        toaster = ToastNotifier()
        toaster.show_toast("ZOSC 서버 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=7, threaded=True, callback_on_click=Support)

    # SERVER Check
    SERVERURL = 'http://zosc.iptime.org/'
    try:
        RES = requests.head(url=SERVERURL, timeout=3)
        CHECK = RES.status_code
        pass

    except requests.exceptions.Timeout:
        Server_Warn()
        sys.exit()
    except requests.exceptions.TooManyRedirects:
        Server_Warn()
        sys.exit()
    except requests.exceptions.RequestException as e:
        Server_Warn()
        sys.exit()

Server_Check()

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
        pass

    else:
        sys.exit()

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



# DB SECTION ===========================================================================

try:
    DB = pymysql.connect(host='zosc.iptime.org', user='ZOSC', passwd='JunseoKR', db='ZOSC', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    pass
except:
    print("MySQL SERVER ERROR")
    toaster = ToastNotifier()
    toaster.show_toast("ZOSC DATA 서버 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=7, threaded=True, callback_on_click=Support)
    sys.exit()


# FTP Section ============================================================================
# MySQL 수정 필요



# MySQL 수정 필요


""" [ ZOSC Analysis ] -------------------------------------------------------------------------------------------------------------------- """

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

        def Get_DB():
            pass

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
            # 문제 : JSON 데이터에 Key가 없고 값만 반환됨 → 반복문 사용하여 일주일 링크 다 요청 하며 함수로 보냄 → 배열에 값 넣음



            for RE in range(1, 8):
                DATA_URL = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.Class) + "/" + str(RE)    # TimeTable Request URL
                DATA_REQ = requests.get(DATA_URL).json()
                print(DATA_REQ)



            #urllib.request.urlretrieve(DATA_URL, DATA_PATH)    # Server Request

            #with open(CACHE, 'r', encoding='UTF8') as D:
                #JSON_USER = json.load(D)

            #D.close()



            

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

        Run()





""" [ Connect ] -------------------------------------------------------------------------------------------------------------------- """
# 사용자 회원가입 웹 이동 필요
# 수정 중지 / 수정 필요

class Middle(QObject):

    # Class 변수 선언
    School = "NULL"
    Grade = 0
    Class = 00
    Number = 00
    Name = "NULL"
    URID = "NULL"
    PW = "NULL"

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        

    def User_New(self):
        Setting_ini = 'C:\\ZOOM SCHEDULER\\Cache_User.json'
        JSON_USER = dict()
        User = dict()
        User[""]
        Middle.Grade = Middle.ID[0:1]
        Middle.Class = Middle.ID[1:3]
        Middle.Number = Middle.ID[3:5]
        Middle.ClassR = Middle.Class.strip("0")

        with open(Setting_ini, 'w', encoding='utf-8') as configfile:
            config_User.write(configfile)
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
        config_FTP['User']['Grade'] = Middle.ID[0:1]
        config_FTP['User']['Class'] = Middle.ID[1:3]
        config_FTP['User']['Number'] = Middle.ID[3:5]
        config_FTP['User']['Name'] = Middle.Name

        with open(User_Temp, 'w', encoding='utf-8') as configfile:
            config_FTP.write(configfile)

        # FTP Upload
        FTP_UpPath = "./HDD1/DATA/ZOSC/User/"+str(Middle.Grade)+"학년 "+str(Middle.Class)+"반/"    # FTP Path 지정
        FTP_UpName = Middle.ID+" "+Middle.Name+".ini"    # User ini 파일 이름 지정
        FTP_UserCheck(FTP_UpName, FTP_UpPath, User_Temp)    # 사용자 확인
        os.remove(User_Temp)    # Upload Temp File Delete
        return




class Connect(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_main = UI_MainWindow()
        self.gui_userset = UI_User()
        self.gui_setting = UI_Setting()
        self.gui_UserReset = UI_UserReSet()

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
        CACHE = 'C:\\ZOOM SCHEDULER\\CACHE.json'

        if os.path.isfile(CACHE):
            with open(CACHE, 'r', encoding='UTF8') as J:
                JSON_USER = json.load(J)
            Middle.School = JSON_USER['USER']['School']
            Middle.Grade = JSON_USER['USER']['Grade']
            Middle.Class = JSON_USER['USER']['Class']
            Middle.Number = JSON_USER['USER']['Number']
            Middle.Name = JSON_USER['USER']['Name']
            Middle.URID = JSON_USER['USER']['URID']
            Middle.PW = JSON_USER['USER']['PW']
            Middle.ID = Middle.Grade+Middle.Class+Middle.Number
            J.close()

            try:
                with DB.cursor() as self.cursor:
                    query = "SELECT * FROM USER WHERE SCHOOL = '{}' AND Grade = {} AND Class = {} AND Number = {} AND Name = '{}' AND URID = '{}' AND PW = '{}'".format(Middle.School, Middle.Grade, Middle.Class, Middle.Number, Middle.Name, Middle.URID, Middle.PW)
                    DB_RES = self.cursor.execute(query)

                if DB_RES == 1:
                    self.gui_main.show()
                    self.Welcome()
                if DB_RES == 0:
                    print("[DATA ERROR] MySQL DATA NOT FOUND!")
                    sys.exit()
            except:
                print("DATA SERVER ERROR!")
            finally:
                DB.close()


            # 파일 제거


        else:
            self.gui_userset.show()
            self.Hello()    # MySQL Connect

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