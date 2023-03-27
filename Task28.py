# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4

a = int(input('a: '))
b = int(input('b: '))

def sum_func(a, b):
    if a == 0:
        return b
    return sum_func(a - 1, b + 1)

print(sum_func(a, b))
