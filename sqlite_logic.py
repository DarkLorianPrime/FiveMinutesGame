import os
import sqlite3
import traceback
import time
try:
    b = 1 / 0
except Exception:
    w = traceback.format_exc()
    print(w)

def connect_logic():
    conn = sqlite3.connect(f'C:/Users/{os.getlogin()}/appdata/Roaming/5min.db')
    conn.execute('CREATE table IF NOT EXISTS settings(difficult text, fps int, update_shop int)')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS HERO(Login str, HP int,  HEAL_COUNT int, MANA int, BALANCE int, MAX_HP int)')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS WEAPON(WEAPON str, WEAPON_ATTACK int, WEAPON_SPEED int, WEAPON_CLASS str, WEAPON_RARITY str)')
    conn.execute('CREATE TABLE IF NOT EXISTS HERO_ACTIVE(Login str)')
    conn.execute('CREATE TABLE IF NOT EXISTS SHOP_ACTIVE(Login str, Product str, enchant str, price int, Product2 str, enchant2 str, price2 int, Product3 str, enchant3 str, price3 int, Product4 str, enchant4 str, price4 int, heals int, time_start int)')
    cur = conn.cursor()
    cur.execute('select * from SETTINGS')
    row = cur.fetchone()
    if row is None:
        cur.execute('insert into SETTINGS values(?,?,?)', ('peaceful', 30, int(time.time())))
    conn.commit()
    cur.execute('select * from SETTINGS')
    row = cur.fetchone()
    cur.execute('update SETTINGS set update_shop = ? where update_shop = ?', (int(time.time() - 15), row[2]))
    cur.execute('delete from HERO_ACTIVE')
    cur.execute('delete from SHOP_ACTIVE')
    conn.commit()


def connection():
    conn = sqlite3.connect(f'C:/Users/{os.getlogin()}/appdata/roaming/5min.db')
    cur = conn.cursor()
    print('Открываю базу')
    return conn, cur


def close_connection():
    conn, cur = connection()
    print('Закрываю базу')
    conn.commit()
    conn.close()


def give_login():
    conn, cur = connection()
    cur.execute('select * from HERO_ACTIVE')
    row_all = cur.fetchone()
    cur.execute('select * from HERO where login is ?', (row_all[0],))
    row = cur.fetchone()
    close_connection()
    return row


def give_weapon():
    conn, cur = connection()
    cur.execute('select * from Weapon')
    row = cur.fetchone()
    close_connection()
    return row


def log_access(d, start):
    with open(f'{os.getcwd()}/BattleLog.log', 'a') as g:
        with open(f'{os.getcwd()}/AccessBattleLog.log', 'a') as s:
            g.write(f'[00:00:0{int(time.time() - start)}]{str(d)}\n')
            g.close()
            s.write(f'[00:00:0{int(time.time() - start)}]{str(d)}\n')
            s.close()
