# -*- conding: utf-8 -*-

import os
import time
import urllib.request
from win10toast import ToastNotifier    # win10toast



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

