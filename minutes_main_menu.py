import os
import random
import sys
import time
from PyQt5.QtGui import QPixmap
import design_main
from PyQt5 import QtWidgets, QtCore
import minutes_start_menu
import main_logic
import sqlite_logic
import class_logic_shop


class main_table(QtWidgets.QMainWindow, design_main.Ui_MainWindow, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super(main_table, self).__init__()
        self.setupUi(self)
        self.render_menu()

    def render_menu(self):
        pixhero, pixcoin = QPixmap(f'{os.getcwd()}/icon.png'), QPixmap(f'{os.getcwd()}/coin.png')
        conn, cur = sqlite_logic.connection()
        HERO_ROW = sqlite_logic.give_login()
        cur.execute('select * from WEAPON')
        WEAPON_ROW = cur.fetchone()
        self.shop_open.setEnabled(True)
        self.heal_button.clicked.connect(lambda: self.heal())
        self.shop_open.clicked.connect(lambda: self.to_shop())
        self.battle_join.clicked.connect(lambda: self.battle())
        self.exit_login.clicked.connect(lambda: self.killed())
        self.exit_windows.clicked.connect(lambda: self.killed_to_windows())
        self.label_7.setPixmap(pixhero)
        self.label_17.setPixmap(pixcoin)
        self.label_4.setText(str(HERO_ROW[1]))
        self.label_5.setText(str(HERO_ROW[2]))
        self.label_6.setText(str(HERO_ROW[3]))
        self.label_8.setText(str(HERO_ROW[0]))
        self.label_10.setText(str(WEAPON_ROW[0]))
        self.label_13.setText(str(WEAPON_ROW[4]))
        self.label_15.setText(str(WEAPON_ROW[1]))
        self.label_16.setText(f'{HERO_ROW[4]} EUTS')
        self.setVisible(True)
        sqlite_logic.close_connection()

    def to_shop(self):
        self.setVisible(False)
        windows_render().to_shop()

    def killed(self):
        conn, cur = sqlite_logic.connection()
        windows_render().back_to_login()
        cur.execute('delete from HERO_ACTIVE')
        conn.commit()
        self.destroy()
        sqlite_logic.close_connection()

    def killed_to_windows(self):
        conn, cur = sqlite_logic.connection()
        cur.execute('delete from HERO_ACTIVE')
        conn.commit()
        sys.exit()

    def heal(self):
        main_logic.Main_logic_min().Heal()
        HERO_ROW = sqlite_logic.give_login()
        self.label_5.setText(str(HERO_ROW[2]))
        self.label_4.setText(str(HERO_ROW[1]))

    def battle(self):
        if os.path.isfile(f'{os.getcwd()}\\AccessBattleLog.log'):
            os.remove(f'{os.getcwd()}\\AccessBattleLog.log')
        conn, cur = sqlite_logic.connection()
        if sqlite_logic.give_login()[3] == 100:
            cur.execute('UPDATE HERO set mana = 0 where Login is ?', (sqlite_logic.give_login()[0],))
            conn.commit()
            sqlite_logic.close_connection()
            main_logic.Main_logic_min().Battle(100)
        else:
            main_logic.Main_logic_min().Battle(0)
        HERO_ROW = sqlite_logic.give_login()
        self.label_4.setText(str(HERO_ROW[1]))
        self.label_5.setText(str(HERO_ROW[2]))
        self.label_6.setText(str(HERO_ROW[3]))
        self.label_8.setText(str(HERO_ROW[0]))
        self.label_16.setText(f'{HERO_ROW[4]} EUTS')
        windows_render().render_logs_windows()


class main_logs(QtWidgets.QMainWindow, design_main.Ui_MainWindow_logs, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super(main_logs, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.destroy())
        self.textBrowser.setText(open(f'{os.getcwd()}/AccessBattleLog.log', 'r').read())

    def event(self, event):
        if event.type() == QtCore.QEvent.WindowDeactivate or event.type() == QtCore.QEvent.Close:
            self.destroy()
        return QtWidgets.QWidget.event(self, event)


class windows_render:
    windows = [main_table, minutes_start_menu.main_auth, main_logs, class_logic_shop.logic_shop]

    def render_main_windows(self):
        self.windows[0]().show()

    def render_logs_windows(self):
        self.windows[2]().show()

    def back_to_login(self):
        self.windows[1]().show()

    def to_shop(self):
        self.windows[3]().show()


if __name__ == '__main__':
    windows_render().render_main_windows()
