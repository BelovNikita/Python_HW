# 2. Для чисел в пределах от 20 до N найти числа,
# кратные 20 или 21. Use comprehension.
N = int(input('Введите число: '))
res = [el for el in range(20, N) if el % 20 == 0 or el % 21 == 0]
print(res)