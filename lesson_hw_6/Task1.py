# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
import random


def rand_list(Num):
    new_list = []
    for i in range(Num):
        new_list.append(random.randrange(1, 10, 1))
    print(new_list)
    return new_list


a = rand_list(int(input('Введите число: ')))

res = [a[i] for i in range(1, len(a)) if a[i] > a[i - 1]]

print(res)
