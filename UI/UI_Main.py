
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ZOOM SCHEDULER")
        MainWindow.resize(1100, 650)
        MainWindow.setMaximumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 30, 1100, 620))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/background/Main.png"))
        self.background.setObjectName("background")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-10, 0, 1114, 41))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap(":/title/ZOSC.png"))
        self.title.setObjectName("title")
        self.btn_run = QtWidgets.QLabel(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(860, 570, 141, 61))
        self.btn_run.setText("")
        self.btn_run.setPixmap(QtGui.QPixmap(":/btn/btn.run.png"))
        self.btn_run.setObjectName("btn_run")
        self.btn_notice = QtWidgets.QLabel(self.centralwidget)
        self.btn_notice.setGeometry(QtCore.QRect(20, 80, 101, 71))
        self.btn_notice.setText("")
        self.btn_notice.setPixmap(QtGui.QPixmap(":/btn/notice.refresh.png"))
        self.btn_notice.setObjectName("btn_notice")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ZOOM SCHEDULER", "ZOOM SCHEDULER"))
#  import zosc.resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())