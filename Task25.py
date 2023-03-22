# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

start_str = 'a a a b c a a d c d d'
print(start_str)
start_str = start_str.split()

counts = {}

for char in start_str:
    if char in counts:
        counts[char] += 1
        print(f'{char}_{counts[char]}', end=' ')
    else:
        counts[char] = 0
        print(char, end=' ')
