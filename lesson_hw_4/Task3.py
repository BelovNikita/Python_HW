# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# 
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# 
# in
# -1
# out
# Negative value of the number of numbers!
# []
# 
# in
# 10
# 
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
import random


def rand_list(Num):
    new_list = []
    for i in range(Num):
        new_list.append(random.randrange(1, 10, 1))
    print(new_list)
    return new_list


numbers = rand_list(int(input()))

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unique_numbers(numbers))