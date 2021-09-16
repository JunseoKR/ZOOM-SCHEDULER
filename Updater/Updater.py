# -*- conding: utf-8 -*-

import os
import sys
import time
import urllib.request
from win10toast import ToastNotifier    # win10toast
from win10toast_click import ToastNotifier    # win10toast-click





def FTP_StatusCheck():    # FTP 서버 상태 확인
    Checkurl = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Check/Status.txt"
    CheckPath = "C:\\ZOOM SCHEDULER\\FTP Status.txt"
    urllib.request.urlretrieve(Checkurl, CheckPath)
    Checktxt = open(CheckPath, 'r')
    Check = Checktxt.read()
    Checktxt.close()
    os.remove(CheckPath)

    def Support():
        SupportChat = "https://open.kakao.com/o/s2HyPjpc"
        webbrowser.open(SupportChat)


    def Warn():
        toaster = ToastNotifier()
        toaster.show_toast("ZOSC 데이터 서버 오류", "여기을 누르시면 지원 채팅으로 이동합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Support.ico", duration=7, threaded=True, callback_on_click=Support)

    if Check == "Running":
        return
    else:
        Warn()
        time.sleep(8)
        sys.exit()


FTP_StatusCheck()


toaster = ToastNotifier()
toaster.show_toast("ZOSC 업데이트", "ZOOM SCHEDULER 업데이트를 시작합니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Updater.ico", duration=3, threaded=True)

os.system('taskkill /f /im ZOOM SCHEDULER.exe')

FTP_version = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Version/Version.txt"    # Version Check 파일 경로 ( FTP 서버 )
FTP_verPath = "C:\\ZOOM SCHEDULER\\Update_Temp.txt"    # Version.txt 저장 경로
# 서버 요청
urllib.request.urlretrieve(FTP_version, FTP_verPath)
# 파일 읽기
FTPread = open(FTP_verPath, 'r')
UpdateVer = FTPread.read()
FTPread.close()
# 파일 제거
os.remove(FTP_verPath)
ZOSC_Path = "C:\\ZOOM SCHEDULER\\ZOOM SCHEDULER.exe"
ZOSC_New = "http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/Update/ZOSC.exe"
try:
    os.remove(ZOSC_Path)
    time.sleep(2)

except FileNotFoundError:
    pass

urllib.request.urlretrieve(ZOSC_New, ZOSC_Path)

complete = ToastNotifier()
complete.show_toast("ZOSC 업데이트", "ZOOM SCHEDULER 업데이트가 완료되었습니다.", icon_path="C:\\GitHub\\ZOOM-SCHEDULER\\UI\\resource\\Updater.ico", duration=3, threaded=True)
time.sleep(1)
os.system("start "+ZOSC_Path)