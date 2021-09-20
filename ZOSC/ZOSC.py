# -*- conding: utf-8 -*-

# [ ZOSC Modules ]

# Normal Modules
import os
import sys
import re
import time
import datetime
from datetime import datetime
from datetime import timedelta
import json
from tendo import singleton    # tendo
# Alert Modules
from win10toast import ToastNotifier    # win10toast
from win10toast_click import ToastNotifier    # win10toast-click
# Request / MySQL Modules
import pymysql
import requests    # requests
import urllib.request
from urllib.parse import quote
# Selenium or Web Modules
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import webbrowser
# Process Modules
import wmi
import threading
from win32com.client import GetObject

# PyQt5 Modules
import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# UI Modules
from Main import *
from UserSet import *
from Setting import *
from DiagSet import *
from Diagnosis import *





""" -----------------------------------------------------------------------------------------------------------------------------------"""

# ======================================================================================== #
# =================================== [ ZOSC 버전 확인 ] ===================================== #
# ======================================================================================== #

curVer = "3.0"

# ======================================================================================== #
# ==================================== [ 버전 꼭 확인! ] ====================================== #
# ======================================================================================== #




""" -----------------------------------------------------------------------------------------------------------------------------------"""
# Support Section =========================================================================
def Support():
    SupportChat = "https://open.kakao.com/o/s2HyPjpc"
    webbrowser.open(SupportChat)

def P_Insert():
    Link = "http://nwjun.com/ZOSC"
    webbrowser.open(Link)

# Method Section =========================================================================

# 지원


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
        if 400<CHECK<1000:
            Server_Warn()
            sys.exit()
        else:
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
    print("Current Version : "+curVer+"\nServer Version : "+UpdateVer)
    # 버전 판별
    if curVer == UpdateVer:
        return

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
    DB_ZOSC = pymysql.connect(host='zosc.iptime.org', user='ZOSC', passwd='JunseoKR', db='ZOSC', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    pass
except:
    print("[ ZOSC ] MySQL SERVER ERROR")
    toaster = ToastNotifier()
    toaster.show_toast("ZOSC DATA 서버 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=3, threaded=True, callback_on_click=Support)
    sys.exit()

try:
    DB_ANALYSIS = pymysql.connect(host='zosc.iptime.org', user='ZOSC', passwd='JunseoKR', db='ANALYSIS', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    pass
except:
    print("[ ANALYSIS ] MySQL SERVER ERROR")
    toaster = ToastNotifier()
    toaster.show_toast("ZOSC DATA 서버 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=3, threaded=True, callback_on_click=Support)
    sys.exit()




""" [ ZOSC Analysis ] -------------------------------------------------------------------------------------------------------------------- """

class Analytic(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)


    def Analysis(self):

        def Input(NT, PROCESS):
            try:
                with DB_ANALYSIS.cursor() as cursor:
                    query = "INSERT INTO `{}-{}-{}-{}` (DATE, TIME, PROCESS) VALUES (NOW(), '{}', '{}')".format(Middle.School, Middle.Grade, Middle.Class, Middle.Name, NT, PROCESS)
                    cursor.execute(query)

            finally:
                DB_ANALYSIS.close


        def Check():
            def NowTime():
                now = time.localtime()
                NT = ("%02d:%02d" % (now.tm_hour, now.tm_min))
                return NT

            Process = os.popen('wmic process get description').read().split()
            for List in range(len(JSON_ANALYSIS['Analysis']['Process'])):
                if DATA[List] in Process:
                    BRIDGE = DATA[List]
                    Input(NowTime(), BRIDGE)
                    print("ANALYSIS Status : \""+BRIDGE+"\"")
                    pass

                else:
                    pass
            threading.Timer(300, Check).start()

        REQURL = "http://zosc.iptime.org/ZOSC/Data/Analysis"
        JSON_ANALYSIS = requests.get(REQURL).json()
        DATA = JSON_ANALYSIS['Analysis']['Process']
        threading.Timer(5, Check).start()
        


""" [ ZOSC RunTime ] ------------------------------------------------------------------------------------------------------------------- """
# sig_numbers 문제 해결 필요 / 오류 처리 필요
class Worker(QObject):
    sig_numbers = pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_main = UI_MainWindow()
        self.ais = Analytic()

    @pyqtSlot()
    def Server_Connect(self, parent=None):

# ========================================================================================
        def today():
            today = datetime.today().weekday()
            return today


# RunTime ===============================================================================

        def Run():
            # Warn ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            def Server_Warn():
                toaster = ToastNotifier()
                toaster.show_toast("서버 연결 오류", "알림을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=3, threaded=True, callback_on_click=Support)
                self.sig_numbers.emit("ZOSC 서버 연결 오류")
                time.sleep(5)
                self.sig_numbers.emit("")

            def DB_Warn():
                toaster = ToastNotifier()
                toaster.show_toast("등록되지 않은 회의", "화상 회의 정보가 등록되지 않았습니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=3, threaded=True, callback_on_click=P_Insert)
                self.sig_numbers.emit("회의 정보 오류")
                time.sleep(5)
                self.sig_numbers.emit("")

            def TimeREQ_Warn():
                toaster = ToastNotifier()
                toaster.show_toast("시간표 처리 오류 [ 수업 시간 ]", "시간표의 수업시간을 불러오는데 오류가 발생했습니다.\n여기를 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=3, threaded=True, callback_on_click=Support)
                self.sig_numbers.emit("수업시간 처리 오류")
                time.sleep(5)
                self.sig_numbers.emit("")

            def TimeTable_Warn():
                toaster = ToastNotifier()
                toaster.show_toast("시간표 처리 오류 [ 시간표 데이터 ]", "시간표의 수업 데이터를 불러오는데 오류가 발생했습니다.\n여기를 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=3, threaded=True, callback_on_click=Support)
                self.sig_numbers.emit("수업 데이터 처리 오류")
                time.sleep(5)
                self.sig_numbers.emit("")

            def Weekend_Warn():
                toaster = ToastNotifier()
                toaster.show_toast("ZOOM SCHEDULER", "주말에는 실행할 수 없습니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Error.ico", duration=2, threaded=False)
                self.sig_numbers.emit("주말 실행 제한")
                time.sleep(5)
                self.sig_numbers.emit("")


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
                print("Ready [{}교시]".format(ClassTime))


            # TimeSet ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            def TIME_SET(School, TN, Subject, DayString, ClassTime):   # 시간 판별 - 타이머

                # 현재 시간 불러오기
                now = time.localtime()
                now_times = ("%02d:%02d" % (now.tm_hour, now.tm_min))
                # 시간 값 형식 판별
                HM = '%H:%M'
                # 남은 시간 계산 ( 단위 | 시:분:초)
                time_dif = datetime.strptime(TIME[ClassTime-2], HM) - datetime.strptime(now_times, HM)
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
                print(School, TN, Subject, ClassTime)
                try:
                    with DB_ZOSC.cursor() as cursor:
                        query = "SELECT ZOOM, GOOGLEMEET, GOORM FROM TEACHER WHERE School = '{}' AND REQN = '{}'".format(School, TN)
                        cursor.execute(query)
                        DATA = cursor.fetchone()
                        if DATA == None:
                            DB_Warn()
                            return

                        else:
                            ZOOM.append(DATA['ZOOM'])
                            MEET.append(DATA['GOOGLEMEET'])
                            GOORM.append(DATA['GOORM'])
                            TIME_SET(School, TN, Subject, DayString, ClassTime)
                finally:
                    DB_ZOSC.close
                    

            # Request ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

            # SET
            DAY_ = 3
            ZOOM = []
            MEET = []
            GOORM = []
            TIME = []

            # 주말 예외 처리
            if DAY_ == (5 or 6):
                Weekend_Warn()
                return

            else:
                # TimeTable Data Request
                self.sig_numbers.emit("Data Request")
                try:
                    REQ_URL = "http://zosc.iptime.org/ZOSC/Data/" + str(Middle.Grade) + "/" + str(Middle.Class)    # TimeTable Request URL
                    TimeTable = requests.get(REQ_URL).json()    # TimeTable Request
                    REQ_TIME = requests.get('http://zosc.iptime.org/ZOSC/Data/Time').json()    # Time Set Request

                    # 수업시간 처리
                    for i in range(1, 8):
                        try:
                            INPUT = REQ_TIME[i]
                            TIME.append(INPUT[2:7])
                        except:
                            break
                            TimeREQ_Warn()
                            return

                    # 수업 데이터 처리
                    for TIME_ in range(7):
                        try:
                            DATA = TimeTable[DAY_][TIME_]
                            Select(Middle.School, DATA['teacher'], DATA['subject'], DATA['weekdayString'], DATA['classTime'])
                            print(DATA)
                        except:
                            break
                            TimeTable_Warn()
                            return

                except:
                    Server_Warn()
                    return


            
            # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
            # [ RunTime 실행 완료 ]
            self.sig_numbers.emit("집중도 분석 기능 시작")
            self.ais.Analysis()
            time.sleep(1)
            self.sig_numbers.emit("ALL READY")
            time.sleep(1)
            self.sig_numbers.emit("ZOSC 백그라운드 실행중")
            

# ========================================================================================

        Run()





""" [ Connect ] -------------------------------------------------------------------------------------------------------------------- """

class Middle(QObject):

    # Class 변수 선언
    School = None
    Grade = 0
    Class = 00
    Number = 00
    Name = "NULL"
    URID = "NULL"
    PW = "NULL"
    City = "NULL"
    Level = "NULL"
    Birth = 000000
    DSPW = None

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)




class Diagnosis(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    def Start(self):
        try:
            path = chromedriver_autoinstaller.install()
            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            options.add_argument("window-size=1920x1080")
            options.add_argument("disable-gpu")
            self.driver = webdriver.Chrome(path, options = options)
            self.driver.get("https://hcs.eduro.go.kr/#/loginHome")
            print("웹 로딩 완료")
            WebDriverWait(self.driver, 200).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/div/ul[1]/li[1]/div/button'))
                        )
            
            # 중학교 선택 후 자가진단 참여하기 시작
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/ul[1]/li[1]/div/button').click()
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/button').click()
            print("분류 선택 완료")

            # 학교 검색 버튼이 누를 수 있을때까지 대기
            WebDriverWait(self.driver, 200).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td/button'))
                        )
            # 학교 검색 창 입장
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td/input').click()
            print("검색 창 클릭 이벤트 완료")

            # 학교 선택창이 누를 수 있을때까지 대기
            WebDriverWait(self.driver, 200).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/input'))
                        )
            # 드롭다운 메뉴창 관련 오브젝트 select 활용으로 전라남도 선택
            select = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select')) 
            if self.getCityLevel(Middle.City) == '-1':
                os.system('cls')
                print("지역 선택값에서 예외가 발생하였습니다")
                self.driver.quit()
                return
            select.select_by_value(self.getCityLevel(Middle.City))
            print("지역 선택 완료")

            # 위와 동일하게 학교 급 수 중학교로 설정
            select = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td/select'))
            if self.getSchoolLevel(Middle.Level) == '-1':
                os.system('cls')
                print("학교 급 수 선택값에서 예외가 발생하였습니다")
                self.driver.quit()
                return
            select.select_by_value(self.getSchoolLevel(Middle.Level))
            print("Level 선택 완료")

            # 학교명 광양 백운중으로 검색 후 검색 버튼 클릭
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys(Middle.School)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
            print("학교 지정 완료")

            # 검색 버튼 아래 확인 버튼 나올때까지 대기
            WebDriverWait(self.driver, 200).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/ul/li/a'))
            )

            # 확인 창 누르고 학교 선택 클릭
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/ul/li/a').click()
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[2]/input').click()
            print("최종 선택 완료")

            # 추가 창 뜰때까지 대기
            WebDriverWait(self.driver, 200).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/input'))
            )

            # 성명 , 생년월일 기입
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr[2]/td/input').send_keys(Middle.Name)
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr[3]/td/input').send_keys(Middle.Birth)
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/input').click()
            print("사용자 정보 출력 완료")
            
            # 패스워드 창 뜰때까지 대기
            WebDriverWait(self.driver, 200).until(
                EC.element_to_be_clickable((By.ID, 'password'))
            )
            
            # 패스워드 창 클릭해서 보안 키보드 띄우기
            self.driver.find_element_by_id('password').click()
            print("PW 창 클릭 이벤트 완료")

            # aria-label 에 버튼 번호 뜨는거 활용해서 클릭
            for pw in list(Middle.DSPW):
                self.driver.find_element_by_xpath("//a[@aria-label='{}']".format(pw)).click()  
            
            # 로그인
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/input').click()
            print("로그인 클릭 이벤트 완료")

            # 자가진단 시작 확인
            WebDriverWait(self.driver, 200).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/section[2]/div[2]/ul/li/a/span[1]'))
            )

            # 자가진단 시작
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/section[2]/div[2]/ul/li/a/span[1]').click() 
            print("자가진단 시작")
            
            # 완료 버튼 누를 수 있을때까지 대기
            WebDriverWait(self.driver, 200).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/dl[1]/dd/ul/li[1]/input'))
            )
            
            # 모두 아니오 , 후 최종 완료
            self.driver.find_element_by_id('survey_q1a1').click()    # survey_q1a2 → '예' 버튼 ID [ 건강 이상 ]
            self.driver.find_element_by_id('survey_q2a1').click()    # survey_q2a2 → '예' 버튼 ID
            self.driver.find_element_by_id('survey_q3a1').click()    # survey_q3a2 → '예' 버튼 ID
            self.driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/input').click()
            print("Complete")
            self.driver.quit()
            return
        except Exception as e:
            print("예외가 발생하였습니다")
            return    # 체크 유무에 따라서 선택 따로
    
    def getCityLevel(self, city):
        if city == "서울특별시":
            return '1'
        elif city == "부산광역시":
            return '2'   
        elif city == "대구광역시":
            return '3'
        elif city == "인천광역시":
            return '4'  
        elif city == "광주광역시":
            return '5'
        elif city == "대전광역시":
            return '6'  
        elif city == "울산광역시":
            return '7'
        elif city == "세종특별자치시":
            return '8'  
        elif city == "경기도":
            return '10'
        elif city == "강원도":
            return '11'  
        elif city == "충청북도":
            return '12'
        elif city == "충청남도":
            return '13'  
        elif city == "전라북도":
            return '14'
        elif city == "전라남도":
            return '15'  
        elif city == "경상북도":
            return '16'
        elif city == "경상남도":
            return '17'  
        elif city == "제주특별자치도":
            return '18' 
        else:
            return '-1'  

    def getSchoolLevel(self, school):
        if school == "유치원":
            return '1'      
        elif school == "초등학교":
            return '2' 
        elif school == "중학교":
            return '3' 
        elif school == "고등학교":
            return '4' 
        elif school == "특수학교 등":
            return '5'      
        else:
            return '-1'



class Connect(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui_main = UI_MainWindow()
        self.gui_userset = UI_User()
        self.gui_setting = UI_Setting()
        self.gui_diagset = UI_DiagSet()
        self.gui_diagnosis = UI_Diagnosis()

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
        # Diagnosis() 쓰레드
        self.diagnosis = Diagnosis()
        self.diagnosis_thread = QThread()
        self.diagnosis.moveToThread(self.diagnosis_thread)
        self.diagnosis_thread.start()
        # Analytic() 쓰레드
        self.ais = Analytic()
        self.ais_thread = QThread()
        self.ais.moveToThread(self.ais_thread)
        self.ais_thread.start()
        
        # 신호 연결
        self._connectSignals()

        # 시스템 트레이
        self.gui_main.tray_icon.show()

        
        # 사용자 체크
        self.Check()
    

    
    def _connectSignals(self):
        # Main GUI
        self.gui_main.btn_hide.clicked.connect(self.gui_main.Tray)     # Tray
        self.gui_main.btn_close.clicked.connect(self.gui_main.Quit)    # Exit
        self.gui_main.btn_run.clicked.connect(self.worker.Server_Connect)     # Runtime
        self.gui_main.btn_notice.clicked.connect(self.Notice_Refresh)     # Notice
        self.gui_main.btn_setting.clicked.connect(self.gui_setting.show)     # Setting UI

        # Setting GUI
        self.gui_setting.btn_info.clicked.connect(self.Information)     # Information Webpage
        self.gui_setting.btn_close.clicked.connect(self.Setting_Close)     # Setting UI Close
        
        # UserSetting GUI
        self.gui_userset.btn_close.clicked.connect(self.User_Cancel)     # UserSet Cancel

        # Diagnosis
        self.gui_diagnosis.btn_yes.clicked.connect(self.gui_diagnosis.hide)
        self.gui_diagnosis.btn_yes.clicked.connect(self.diagnosis.Start)

        # PyqtSlot
        self.worker.sig_numbers.connect(self.gui_main.updateStatus)     # PyqtSlot Connect
        


    def Quit(self):    # 오류 처리 확인 필요
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "ZOSC의 모든 프로세스가 종료됩니다.",
                QSystemTrayIcon.Information,
                2000
            )
        self.gui_main.hide()
        time.sleep(2)
        sys.exit()    # 오류 처리 확인 필요 / 미사용

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
            #Middle.City = JSON_USER['DIAGNOSIS']['City']
            #Middle.Level = JSON_USER['DIAGNOSIS']['Level']
            #Middle.Birth = JSON_USER['DIAGNOSIS']['Birth']
            #Middle.DSPW = JSON_USER['DIAGNOSIS']['PW']
            

            try:
                with DB_ZOSC.cursor() as self.cursor:
                    query = "SELECT * FROM USER WHERE SCHOOL = '{}' AND Grade = {} AND Class = {} AND Number = {} AND Name = '{}' AND URID = '{}' AND PW = '{}'".format(Middle.School, Middle.Grade, Middle.Class, Middle.Number, Middle.Name, Middle.URID, Middle.PW)
                    DB_RES = self.cursor.execute(query)

                if DB_RES == 1:
                    self.gui_main.show()
                    self.Welcome()
                    try:
                        Middle.City = JSON_USER['DIAGNOSIS']['City']
                        Middle.Level = JSON_USER['DIAGNOSIS']['Level']
                        Middle.Birth = JSON_USER['DIAGNOSIS']['Birth']
                        Middle.DSPW = JSON_USER['DIAGNOSIS']['PW']
                        self.gui_diagnosis.show()
                    except:
                        self.gui_diagset.show()
                    finally:
                        J.close()
                if DB_RES == 0:
                    print("[DATA ERROR] MySQL DATA NOT FOUND!")
                    sys.exit()
            except:
                print("[ ZOSC ] DATA SERVER ERROR!")
            finally:
                DB_ZOSC.close


        else:
            self.gui_userset.show()

    def Diagnosis(self):
        self.gui_diagnosis.hide()
        self.diagnosis.Start()
        pass

    def Notice_Refresh(self):
        self.gui_main.label.setText(Notice())
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "공지사항이 새로고침되었습니다.",
                QSystemTrayIcon.Information,
                2000
            )

    def Setting_Close(self):
        self.gui_setting.hide()
        return

    def Information(self):
        InfoURL = 'http://nwjun.com'
        webbrowser.open(InfoURL)
        
    def User_Cancel(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "학번, 이름을 입력하지 않으시면 ZOSC 사용이 불가합니다.",
                QSystemTrayIcon.Warning,
                2000
            )
        time.sleep(2)
        sys.exit()

    def Welcome(self):
        self.gui_main.tray_icon.showMessage(
                "{}님 안녕하세요!".format(Middle.Name),
                "{} {}학년 {}반 {}\n로그인되었습니다.".format(Middle.School, Middle.Grade, Middle.Class, Middle.Name),
                QSystemTrayIcon.Information,
                2000
            )

    def Hello(self):
        self.gui_main.tray_icon.showMessage(
                "ZOOM SCHEDULER",
                "반가워요!\nZOSC를 이용하시려면 로그인이 필요합니다.",
                QSystemTrayIcon.Information,
                2000
            )    # 미사용

    def ERROR_User(self):
        os.remove("C:\\ZOOM SCHEDULER\\Setting.ini")
        self.gui_main.tray_icon.showMessage(
                "사용자 정보 오류",
                "문제를 해결했습니다.\nZOSC를 다시 실행하세요.",
                QSystemTrayIcon.Warning,
                2000
            )
        time.sleep(3)
        sys.exit()    # 재사용




""" -----------------------------------------------------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Connect(app)
    sys.exit(app.exec_())