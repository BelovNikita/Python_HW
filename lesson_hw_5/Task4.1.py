import random
import time

count_of_candies = 2021

gamer_1 = input('введите имя 1 игрока: ')
bot = 'Бот'
m = random.randint(1, 2)
if m == 1:
    current_gamer = gamer_1
else:
    current_gamer = bot
while count_of_candies > 0:
    print(f"количество оставшихся конфет: {count_of_candies}")
    while True:
        if current_gamer == gamer_1:
            n = input(f"ход игрока {gamer_1}: ")
        if current_gamer == bot:
            time.sleep(1)
            n = random.randint(1, 28)
            print(f"ход бота: {n}")
        try:
            number_to_delete = int(n)
            if number_to_delete >= 1 and number_to_delete <= 28:
                break
        except:
            if n.isalpha():
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
    count_of_candies -= number_to_delete
    current_gamer = bot if current_gamer == gamer_1 else gamer_1
current_gamer = bot if current_gamer == gamer_1 else gamer_1
print(f"Победил {current_gamer}")
