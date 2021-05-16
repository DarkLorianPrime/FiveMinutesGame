from PyQt5 import QtCore
from PyQt5.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QFrame, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QSize(500, 500))
        Form.setMaximumSize(QSize(500, 500))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 210, 211, 81))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(344, 422, 121, 51))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 422, 121, 51))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 60, 281, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 300, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(164, 422, 161, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(
            QCoreApplication.translate("Form", u"\u041d\u0410\u0427\u0410\u0422\u042c \u0418\u0413\u0420\u0423", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"RESTART", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"CHEAT MODE", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"INSERT YOUR NICKNAME", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Settings", None))


class Ui_Dialog_reset(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 0, 400, 91))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 80, 461, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 140, 350, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 390, 111, 91))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(380, 390, 111, 91))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(240, 170, 21, 301))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 380, 501, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_reset(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi_reset(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0412\u0432\u0435\u0434\u0438 \u0441\u044e\u0434\u0430 \u0441\u0432\u043e\u0439 \u043d\u0438\u043a",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0422\u044b \u0443\u0432\u0435\u0440\u0435\u043d \u0447\u0442\u043e \u0445\u043e\u0447\u0435\u0448\u044c \u0441\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u043c \u043d\u0438\u043a\u0435?",
                                                        None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"NO", None))

    # retranslateUi


class Ui_Dialog_Settings(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 80, 261, 51))
        font = QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 200, 41))
        font1 = QFont()
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 90, 171, 31))
        self.label_3.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 440, 411, 91))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 130, 501, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 150, 261, 51))
        self.pushButton_2.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 160, 111, 31))
        self.label_4.setFont(font)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 200, 501, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 420, 441, 31))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(100, 360, 271, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_sett(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi_sett(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Difficult shift", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u0440\u043e\u0435\u043a\u0442 \u0431\u044b\u043b \u0440\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d DarkLorian.",
                                                        None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"FPS Counter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0418 \u0411\u0423\u0414\u0423\u0422 \u041f\u0420\u0418\u041c\u0415\u041d\u0415\u041d\u042b \u041f\u041e\u0421\u041b\u0415 \u0412\u042b\u0425\u041e\u0414\u0410 \u0418\u0417 \u042d\u0422\u041e\u0413\u041e \u041c\u0415\u041d\u042e",
                                                        None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi


class Ui_Dialog_Cheat(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 161, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 40, 401, 28))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-13, 70, 551, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 90, 121, 16))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(102, 110, 291, 28))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-13, 140, 551, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 160, 121, 16))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(130, 180, 231, 28))
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-23, 210, 591, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 397, 251, 51))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 320, 431, 20))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 290, 411, 80))
        self.frame.setMouseTracking(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_cheat(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi_cheat(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0411\u0415\u0421\u041a\u041e\u041d\u0415\u0427\u041d\u042b\u0415 \u0425\u0418\u041b\u041a\u0418",
                                                      None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GIVE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041c\u041d\u041e\u0413\u041e \u0416\u0418\u0417\u041d\u0415\u0419",
                                                        None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"GIVE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041c\u041d\u041e\u0413\u041e \u0414\u0415\u041d\u0415\u0413",
                                                        None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"GIVE", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u042b\u041a\u041b\u042e\u0427\u0415\u041d\u0418\u0415 \u0427\u0418\u0422\u041e\u0412 \u0412\u041e\u0417\u041c\u041e\u0416\u041d\u041e \u0422\u041e\u041b\u042c\u041a\u041e \u041f\u0420\u0418 \u041f\u041e\u041b\u041d\u041e\u041c \u0420\u0415\u0421\u0415\u0422\u0415",
                                                        None))
    # retranslateUi
