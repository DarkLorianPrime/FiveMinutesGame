import random

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD


class game: 
    # Переменные для игры
    shoot = 1
    level = 1
    levelheal = 1
    cost = [10, 5]
    costheal = 25
    score = 0
    difficult = 1
    health = 100
    healthmax = 125
    healcount = 1
    curing = 15
    minus = 0
    #######
    # Неймы монстров и оружия#
    monstersfam = ['Тупой', 'Продажный', 'Страшный', 'Драконообразный', 'Этоктовообще', 'Слизнеподобный', 'Отсталый',
                   'Сильный', 'Убивающий', 'Милый', 'Звездный', 'из будущего', 'Нифига себе он умный', 'Яблочный',
                   'FUS RO DAH', 'Пизанский', 'из MAIL.RU', 'Открывающийся']
    monstersname = ['Огр', 'Дракон', 'Бог', 'Петух', 'Данил', 'Эльф', 'Тролль', 'Нуар', 'Кот', 'Деанон', 'Пони',
                    'Викинг', 'Леново', 'Простреленное колено', 'Агент', 'Орк', 'Уставший программист', 'Разрушитель',
                    'Артем', 'Акино', 'Грифон', 'Анимешник']
    guns = ['Скиайати', 'Скана', 'Экскалибур', 'Кладоносец', 'Дробовик', 'BAN HAMMER', 'UNBAN HAMMER',
            'Kotofey на палочке', 'Улучшенная палка с улицы', 'Разитель драконов без лезвия', 'ARTONЕСКО', 'AERO',
            'Кинжал', 'Тяжелый Арбалет', 'Бесстрашный Помощник', 'Питон (жалко змейку)', ]

    ###############
    # Upgrade#
    def upgrade(self, score, shoot, level, cost, guns):
        if score >= cost:
            game.shoot = shoot + 1
            game.level = level + 1
            game.score = score - cost
            print(cost)
            print(game.cost)
            game.cost[0] = cost + 15
            print(game.cost)
            messagebox.showinfo(title="upgrade",
                                message=f"Уровень вашего оружия повышен\nТеперь ваш уровень равен: {game.shoot}\nСледующий LEVEL UP будет стоить: {game.cost[0]}\nВы купили: {guns[random.randint(0, 9)]}")
            windows.update()
            game.a.destroy()
            try:
                self.shop().a
            except:
                print('окно обновлено')

        else:
            messagebox.showerror(title="Действие не выполнено.", message='На вашем счете не достаточно баблишка.')
            game.a.update()

    # Heal Upgrade#
    def upgradeheal(self, curing, costheal, levelheal, score, healthmax):
        if score >= costheal:
            game.curing = curing + 3
            game.score = score - costheal
            game.levelheal = levelheal + 1
            game.costheal = costheal + 10
            game.healthmax = healthmax + 3
            messagebox.showinfo(title="upgrade",
                                message=f"Уровень вашего восприятия зелий повышен\nТеперь ваш уровень равен: {game.levelheal}\nМаксимальное количество жизней теперь {game.healthmax}\nСледующий LEVEL UP будет стоить: {game.costheal}")
            game.a.destroy()
            try:
                self.shop().a
            except:
                print('окно обновлено')
        else:
            messagebox.showerror(title="Действие не выполнено.", message='На вашем счете не достаточно баблишка.')
            game.a.update()

    # Kill#
    def killhard(self, score, shoot, health, level):
        monsterdamage = 0
        monsterhp = 0
        level = level
        if level <= 5:
            monsterhp = random.randint(5, 10)
            monsterdamage = random.randint(1, 10)
        elif level >= 5 and level <= 10:
            monsterhp = random.randint(5, 10)
            monsterhp = ((monsterhp * 5) / 2)
            monsterdamage = random.randint(1, 10)
            monsterdamage = ((monsterdamage * 5) / 2)
        elif level >= 10 and level <= 100:
            monsterhp = random.randint(5, 10)
            monsterhp = ((monsterhp * level) / 2)
            monsterdamage = random.randint(1, 10)
            monsterdamage = ((monsterdamage * level) / 2)
        elif level >= 100:
            monsterhp = random.randint(10, 20)
            monsterhp = ((monsterhp * level) / 1.5)
            monsterdamage = random.randint(3, 20)
            monsterdamage = ((monsterdamage * level) / 1.5)
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        lbl.configure(
            text=f'Вы встретили  {game.monstersfam[j]} {game.monstersname[i]}\nУ монстра: {int(monsterhp)} хп\nЕго урон равен {int(monsterdamage)}\nВаш урон {int(shoot)}',
            font=('arial', 20, BOLD))
        while monsterhp > 0:
            health = (health - monsterdamage)
            monsterhp = (monsterhp - shoot)
        if health > 0:
            game.score = score + random.randint(8, 15)
            game.health = health
            messagebox.showinfo(title='Сводка о битве',
                                message=f'У босса осталось: {int(monsterhp)}\nУ вас осталось {int(health)}\nЗаказ завершен. Ваш счет:{game.score}')
            windows.after(200)
            lbl.configure(text='Вы перешли в главное меню.', font=('arial', 10, BOLD))
        else:
            messagebox.showinfo(title='А всё...', message='Ты умер. Окно закроется.')
            windows.after(3000, windows.destroy())
        return game.health, game.score

    # Heal#
    def heal(self, healcount, health, healthmax, curing):
        if game.healcount > 0:
            game.health = health + curing
            if game.health > healthmax:
                game.healcount = healcount - 1
                print(f'{game.health} - Макс хп.')
                minus = game.healthmax - game.health + curing
                print(minus)
                game.health = health + minus
                messagebox.showinfo(title="Вы использовали зелье.",
                                    message=f'Вы потеряли {- minus} хп,\nВы восстановили {game.curing} HP, теперь у вас {game.health}\nОсталось еще {game.healcount} баночек регенерации')
                print("\nвы потеряли:", minus, 'хп')
            else:
                game.healcount = healcount - 1
                game.health = health + curing
                messagebox.showinfo(title="Вы использовали зелье.",
                                    message=f'Вы восстановили {game.curing} HP, теперь у вас {game.health}\nОсталось еще {game.healcount} баночек регенерации')
        else:
            messagebox.showerror(title="Не удалось использовать зелье",
                                 message=f'У вас их просто нет.')

    # Buy Heal#
    def healbuy(self, healcount, score):
        if score >= game.cost[1]:
            game.score = score - 5
            game.healcount = healcount + 1
            messagebox.showinfo(title='Уведомление о покупке',
                                message=f'Поздравляем с покупкой! Теперь у вас {game.healcount} зелий')
            game.a.destroy()
            try:
                self.shop().a
            except:
                print('окно обновлено')
        else:
            messagebox.showerror(title="Действие не выполнено.", message='На вашем счете не достаточно баблишка.')
            game.a.update()

    def save(self, ):
        if messagebox.askokcancel("Ты выходишь...", "Ты уверен что хочешь выйти?"):
            windows.destroy()

    # Магнит#
    def shop(self):
        game.a = Toplevel()
        a = game.a
        a.update()
        a.resizable(False, False)
        a.update()
        a.title('Магазин Game')
        Button(text=f"Улучшение Оружия{game.cost[0]}", width=30)
        button_openbutton1 = ttk.Button(a, text=f"Улучшение Оружия - {game.cost[0]}", width=30,
                                        command=lambda: game.upgrade(game.score, game.shoot, game.level, game.cost[0],
                                                                     game.guns))
        a.update()
        windows.update()
        lbl1 = Label(a, text=f'Уровень способности: {game.level}')
        button_openbutton2 = ttk.Button(a, text=f"Улучшение восприятия зелий - {game.costheal}",
                                        command=lambda: game.upgradeheal(game.curing, game.costheal, game.levelheal,
                                                                         game.score, game.healthmax), width=30)
        a.update()
        lbl2 = Label(a, text=f'Уровень способности: {game.levelheal}')
        button_openbutton3 = ttk.Button(a, text=f"Купить новое зелье здоровья - {game.cost[1]}",
                                        command=lambda: game.healbuy(game.healcount, game.score), width=30)
        a.update()
        lbl3 = Label(a, text=f'У вас: {game.healcount} зелий')
        button_openbutton4 = ttk.Button(a, text=f"Выход", command=lambda: a.destroy())
        a.update()
        lbl4 = Label(a, text=f'На вашем счете: {game.score} очков.')
        button_openbutton1.pack(expand=1, )
        lbl1.pack()
        button_openbutton2.pack(expand=2, )
        lbl2.pack()
        button_openbutton3.pack(expand=3, )
        lbl3.pack()
        button_openbutton4.pack(expand=4, )
        lbl4.pack()
        lbl.configure(text="Вы перешли в магазин, взаимодействие происходит в соседнем окне.")
        ######
        # if command == 'healUpgrade':
        #       curing, score, levelheal, game.prices['healUpgrade'], healthmax = game.upgradeheal(game.curing,
        #                                                                                         prices[
        #                                                                                            'healUpgrade'],
        #                                                                                       game.levelheal, game.score,
        #                                                                                      game.healthmax)
        # pass

        # if command == 'heal':
        #        score = score - game.cost[1]
        #        healcount = game.healcount + 1
        #       print("У вас", healcount, "Баночек")
        #      pass

        # if command == 'stat':
        #        print('Вы открыли доступ к своей статистике')
        #        stat = 1
        #        pass

        # if command == 'exit':
        # print('Вы вышли из магазина.')
        # else:
        #    print(f'Not enough points: needs {game.prices[command]}, you have only {game.score}')


game = game()
windows = Tk()
windows.update()
windows.protocol("WM_DELETE_WINDOW", game.save)
windows.minsize(500, 500)
windows.maxsize(500, 500)
lbl = Label(text="Ты попал туда, откуда не выбираются \n25 школе привет", bg="#525050", fg="#ffffff", width="500",
            height="20")
lbl.pack()
button_kill = ttk.Button(windows, text='Пойти в рейд',
                         command=lambda: game.killhard(game.score, game.shoot, game.health, game.level))
button_kill.pack(expand=1)
windows.resizable(False, False)
windows.title('Game')
btn1 = Button(text="shop", width=200, command=game.shop, font=('arial', 20, BOLD), border=2)
btn1.pack(pady=10, )
btn2 = Button(text="Heal", width=200,
              command=lambda: game.heal(game.healcount, game.health, game.healthmax, game.curing),
              font=('arial', 20, BOLD), border=2)
btn2.pack(pady=10)
###
# elif move == "heal" and game.healcount > 0:
#       healcount, health = game.heal(game.healcount, game.health, game.healthmax, game.curing)
#
# elif move == "heal" and game.healcount <= 0:
#        print('У вас не хватает баночек. Попробуйте купить их в магадане.')
#
# elif move == "fix":
#        print('Убрана система шанса\nДобавлена система Максимального Здоровья\nДобавлен магазин')
##
# elif move == "exit":
#    1
###

windows.mainloop()
