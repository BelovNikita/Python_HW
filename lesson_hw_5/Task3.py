# 3. Создайте программу для игры в "Крестики-нолики".
# Поле 3x3. Игрок - игрок, без бота.

d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kol = 0
q = "X"
for i in range(0, 3):
    print(f' {d[i * 3]} | {d[i * 3 + 1]} | {d[i * 3 + 2]}')
    print("___________")
while kol < 9:
    t = "Крестик " if q == "X" else "Нолик "
    while True:
        number = input(f"{t}: ")
        try:
            n = int(number)
            if 1 <= n <= 9:
                break
        except:
            if number.isalpha():
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
    d[n - 1] = q
    for i in range(0, 3):
        print(f' {d[i * 3]} | {d[i * 3 + 1]} | {d[i * 3 + 2]}')
        print("___________")
    kol += 1
    q = "X" if q != "X" else "O"
    r = ""
    for i in range(0, 2):
        if d[3 * i] == d[3 * i + 1] and d[3 * i + 1] == d[3 * i + 2]:
            r = d[3 * i]
        if d[i] == d[3 + i] and d[3 + i] == d[6 + i]: r = d[i]
    if d[0] == d[4] and d[4] == d[8]: r = d[0]
    if d[2] == d[4] and d[4] == d[6]: r = d[2]
    if r == "" and kol > 8:
        print("Ничья")
        break
    if r != "":
        print(f'{"Крестики" if r == "X" else "Нолики"} выиграли')
        break
