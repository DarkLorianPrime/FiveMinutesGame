import os
import sqlite3
import sys
import sqlite_logic
import hero_handler
import design_auth
import minutes_main_menu
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

conn = sqlite3.connect(f'C:/Users/{os.getlogin()}/appdata/Roaming/5min.db')
cur = conn.cursor()
sqlite_logic.connect_logic()


class main_auth(QtWidgets.QMainWindow, design_auth.Ui_Form, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super(main_auth, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.input_nick_and_start_game())
        self.pushButton_2.clicked.connect(lambda: windows_render().render_restart_windows())
        self.pushButton_2.clicked.connect(lambda: self.killed())
        self.pushButton_3.clicked.connect(lambda: windows_render().render_cheat_windows())
        self.pushButton_3.clicked.connect(lambda: self.killed())
        self.pushButton_4.clicked.connect(lambda: windows_render().render_setting_windows())
        self.pushButton_4.clicked.connect(lambda: self.killed())

    def closeEvent(self, event):
        request = QMessageBox.question(self, 'Ты уверен что хочешь выйти?', 'Ты уходишь?(', QMessageBox.Yes,
                                       QMessageBox.No)
        if request == QMessageBox.Yes:
            sys.exit()
        else:
            event.ignore()

    def input_nick_and_start_game(self):
        try:
            textbox = self.lineEdit.text()
            if textbox == '':
                self.lineEdit.setText("ВВЕДИ NICK")
            else:
                if textbox != 'ВВЕДИ NICK':
                    hero_handler.login(textbox)
                    self.killed()
                    print(textbox)
                    cur.execute('insert into HERO_ACTIVE values(?)', (textbox,))
                    conn.commit()
                    minutes_main_menu.windows_render().render_main_windows()
        except Exception as ex:
            print(ex)

    def killed(self):
        self.destroy()


class reset(QtWidgets.QMainWindow, design_auth.Ui_Dialog_reset, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.restart())
        self.pushButton_2.clicked.connect(lambda: self.exit())

    def restart(self):
        textbox = self.lineEdit.text()
        if textbox == '':
            self.lineEdit.setText("ВВЕДИ NICK")
        else:
            if textbox != 'ВВЕДИ NICK':
                cur.execute('select * from HERO where login is ?', (textbox,))
                row = cur.fetchone()
                if row is None:
                    self.lineEdit.setText("Ник не найден")
                else:
                    cur.execute('delete from HERO where login is ?', (textbox,))
                    cur.execute('insert into HERO values(?,?,?,?,?)', (textbox, 100, 1, 0, 0))
                    conn.commit()

    def exit(self):
        self.close()
        main_auth().show()


class settings(QtWidgets.QMainWindow, design_auth.Ui_Dialog_Settings, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super(settings, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.set_difficult())
        self.pushButton_2.clicked.connect(lambda: self.set_fps())
        self.pushButton_3.clicked.connect(lambda: self.exit())
        cur.execute('select * from SETTINGS')
        self.row_sett = cur.fetchone()
        self.label_3.setText(self.row_sett[0])
        self.label_4.setText(str(self.row_sett[1]))

    def set_difficult(self):
        cur.execute('select * from SETTINGS')
        row_sett = cur.fetchone()
        if row_sett[0] == 'peaceful':
            list_upd = 'NORMAL', 'peaceful'
        else:
            list_upd = 'peaceful', 'NORMAL'
        cur.execute('update SETTINGS set difficult = ? where difficult = ?', list_upd)
        conn.commit()
        cur.execute('select * from SETTINGS')
        row_sett = cur.fetchone()
        self.label_3.setText(row_sett[0])
        self.update()

    def set_fps(self):
        # NOT WORKING #
        cur.execute('select * from SETTINGS')
        row_sett = cur.fetchone()
        if row_sett[1] == 30:
            list_upd = 60, 30
        else:
            list_upd = 30, 60
        cur.execute('update SETTINGS set fps = ? where fps = ?', list_upd)
        cur.execute('select * from SETTINGS')
        row_sett = cur.fetchone()
        self.label_4.setText(str(row_sett[1]))
        conn.commit()
        self.update()

    def exit(self):
        try:
            self.close()
            main_auth().show()
        except Exception as ex:
            print(ex)


class cheat(QtWidgets.QMainWindow, design_auth.Ui_Dialog_Cheat, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super(cheat, self).__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(lambda: self.exit())

    def exit(self):
        self.close()
        main_auth().show()


class windows_render:
    def __init__(self):
        self.windows = [main_auth, reset, settings, cheat]

    def render_main_windows(self):
        app = QtWidgets.QApplication(sys.argv)
        self.windows[0]().show()
        app.exec_()

    def render_restart_windows(self):
        self.windows[1]().show()

    def render_setting_windows(self):
        self.windows[2]().show()

    def render_cheat_windows(self):
        self.windows[3]().show()


if __name__ == '__main__':
    windows_render().render_main_windows()
