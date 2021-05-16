import sqlite3
import os
import Weapon_handler

conn = sqlite3.connect(f'C:/Users/{os.getlogin()}/appdata/roaming/5min.db')
cur = conn.cursor()


def login(login):
    cur.execute('select * from HERO where Login is ?', (login,))
    row = cur.fetchone()
    if row is None:
        print(1)
        sword = Weapon_handler.data['weapon']['swords'][12]
        sword_rarity = Weapon_handler.data['enchant']['simple'][2]
        cur.execute('insert into HERO values(?,?,?,?,?,?)', (login, 100, 100, 0, 0, 100))
        cur.execute('insert into WEAPON values(?,?,?,?,?)',
                    (sword['name'], int(sword['damage']), int(sword['speed']), sword['element'], sword_rarity))
        conn.commit()
