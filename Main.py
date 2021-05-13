""" Qt UI 임포트 """
from PyQt4.QtGui import

""" FTP 라이브러리 """
import ftplib

""" 파이썬 OS """
import os

""" FTP 링크 파일 다운 """
import urllib




url = 'http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/INF/CHECK_INF.txt'

urllib.urlretrieve(url, "CHECK_INF.txt")


data=CHECK.read()
