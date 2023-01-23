#  4. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random

count_of_candies = 2021
print(
    "На столе лежит 2021 конфета. \nИграют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход. ")
gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
m = random.randint(1, 2)
if m == 1:
    current_gamer = gamer_1
else:
    current_gamer = gamer_2

while count_of_candies > 0:
    print(f"количество оставшихся конфет: {count_of_candies}")
    while True:
        n = input(f"ход игрока {current_gamer} : ")
        try:
            number_to_delete = int(n)
            if 1 <= number_to_delete <= 28:
                break
        except:
            if n.isalpha():
                print("Введены буквы")
            else:
                print("Введены  непонятные  символа")
    count_of_candies -= number_to_delete
    current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
print(f"Победил {current_gamer}")