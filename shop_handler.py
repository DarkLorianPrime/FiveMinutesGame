import os
import random
import time

import Weapon_handler
import sqlite3

conn = sqlite3.connect(f'C:/Users/{os.getlogin()}/appdata/Roaming/5min.db')
cur = conn.cursor()
cur.execute('select * from SETTINGS')
row = cur.fetchone()

try:
    cur.execute('select * from SETTINGS')
    rows = cur.fetchone()
    list_for_sale = []
    i = 0
    new_time = time.time()
    print(int(new_time) - int(rows[2]))
    if int(new_time) - int(rows[2]) > 15:
        print(1)
        cur.execute('update SETTINGS set update_shop = ? where update_shop = ?', (int(time.time()), rows[2]))
        conn.commit()
        print(1)
        l = list(range(1, len(Weapon_handler.data['weapon']['swords'])))
        random.shuffle(l)
        list_for_sale.clear()
        list_for_sale.append(Weapon_handler.data['weapon']['swords'][l[i]])
        print('Ассортимент был обновлен! Чтобы увидеть его, еще раз напишите shop')
    else:
        print(1)
except Exception as ex:
    print(ex)
