# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011

a = int(input())
result = []

while a:
    result.append(a % 2)
    a //= 2
result.reverse()

print(*(result), sep='')
