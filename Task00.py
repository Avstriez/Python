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
