""" [ Import ] --------------------------------------------------------------------------------------------------- """

# Local에서 실행 시 pip으로 모듈을 설치해야 함.
# 현재 필요한 모듈 이외는 모두 주석 처리하였습니다.
# ( 주석 처리된 모듈은 모두 사용 예정입니다. )



# Import [ Qt UI ]
# from PyQt5.QtGui import
# import pyautogui as pg

# Import [ Ftplib ]
# import ftplib

# Import [ OS ]
import os

# Import [ URL Request ]
import urllib.request

# Import [ configparser_ini File ]
import configparser

# Import [ File path ]
import os.path

# Imoport requests
import requests







""" [ Function ] --------------------------------------------------------------------------------------------------- """


# Function (def) Section
# 기능 삽입 구역


# ZOSC 버전
curVer = "2.2"



# Version Check
# 프로그램 버전 체크

def Version():

    # 경로 지정
    FTP_version = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Version/Version.txt"
    FTP_verPath = "C:\\ZOOM SCHEDULER\\version.txt"

    # 서버 요청
    urllib.request.urlretrieve(FTP_version, FTP_verPath)
    
    # 파일 읽기
    FTPread1 = open(FTP_verPath, 'r')
    UpdateVer = FTPread1.read()
    FTPread1.close()

    # 파일 제거
    os.remove(FTP_verPath)

    # 버전 판별
    if curVer == UpdateVer:
        pass

    else:
        print("업데이트가 있습니다.\n")








# Folder Create

def Folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)




# USER Information Check

def User_New():
    
    # User Information Setting
    UserSetting_ini = 'C:\ZOOM SCHEDULER\Setting.ini'


    # ini File Read
    if os.path.isfile(UserSetting_ini):
        config_User = configparser.ConfigParser()

        config_User.read(UserSetting_ini, encoding='utf-8')
        config_User.sections()

        Grade = config_User['User']['Grade']
        Class = config_User['User']['Class']
        Number = config_User['User']['Number']
        Name = config_User['User']['Name']

        ID = Grade+Class+Number
        print(ID)
        print(Name)
        pass



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




    Userini_path = 'C:\ZOOM SCHEDULER\Setting.ini'
    with open(Userini_path, 'w', encoding='utf-8') as configfile:
        config_User.write(configfile)




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




# Subject Schedule ZOSC.ini Create
# Server Request

def ZOSC_ini():

    Sub1, Sub2, Sub3, Sub4, Sub5, Sub6, Sub7 = input("테스트용 시간표 입력 : ").split()
    Time1, Time2, Time3, Time4, Time5, Time6, Time7 = input("\n테스트용 시간 입력 ( 입력형식 = HHMM ) :").split()

    config_Subject = configparser.ConfigParser()

    # Save Subject Schedule
    config_Subject['Subject'] = {}
    config_Subject['Subject']['Subject1'] = Sub1
    config_Subject['Subject']['Subject2'] = Sub2
    config_Subject['Subject']['Subject3'] = Sub3
    config_Subject['Subject']['Subject4'] = Sub4
    config_Subject['Subject']['Subject5'] = Sub5
    config_Subject['Subject']['Subject6'] = Sub6
    config_Subject['Subject']['Subject7'] = Sub7

    # Save Time Schedule
    config_Subject['Time'] = {}
    config_Subject['Time']['Time1'] = Time1
    config_Subject['Time']['Time2'] = Time2
    config_Subject['Time']['Time3'] = Time3
    config_Subject['Time']['Time4'] = Time4
    config_Subject['Time']['Time5'] = Time5
    config_Subject['Time']['Time6'] = Time6
    config_Subject['Time']['Time7'] = Time7
    
    ZOSCini_path = 'C:\ZOOM SCHEDULER\ZOSC.ini'
    with open(ZOSCini_path, 'w', encoding='utf-8') as configfile:
        config_Subject.write(configfile)
    



def Server_Get():
    
    # nodeJS 서버 상태 확인
    # goorm IDE는 실행 중이므로 code 200 발생

    nodeJS_Check = requests.get('https://zosc-server.run.goorm.io/Time')
    if nodeJS_Check.status_code == 200:
        print("nodeJS Server Online\n")

    else:
        print("nodeJS Server Offline\n")

       






    # 임시 서버 요청 테스트

    Subject1 = requests.get('https://zosc-server.run.goorm.io/2_9_1_1')
    print(Subject1)

    Subject2 = requests.get('https://zosc-server.run.goorm.io/2_1_1_2')
    Subject3 = requests.get('https://zosc-server.run.goorm.io/2_1_1_3')
    Subject4 = requests.get('https://zosc-server.run.goorm.io/2_1_1_4')
    Subject5 = requests.get('https://zosc-server.run.goorm.io/2_1_1_5')
    Subject6 = requests.get('https://zosc-server.run.goorm.io/2_1_1_6')
    Subject7 = requests.get('https://zosc-server.run.goorm.io/2_1_1_7')

    Time = requests.get('https://zosc-server.run.goorm.io/Time')






""" [ Main ] --------------------------------------------------------------------------------------------------- """

# Main Runtime

Folder('\ZOOM SCHEDULER')

Version()

User_New()

ZOSC_ini()

State()

Server_Get()

print("\nTest Complete\n")

print(exit)