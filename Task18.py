# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5 -->1 2 3 4 5
# 6-> 5

n = int(input('Введите количество массива: '))
arr = [i for i in range(n)]
print(arr)
x = int(input('Введите число для поиска: '))

result = arr[0]
for i in range(len(arr)):
    if (x-arr[i]) < x-result and x-arr[i] > 0:
        result = i
print(result) 
