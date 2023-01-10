# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import sample


def rand_list(Nums):
    new_list = sample(range(1, (Nums + 1) * 2), k=Nums)
    print(new_list)
    l = len(new_list) // 2
    if len(new_list) % 2 != 0:
        final_list = [new_list[i] * new_list[len(new_list) - i - 1] for i in range(l)]
        final_list.append(new_list[l])
    else:
        final_list = [new_list[i] * new_list[len(new_list) - i - 1] for i in range(l)]
    print(final_list)


rand_list(int(input("Введите какое количество чисел задействовать: ")))
