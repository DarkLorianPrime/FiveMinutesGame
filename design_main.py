from PyQt5 import QtCore
from PyQt5.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QPushButton, QLabel, QFrame, QWidget, QTextBrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        self.heal_button = QPushButton(self.centralwidget)
        self.font = QFont()
        self.shop_open = QPushButton(self.centralwidget)
        self.battle_join = QPushButton(self.centralwidget)
        self.frame = QFrame(self.centralwidget)
        self.label = QLabel(self.frame)
        self.label_2 = QLabel(self.frame)
        self.label_3 = QLabel(self.frame)
        self.label_4 = QLabel(self.frame)
        self.label_5 = QLabel(self.frame)
        self.label_6 = QLabel(self.frame)
        self.label_7 = QLabel(self.centralwidget)
        self.exit_login = QPushButton(self.centralwidget)
        self.exit_windows = QPushButton(self.centralwidget)
        self.frame_2 = QFrame(self.centralwidget)
        self.label_17 = QLabel(self.centralwidget)
        self.label_16 = QLabel(self.centralwidget)
        self.font2 = QFont()
        self.label_8 = QLabel(self.centralwidget)
        self.line = QFrame(self.frame_2)
        self.label_15 = QLabel(self.frame_2)
        self.label_14 = QLabel(self.frame_2)
        self.label_9 = QLabel(self.frame_2)
        self.label_10 = QLabel(self.frame_2)
        self.font1 = QFont()
        self.label_11 = QLabel(self.frame_2)
        self.label_12 = QLabel(self.frame_2)
        self.label_13 = QLabel(self.frame_2)
        self.scale_size(MainWindow)

    def scale_size(self, MainWindow):
        self.font1.setPointSize(12)
        self.label_10.setFont(self.font1)
        self.label_14.setGeometry(QRect(30, 140, 141, 16))
        self.label_14.setFont(self.font)
        self.font1.setPointSize(12)
        self.label_10.setFont(self.font1)
        self.label_8.setGeometry(QRect(370, 10, 571, 61))
        self.label_16.setGeometry(QRect(70, 100, 61, 16))
        self.label_17.setGeometry(QRect(10, 100, 47, 13))
        self.font2.setPointSize(20)
        self.label_8.setFont(self.font2)
        self.line.setGeometry(QRect(20, 155, 381, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_15.setGeometry(QRect(170, 136, 151, 20))
        self.label_15.setFont(self.font1)
        MainWindow.resize(1280, 768)
        MainWindow.setMinimumSize(QSize(1280, 768))
        MainWindow.setMaximumSize(QSize(1280, 768))
        self.heal_button.setObjectName(u"heal")
        self.heal_button.setGeometry(QRect(20, 630, 111, 111))
        self.font.setPointSize(14)
        self.heal_button.setFont(self.font)
        self.shop_open.setObjectName(u"shop")
        self.shop_open.setGeometry(QRect(210, 630, 271, 111))
        self.shop_open.setFont(self.font)
        self.battle_join.setObjectName(u"battle")
        self.battle_join.setGeometry(QRect(560, 630, 271, 111))
        self.battle_join.setFont(self.font)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, -20, 371, 101))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(10)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 91, 16))
        self.label.setFont(self.font)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 30, 131, 16))
        self.label_2.setFont(self.font)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 30, 81, 16))
        self.label_3.setFont(self.font)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 52, 91, 21))
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 45, 101, 31))
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 52, 71, 21))
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(480, 340, 47, 13))
        self.exit_login.setObjectName(u"exit_login")
        self.exit_login.setGeometry(QRect(1084, 10, 181, 71))
        self.exit_windows.setObjectName(u"exit_windows")
        self.exit_windows.setGeometry(QRect(1080, 90, 191, 91))
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(900, 300, 481, 221))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(3)
        self.frame_2.setMidLineWidth(10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 40, 141, 41))
        self.label_9.setFont(self.font)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 50, 211, 21))
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 90, 47, 13))
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 92, 191, 21))
        self.label_12.setFont(self.font)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 90, 91, 21))
        self.label_13.setFont(self.font1)
        self.label_14.setObjectName(u"label_14")
        self.label_15.setObjectName(u"label_15")
        self.line.setObjectName(u"line")
        self.label_8.setObjectName(u"label_8")
        self.label_16.setObjectName(u"label_16")
        self.label_17.setObjectName(u"label_17")
        self.label_7.resize(500, 500)
        self.label_7.move(300, 50)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.heal_button.setText(QCoreApplication.translate("MainWindow", u"HEAL", None))
        self.shop_open.setText(QCoreApplication.translate("MainWindow", u"SHOP", None))
        self.battle_join.setText(QCoreApplication.translate("MainWindow", u"BATTLE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HEALTH", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HEAL_COUNT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MANA", None))
        self.exit_login.setText(QCoreApplication.translate("MainWindow", u"EXIT TO LOGIN", None))
        self.exit_windows.setText(QCoreApplication.translate("MainWindow", u"EXIT TO WINDOWS", None))
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"\u0422\u0412\u041e\u0415 \u041e\u0420\u0423\u0416\u0418\u0415",
                                       None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"{weapon}", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041a\u0410\u0427\u0415\u0421\u0422\u0412\u041e \u041e\u0420\u0423\u0416\u0418\u042f",
                                                         None))
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0420\u041e\u041d \u041e\u0420\u0423\u0416\u0418\u042f",
                                       None))
        self.label_17.resize(24, 24)
    # retranslateUi


class Ui_MainWindow_logs(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 10, 481, 411))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 430, 231, 61))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_logs(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi_logs(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                                                            "></p></body></html>",
                                                            None))
        self.textBrowser.setText('ПРИВЕТ ЛОХИ!')
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi
