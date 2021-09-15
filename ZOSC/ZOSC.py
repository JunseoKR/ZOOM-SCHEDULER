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
# =================================== [ ZOSC 버전 확인 ] ===================================== #
# ======================================================================================== #

curVer = "3.0"

# ======================================================================================== #
# ==================================== [ 버전 꼭 확인! ] ====================================== #
# ======================================================================================== #




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
    JSON_SET = requests.get(REQURL).json()
    UpdateVer = JSON_SET['zosc']['version']

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
    NR = open(REQPATH, 'r', encoding='UTF8')
    Notice = NR.read()
    NR.close()
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





""" [ ZOSC Analysis ] -------------------------------------------------------------------------------------------------------------------- """

class Analysis(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)


    def NowTime(self):
        now = time.localtime()
        NT = ("%04d.%02d.%02d" % (now.tm_year, now.tm_mon, now.tm_mday))
        return NT

    def Input():
        pass

    def Record():
        pass

    def Analysis(self):
        def Check():
            while(True):
                Process = os.popen('wmic process get description').read().split()


        REQURL = ""
        

    #if "chrome.exe" in Process:




""" [ ZOSC RunTime ] ------------------------------------------------------------------------------------------------------------------- """

class Worker(QObject):
    sig_numbers = pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_main = UI_MainWindow()
        self.analysis = Analysis()

    @pyqtSlot()
    def Server_Connect(self, parent=None):

# ========================================================================================
        def today():
            today = datetime.today().weekday()
            return today


# RunTime ===============================================================================
        def Run():
            # Analysis 클래스
            self.analysis.Analysis()

            self.sig_numbers.emit("서버 연결중")
            # Alert ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            def Server_Warn():
                toaster = ToastNotifier()
                toaster.show_toast("서버 연결 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=5, threaded=True, callback_on_click=Support)
                self.sig_numbers.emit("AWS 서버 연결 오류")
                time.sleep(5)
                self.sig_numbers.emit("")

            def alert():
                toaster = ToastNotifier()
                toaster.show_toast("ZOOM SCHEDULER", "주말에는 실행할 수 없습니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Error.ico", duration=2, threaded=False)

            # RunTime ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            def RunTime(School, TN, Subject, DayString, ClassTime, TIMER):  # 메인 런타임

                def Notification(): # 수업시간 알림
                    toaster = ToastNotifier()
                    toaster.show_toast("ZOOM SCHEDULER", "[{}교시] {} {}* 선생님\n수업이 5초 후 시작됩니다.".format(ClassTime, Subject, TN), icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\icon.ico", duration=5, threaded=True)

                def Start_Check():  # 줌 LINK 실행(OS)
                    Notification()
                    time.sleep(5)
                    os.system("start "+ZOOM[ClassTime-1])

                threading.Timer(TIMER, Start_Check).start()
                print("Timer Ready")

            # TimeSet ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            def TIME_SET(School, TN, Subject, DayString, ClassTime):   # 시간 판별 - 타이머

                # 현재 시간 불러오기
                now = time.localtime()
                now_times = ("%02d:%02d" % (now.tm_hour, now.tm_min))

                # 시간 값 형식 판별
                HM = '%H:%M'

                # 남은 시간 계산 ( 단위 | 시:분:초)
                time_dif = datetime.strptime(TIME[ClassTime-1], HM) - datetime.strptime(now_times, HM)

                # 시간 판별 ( 0 미만일 시 내일로 넘어감 ( 오류 처리 ) )
                if time_dif.days < 0:
                    time_dif = timedelta(days=0,seconds=time_dif.seconds, microseconds=time_dif.microseconds)

                # 시:분:초 형식에서 시, 분 받아오기
                hour, minute, null = str(time_dif).split(":")

                # 남은 시간, 분 모두 초로 변환
                TIMER = int(hour)*3600 + int(minute)*60 - 120

                RunTime(School, TN, Subject, DayString, ClassTime, TIMER)   # 런타임 호출

            # DB ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            def Select(School, TN, Subject, DayString, ClassTime):
                print(School, TN, Subject, DayString, ClassTime)
                try:
                    with DB.cursor() as cursor:
                        query = "SELECT ZOOM, GOOGLEMEET, GOORM FROM TEACHER WHERE School = '{}' AND REQN = '{}'".format(School, TN)
                        cursor.execute(query)
                        DATA = cursor.fetchone()
                        print(DATA)
                        if DATA == None:
                            print("Error")
                            return

                        else:
                            ZOOM.append(DATA['ZOOM'])
                            MEET.append(DATA['GOOGLEMEET'])
                            GOORM.append(DATA['GOORM'])
                            TIME_SET(School, TN, Subject, DayString, ClassTime)    # 오류 처리 필요
                finally:
                    DB.close
                    

            # Request ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            # TimeTable Data Request

            DATA_URL = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.Class)    # TimeTable Request URL
            TimeTable = requests.get(DATA_URL).json()

            # SET
            DAY_ = 3
            ZOOM = []
            MEET = []
            GOORM = []

            # Time Data Request
            REQ_TIME = requests.get('http://zosc.iptime.org/ZOSC/Data/Time').json()
            TIME = []
            for i in range(1, 8):
                INPUT = REQ_TIME[i]
                TIME.append(INPUT[2:7])

            for TIME_ in range(7):
                            DATA = TimeTable[DAY_][TIME_]
                            Select(Middle.School, DATA['teacher'], DATA['subject'], DATA['weekdayString'], DATA['classTime'])
            
            
            # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            # Time_Set() → RunTime() 함수 호출
            self.sig_numbers.emit("서버 연결 완료")
            self.sig_numbers.emit("시간표 불러오기 완료")

            # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            # [ RunTime 실행 완료 ]

            self.sig_numbers.emit("RunTime Ready")
            time.sleep(1)
            self.sig_numbers.emit("ZOSC 백그라운드 실행중")
            

# ========================================================================================

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
                DB.close


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




# 함수 저장

def Save_Json():
    REQURL = "http://zosc.iptime.org/ZOSC/Data/Set"    # Version Check 파일 경로 ( NodeJS 서버 )
    REQPATH = "C:\\ZOOM SCHEDULER\\REQUEST.json"
    urllib.request.urlretrieve(REQURL, REQPATH)
    with open(REQPATH, 'r') as J:
        JSON_VERSION = json.load(J)
    UpdateVer = JSON_VERSION['zosc']['version']
    J.close()
    os.remove(REQPATH)