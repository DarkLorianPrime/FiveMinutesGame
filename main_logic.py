import sys
import time
from PyQt5.QtWidgets import QMessageBox
import sqlite_logic
import minutes_main_menu
import random
import Weapon_handler


class Main_logic_min:
    def Heal(self):
        row = sqlite_logic.give_login()
        if row[2] > 0:
            if row[1] != row[5]:
                health = row[5] - row[1]
                if health <= 25:
                    health = health + row[1]
                else:
                    health = row[1] + 25
                conn, cur = sqlite_logic.connection()
                cur.execute('update HERO set HEAL_COUNT = ?, HP = ? where Login = ?', (int(row[2] - 1), health, row[0]))
                conn.commit()
                sqlite_logic.close_connection()

    def Battle(self, Mana):
        try:
            start = time.time()
            sqlite_logic.log_access(f'=====================', start)
            battle_type = random.randint(1, 20)
            if Mana == 100:
                sqlite_logic.log_access('Событие: Использование магии на ДОБАВЬ ЧТО НИБУДЬ', start)
                sqlite_logic.log_access(f'Вместе с использованием ты сжег все выпавшие монеты. Смирись.', start)
                sqlite_logic.log_access(f'=====================', start)
                return
            if battle_type == 1:
                """
                Потеря склянок
                """
                nick = sqlite_logic.give_login()
                if nick[2] > 1:
                    conn, cur = sqlite_logic.connection()
                    cur.execute('update HERO set HEAL_COUNT = ? where login = ?', (nick[2] - 2, nick[0]))
                    conn.commit()
                    sqlite_logic.close_connection()
                work, bb = 2, 1
                sqlite_logic.log_access('Событие: Нападение разбойников.', start)
            elif battle_type == 5:
                """
                Сильный босс
                """
                work, bb = 4, 5
                sqlite_logic.log_access('Событие: Попадание в логово рейдового босса.', start)
            elif battle_type == 10:
                """
                прибыльный ивент
                """
                row = sqlite_logic.give_login()
                Balance_minus = random.randint(1, 150)
                self.update_balance(row[0], (row[4] + Balance_minus))
                sqlite_logic.log_access('Событие: Попадание в логово выживающих.\n'
                                        f'Ты заработал {Balance_minus} EUTS. Жители ненавидят тебя.\n'
                                        '=====================', start)
                return
            elif battle_type == 15:
                """
                Тебя развели на деньги
                """
                row = sqlite_logic.give_login()
                BALANCE = row[4] - random.randint(1, 150)
                self.update_balance(row[0], BALANCE)
                work, bb = 3, 2
                sqlite_logic.log_access(
                    f'Событие: Раздача денег беженцам с соседней деревни.\nТы отдал {BALANCE}. Жители благодарят тебя.',
                    start)
            elif battle_type == 20:
                """
                договорился с монстром
                """
                sqlite_logic.log_access('Событие: Тебе попался разумный монстр, у которого сегодня выходной. Повезло.\n'
                                        '=====================', start)
                return
            else:
                """
                Обычный бой
                """
                sqlite_logic.log_access(f'Событие: На тебя напал ДОБАВЬ СЮДА ЧЕ НИБУДЬ', start)
                work, bb = 1, 1
            self.while_battle(work=work, bb=bb, start_time=start)
        except Exception as ex:
            print(ex)

    def update_balance(self, login, balance):
        conn, cur = sqlite_logic.connection()
        cur.execute('update HERO set balance = ? where login = ?', (balance, login))
        conn.commit()
        sqlite_logic.close_connection()

    def while_battle(self, work, start_time, bb=1):
        conn, cur = sqlite_logic.connection()
        weapon, nick = sqlite_logic.give_weapon(), sqlite_logic.give_login()
        start = start_time
        HP = nick[1]
        MONSTER_HP = random.randint(1 * bb, int(25 * (weapon[1] / 3) * (weapon[2] / 3)))
        MONSTER_DAMAGE = random.randint(1 * bb, int(25 * (weapon[1] / 4) * (weapon[2] / 4)))
        critChance = random.randint(0, Weapon_handler.data['enchant'][weapon[4]][1])
        addDamage = 0
        if weapon[4] != 'mythic':
            addDamage = Weapon_handler.data['enchant'][weapon[4]][0]
        elif weapon[4] == 'mythic':
            addDamage = Weapon_handler.data['enchant'][weapon[4]][0] * weapon[1]
        weapon_damage = weapon[1] * (weapon[2] / 3) + addDamage
        while MONSTER_HP > 0:
            if critChance == 3:
                MONSTER_HP -= weapon_damage * 2
                sqlite_logic.log_access(f'КРИТИЧЕСКИЙ УДАР! Нанесено {int(weapon_damage) * 2} урона', start)
            else:
                MONSTER_HP -= weapon_damage
                sqlite_logic.log_access(f'Ты нанес {int(weapon_damage)} урона', start)
            time.sleep(1)
            HP -= MONSTER_DAMAGE
            sqlite_logic.log_access(f'Ты получил {int(MONSTER_DAMAGE)} урона', start)
            sqlite_logic.log_access(f'Оставшиеся ХП {int(HP)}', start)
            sqlite_logic.log_access(f'Оставшиеся ХП монстра {int(MONSTER_HP)}', start)
            if HP < 0:
                sqlite_logic.log_access(f'Ты умер.\nОставшиеся ХП у монстра: {int(MONSTER_HP)}', start)
                self.death_event()
        coin_NEW = random.randint(1, (10 * work))
        coin = coin_NEW + nick[4]
        sqlite_logic.log_access(f'Ты заработал {coin_NEW} EUTS', start)
        sqlite_logic.log_access(f'Оставшиеся ХП {int(HP)}', start)
        sqlite_logic.log_access(f'=====================', start)
        cur.execute('UPDATE HERO set HP = ?, balance = ?, MANA = ? where login = ?', (HP, coin, nick[3] + 5, nick[0]))
        conn.commit()
        sqlite_logic.close_connection()

    def death_event(self):
        QMessageBox.warning(minutes_main_menu.main_table(), 'Тебе конец.',
                            'Ты умер, и тебе определенно конец.\nАккаунт останется в базе данных мертвым грузом. Мухах.')
        sys.exit()
