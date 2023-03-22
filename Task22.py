# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Enter N: '))
m = int(input('Enter M: '))

array_1 = []
print('Enter N-numbers: ')
for i in range(n):
    array_1.append(int(input()))

array_2 = []
print('Enter M-numbers: ')
for i in range(m):
    array_2.append(int(input()))

set_1 = set(array_1)
set_2 = set(array_2)
set_result = set_1.intersection(set_2)
print('Во введенных наборах встречаются числа: ', end='')
print(*sorted(set_result))
