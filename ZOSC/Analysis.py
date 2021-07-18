# -*- conding: utf-8 -*-

import os
import wmi
import time
from datetime import datetime
from datetime import timedelta
from win32com.client import GetObject
import PyQt5    # PyQt5 / PyQt5-tools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class Analysis(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    def NowTime(self):
        now = time.localtime()
        today = ("%04d.%02d.%02d" % (now.tm_year, now.tm_mon, now.tm_mday))
        return today

    def Analysis_Class(self):
        Analysis_Result = "C:\\ZOOM SCHEDULER\\Analysis\\Analysis Result.txt"

        def RunTime():
            Time = 0
            Process_List = []
            while Time != 50:
                WMI = GetObject('winmgmts:')
                Processes = WMI.InstancesOf('Win32_Process')

                for Process in Processes:
                    Process_List.append(Process.Properties_('Name').Value)
                print(Process_List)
                time.sleep(5)
                break
                


        if os.path.isfile(Analysis_Result):
            RunTime()

        else:
            New = open(Analysis_Result, 'w')
            New.close()
            RunTime()