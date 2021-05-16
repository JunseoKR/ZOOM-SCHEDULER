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





""" [ Main ] --------------------------------------------------------------------------------------------------- """

# Function (def) Section

def Folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)




# USER Information Check

def User_New():
    
    # 파일 존재하지 않으면 생성 [ Folder 함수 호출 ]
    Folder('\ZOOM SCHEDULER')


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
            Name = input("\n이름을 입력하세요 : ")

            if len(Name) > 4:
                print("이름을 제대로 입력해 주세요.\n")
                continue

            else:
                config_User['User']['Name'] = Name

                print("\n[ 설정되었습니다 ]\n")
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
        print("\nFTP ONLINE")

    else:
        print("\nFTP OFFLINE")
        print(exit)




# Subject Schedule ZOSC.ini Create

def ZOSC_ini():

    Sub1, Sub2, Sub3, Sub4, Sub5, Sub6, Sub7 = input("\n테스트용 시간표 입력 : ").split()
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
    




# URL = 'https://zosc-server.run.goorm.io/ a_b_c_d
# a, b, c, d는 모두 변수. 링크 속에 이 변수들을 넣고 선언할 수 있는가?

def Server_Get():

    Subject1 = requests.get('https://zosc-server.run.goorm.io/2_1_1_1')
    Subject2 = requests.get('https://zosc-server.run.goorm.io/2_1_1_2')
    Subject3 = requests.get('https://zosc-server.run.goorm.io/2_1_1_3')
    Subject4 = requests.get('https://zosc-server.run.goorm.io/2_1_1_4')
    Subject5 = requests.get('https://zosc-server.run.goorm.io/2_1_1_5')
    Subject6 = requests.get('https://zosc-server.run.goorm.io/2_1_1_6')
    Subject7 = requests.get('https://zosc-server.run.goorm.io/2_1_1_7')

    Time = requests.get('https://zosc-server.run.goorm.io/Time')







# Main Runtime


User_New()

ZOSC_ini()

State()

print("Test Complete")

print(exit)