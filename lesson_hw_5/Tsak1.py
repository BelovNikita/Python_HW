# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
#
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
import random


def random_abc(num):
    random_list = []
    letters = 'абв'
    for i in range(num):
        rand_string = ''.join(random.sample(letters, 3))
        random_list.append(rand_string)
    random_str = ' '.join(random_list)
    return random_str


N = int(input('Number of words:'))

if N > 0:
    new_list = random_abc(N)
    print(new_list)
    new_str = new_list.replace('абв ', '')
    print(''.join(new_str))

else:
    print('The data is incorrect')
