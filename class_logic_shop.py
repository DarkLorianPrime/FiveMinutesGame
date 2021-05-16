import os
import sqlite3
import sys
import random
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import shop_design
import minutes_main_menu
import Weapon_handler
import sqlite_logic


class logic_shop(QtWidgets.QMainWindow, shop_design.Ui_MainWindow, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super(logic_shop, self).__init__()
        self.setupUi(self)
        self.Exit_but.clicked.connect(lambda: self.exit_main())
        self.Buy_Heal.clicked.connect(lambda: self.exit_main())
        self.Buy_1slot.clicked.connect(lambda: self.func_buy_weapon(1))
        self.Buy_2slot.clicked.connect(lambda: self.func_buy_weapon(2))
        self.Buy_3slot.clicked.connect(lambda: self.func_buy_weapon(3))
        self.Buy_4slot.clicked.connect(lambda: self.func_buy_weapon(4))
        conn, cur, row = self.sqlite_connect_weapon()
        if row is None:
            price_list = self.update_sqlite()
            cur.execute('insert into SHOP_ACTIVE values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', price_list)
            conn.commit()
            time_update = 300
        else:
            if int(time.time()) - int(row[14]) >= 300:
                price_list = self.update_sqlite()
                cur.execute('insert into SHOP_ACTIVE values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', price_list)
                conn.commit()
                cur.execute('select * from SHOP_ACTIVE')
                all = cur.fetchall()
                print(all)
            time_update = 300 - (int(time.time()) - int(row[14]))
        self.render_shop(time_update)

    def render_shop(self, time_update):
        conn, cur, row = self.sqlite_connect_weapon()
        self.label_2.setText(row[1])
        self.label_9.setText(row[4])
        self.label_10.setText(row[7])
        self.label_11.setText(row[10])
        for i in Weapon_handler.data['weapon']['swords']:
            if i['name'] == row[10]:
                self.label_12.setText(f"{i['damage']} ATK")
                self.label_16.setText(f"{i['speed']} SPD")
                self.label_20.setText(row[11])
                self.label_24.setText(i['element'])
                self.label_35.setText(f"{row[12]} EUTS")
            if i['name'] == row[7]:
                self.label_13.setText(f"{i['damage']} ATK")
                self.label_17.setText(f"{i['speed']} SPD")
                self.label_21.setText(row[8])
                self.label_25.setText(i['element'])
                self.label_36.setText(f"{row[9]} EUTS")
            if i['name'] == row[4]:
                self.label_14.setText(f"{i['damage']} ATK")
                self.label_18.setText(f"{i['speed']} SPD")
                self.label_22.setText(row[5])
                self.label_26.setText(i['element'])
                self.label_37.setText(f"{row[6]} EUTS")
            if i['name'] == row[1]:
                self.label_15.setText(f"{i['damage']} ATK")
                self.label_19.setText(f"{i['speed']} SPD")
                self.label_23.setText(row[2])
                self.label_27.setText(i['element'])
                self.label_38.setText(f"{row[3]} EUTS")
        self.label_28.setText('NO INFORMATION')
        self.label_29.setText('NO INFORMATION')
        self.label_30.setText('NO INFROMATION')
        self.label_31.setText('NO INFORMATION')
        self.label_33.setText(str(row[13]))
        self.Timer.setText(f'{time_update} SEC')
        self.sqlite_close_weapon()

    def exit_main(self):
        self.destroy()
        print('Выполняю выход')
        minutes_main_menu.main_table().shop_open.setEnabled(True)

    def sqlite_connect_weapon(self):
        conn = sqlite3.connect(f'C:/Users/{os.getlogin()}/appdata/Roaming/5min.db', timeout=1)
        cur = conn.cursor()
        cur.execute('SELECT * FROM SHOP_ACTIVE')
        row = cur.fetchone()
        return conn, cur, row

    def func_buy_weapon(self, slot):
        conn, cur, row = self.sqlite_connect_weapon()
        print(sqlite_logic.give_login()[4])
        weapon_dict = {}
        print(row)
        if slot == 1:
            weapon_dict['name'] = row[1]
            weapon_dict['enchant'] = row[2]
            weapon_dict['cost'] = row[3]
        elif slot == 2:
            weapon_dict['name'] = row[4]
            weapon_dict['enchant'] = row[5]
            weapon_dict['cost'] = row[6]
        elif slot == 3:
            weapon_dict['name'] = row[7]
            weapon_dict['enchant'] = row[8]
            weapon_dict['cost'] = row[9]
        elif slot == 4:
            weapon_dict['name'] = row[10]
            weapon_dict['enchant'] = row[11]
            weapon_dict['cost'] = row[12]
        if sqlite_logic.give_login()[4] - weapon_dict['cost'] >= 0:
            conn = sqlite3.connect(f'C:/Users/{os.getlogin()}/appdata/Roaming/5min.db', timeout=1)
            cur = conn.cursor()
            print(sqlite_logic.give_weapon())
            for i in Weapon_handler.data['weapon']['swords']:
                if i['name'] == weapon_dict['name']:
                    cur.execute('update WEAPON set WEAPON = ?, WEAPON_ATTACK = ?, WEAPON_SPEED = ?, WEAPON_RARITY = ?', (weapon_dict['name'], i['damage'], i['speed'], weapon_dict['enchant']))
                    cur.execute('update HERO set BALANCE = ? where Login = ?', (sqlite_logic.give_login()[4] - weapon_dict['cost'], sqlite_logic.give_login()[0],))
                    conn.commit()
                    QMessageBox.information(self, 'Покупка успешна!', f'Спасибо за покупку. Твой счет: {sqlite_logic.give_login()[4] - weapon_dict["cost"]}')
                    minutes_main_menu.main_table().shop_open.setEnabled(True)
        else:
            QMessageBox.warning(self, 'Нет денег.',
                                f'Покупка отменена. Недостаточно денег на аккаунте.\nТвой счет: {sqlite_logic.give_login()[4]}')

        print(weapon_dict)

    def sqlite_close_weapon(self):
        conn, cur, row = self.sqlite_connect_weapon()
        conn.commit()
        cur.close()
        conn.close()

    def update_sqlite(self):
        conn, cur, row = self.sqlite_connect_weapon()
        cur.execute('DELETE FROM SHOP_ACTIVE')
        conn.commit()
        login = sqlite_logic.give_login()[0]
        self.sqlite_close_weapon()
        sqlite_logic.close_connection()
        first_weapon, second_weapon, three_weapon, fourble_weapon = Weapon_handler.data['weapon']['swords'][
                                                                        self.get_int(0)], \
                                                                    Weapon_handler.data['weapon']['swords'][
                                                                        self.get_int(0)], \
                                                                    Weapon_handler.data['weapon']['swords'][
                                                                        self.get_int(0)], \
                                                                    Weapon_handler.data['weapon']['swords'][
                                                                        self.get_int(0)]
        first_enchant, second_enchant, three_enchant, fourble_enchant = Weapon_handler.data['enchant'][
                                                                            self.get_int(1)], \
                                                                        Weapon_handler.data['enchant'][
                                                                            self.get_int(1)], \
                                                                        Weapon_handler.data['enchant'][
                                                                            self.get_int(1)], \
                                                                        Weapon_handler.data['enchant'][
                                                                            self.get_int(1)]
        first_price, second_price, three_price, fourble_price = random.randint(7, 77) * first_enchant[
            0], random.randint(7, 77) * second_enchant[0], random.randint(7, 77) * three_enchant[0], random.randint(
            7, 77) * fourble_enchant[0]
        if first_enchant[2] == 'Mythic':
            first_price = int(first_price) * 11
        if second_enchant[2] == 'Mythic':
            second_price = int(second_price) * 11
        if second_enchant[2] == 'Mythic':
            three_price = int(three_price) * 11
        if second_enchant[2] == 'Mythic':
            fourble_price = int(fourble_price) * 11
        heals = random.randint(0, 20)
        time_start = time.time()
        price_list = (
            login, first_weapon['name'], first_enchant[2], first_price, second_weapon['name'], second_enchant[2],
            second_price, three_weapon['name'], three_enchant[2], three_price, fourble_weapon['name'],
            fourble_enchant[2], fourble_price, heals, time_start)
        return price_list

    def get_int(self, query):
        if query == 0:
            return random.randint(0, 16)
        if query == 1:
            integ = random.randint(0, 30) + random.randint(0, 30)
            if 1 <= integ <= 20:
                return 'simple'
            if 20 < integ <= 35:
                return 'rare'
            if 35 < integ <= 45:
                return 'epic'
            if 45 < integ <= 55:
                return 'legendary'
            if 55 < integ <= 60:
                return 'mythic'


class windows_render:
    def __init__(self):
        self.windows = [logic_shop]

    def render_main_windows(self):
        app = QtWidgets.QApplication(sys.argv)
        self.windows[0]().show()
        app.exec_()


if __name__ == '__main__':
    windows_render().render_main_windows()
