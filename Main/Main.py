""" [ Import ] --------------------------------------------------------------------------------------------------- """

# Local에서 실행 시 pip으로 모듈을 설치해야 함.
# 현재 필요한 모듈 이외는 모두 주석 처리하였습니다.
# ( 주석 처리된 모듈은 모두 사용 예정입니다. )



# Import [ Qt UI ]
# from PyQt5.QtGui import
# import pyautogui as pg

# Import [ Ftplib ]
import ftplib

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

# Import datetime
import threading

# Import time
import time

#Import datetime
import datetime
from datetime import datetime
from datetime import timedelta

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
    UserSetting_ini = 'C:\\ZOOM SCHEDULER\\Setting.ini'

    global Grade
    global Class
    global ClassR
    global Number
    global Name
    global ID


    # ini File Read
    if os.path.isfile(UserSetting_ini):
        config_User = configparser.ConfigParser()

        config_User.read(UserSetting_ini, encoding='utf-8')
        config_User.sections()

        Grade = config_User['User']['Grade']
        Class = config_User['User']['Class']
        Number = config_User['User']['Number']
        Name = config_User['User']['Name']

        # 반 09 → 9
        ClassR = Class.strip("0")

        ID = Grade+Class+Number

        User_Get = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/DATA/ZOSC/User/"+str(Grade)+"학년%20"+str(Class)+"반/"+str(ID)+"%20"+Name+".txt"
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

                Grade = ID[0:1]
                Class = ID[1:3]
                Number = ID[3:5]
                
                # 반 09 → 9
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
        # [ 주의 ] : FTP ID, Password 작성 후 commit 금지!!! ( 서버 보안 )

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



        FTP_host = "DataJunseo.ipdisk.co.kr"
        FTP_user = "codedata"
        FTP_password = "codedata"
        FTP_UpPath = "./HDD1/DATA/ZOSC/User/"+str(Grade)+"학년 "+str(Class)+"반/"
        FTP_UpName = ID+" "+Name+".ini"

        FTP_Upload = ftplib.FTP(FTP_host, FTP_user, FTP_password)
        FTP_Upload.cwd(FTP_UpPath)
        print(FTP_Upload.pwd())
    
        FTP_MF = open(User_Temp, 'rb')
        FTP_Upload.storbinary('STOR '+FTP_UpName, FTP_MF)
        FTP_MF.close()
        FTP_Upload.close()
        
        os.remove(User_Temp)


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

# ***  사용 중지 ***
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





# Notification

def Notification():
    toaster = ToastNotifier()
    toaster.show_toast("ZOOM SCHEDULER", "수업이 5초 후에 켜집니다.", icon_path=None, duration=5, threaded=False)





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
    Subject_1 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_1"
    Subject_2 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_2"
    Subject_3 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_3"
    Subject_4 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_4"
    Subject_5 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_5"
    Subject_6 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_6"
    Subject_7 = "https://zosc-server.run.goorm.io/"+str(Grade)+"_"+str(ClassR)+"_1_7"

    ZOSCA_1 = requests.get(Subject_1)
    ZOSCA_2 = requests.get(Subject_2)
    ZOSCA_3 = requests.get(Subject_3)
    ZOSCA_4 = requests.get(Subject_4)
    ZOSCA_5 = requests.get(Subject_5)
    ZOSCA_6 = requests.get(Subject_6)
    ZOSCA_7 = requests.get(Subject_7)

    ZOSC_1 = ''.join(filter(str.isalnum, ZOSCA_1.text))
    ZOSC_2 = ''.join(filter(str.isalnum, ZOSCA_2.text))
    ZOSC_3 = ''.join(filter(str.isalnum, ZOSCA_3.text))
    ZOSC_4 = ''.join(filter(str.isalnum, ZOSCA_4.text))
    ZOSC_5 = ''.join(filter(str.isalnum, ZOSCA_5.text))
    ZOSC_6 = ''.join(filter(str.isalnum, ZOSCA_6.text))
    ZOSC_7 = ''.join(filter(str.isalnum, ZOSCA_7.text))


    Z1_TrA = ZOSC_1[13:15]
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

        # ZOOM Link 실행
        def Start_Check():
            # UI Show Section

            Notification()
            time.sleep(5)
            os.system("start "+Link)


        threading.Timer(result, Start_Check).start()






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

        RunTime(result_min, Link)




    now = datetime.now()
    NT = now.hour
    if NT >= 18:
        print("현재 실행이 불가합니다.")
        return





    Time_Set(Time1, Link1)
    Time_Set(Time2, Link2)
    Time_Set(Time3, Link3)
    Time_Set(Time4, Link4)
    Time_Set(Time5, Link5)
    Time_Set(Time6, Link6)
    Time_Set(Time7, Link7)








""" [ Main ] --------------------------------------------------------------------------------------------------- """

# Main Runtime


Folder('\ZOOM SCHEDULER')

Version()

User_New()

State()

Server_Get()

print(exit) 