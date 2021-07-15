class UI_Setting(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):

            MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.offset = None

            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(600, 500)
            MainWindow.setMinimumSize(QtCore.QSize(600, 500))
            MainWindow.setMaximumSize(QtCore.QSize(600, 500))

            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.center()

            self.background = QtWidgets.QLabel(self.centralwidget)
            self.background.setGeometry(QtCore.QRect(0, 0, 600, 500))
            self.background.setText("")
            self.background.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/landscape/Setting.png"))
            self.background.setObjectName("background")

            self.dot = QtWidgets.QLabel(self.centralwidget)
            self.dot.setGeometry(QtCore.QRect(70, 130, 21, 61))
            self.dot.setText("")
            self.dot.setPixmap(QtGui.QPixmap("C:/GitHub/ZOOM-SCHEDULER/UI/resource/elements/•.png"))
            self.dot.setObjectName("dot")

            """close button"""
            self.btn_close = QtWidgets.QPushButton(self.centralwidget)
            self.btn_close.setGeometry(QtCore.QRect(535, 7, 55, 25))
            self.btn_close.setObjectName("btn_close")
            self.btn_close.setStyleSheet(
                '''
                QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/btn.close.png); border:0px;}
                QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/btn.close.active.png); border:0px;}
                '''
            )

            """end"""

            self.btn_info = QtWidgets.QPushButton(self.centralwidget)
            self.btn_info.setGeometry(QtCore.QRect(500, 440, 41, 23))
            self.btn_info.setObjectName("btn_info")
            self.btn_info.setStyleSheet(
                '''
                QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/info.png); border:0px;}
                QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/info.active.png); border:0px;}
                '''
            )

            self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
            self.btn_reset.setGeometry(QtCore.QRect(70, 143, 170, 40))
            self.btn_reset.setObjectName("btn_reset")
            self.btn_reset.setStyleSheet(
                '''
                QPushButton{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/normal/user.reset.png); border:0px;}
                QPushButton:hover{image:url(C:/GitHub/ZOOM-SCHEDULER/UI/resource/button/active/user.reset.active.png); border:0px;}
                '''
            )

            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))