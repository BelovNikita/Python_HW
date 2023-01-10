# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample


def rand_list(Nums):
    new_list = sample(range(1, (Nums + 1) * 5), k=Nums)
    print(new_list)
    Sum = 0
    for i in range(0,len(new_list),2):
        Sum = Sum + new_list[i]
    return Sum

print(rand_list(int(input("Введите какое количество чисел задействовать: "))))

