# 5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
#
# in
# - 3
# - 6
# - 2
# - 1
#
# out
# 5.099

import math

Xa = int(input("Ввидите значение Xa"))
Ya = int(input("Ввидите значение Ya"))
Xb = int(input("Ввидите значение Xb"))
Yb = int(input("Ввидите значение Yb"))

d = math.sqrt(math.pow(Xb - Xa, 2) + math.pow(Yb - Ya, 2))
print(round(d, 3))