# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.
#
# in
# 6
#
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

new_list = []
n = int(input("Ввидите число: "))
for i in range(1, n + 1):
    m = (1 + 1/i) ** i
    new_list.append(round(m,3))
print(new_list)

sum = 0.0
for i in range(n):
    sum = sum + new_list[i]

print(sum)
