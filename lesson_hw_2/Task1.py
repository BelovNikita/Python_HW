# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
#
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

n = float(input("Ввидите число: "))
sum = 0

while n % 1 != 0:
    n *= 10

while n > 0:
    sum = sum + (n % 10)
    n = n // 10

print(int(sum))
