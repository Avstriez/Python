# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

A = int(input())
num_1 = 0
num_2 = 1
n = 2
while num_2 <= A:
    if num_2 == A:
        print(n)
        break
    num_1, num_2 = num_2, num_1 + num_2
    n = n + 1
else:
    print(-1)


# A = int(input())
# num_1, num_2, n = 0, 1, 2

# while num_2 < A:
# num_1, num_2 = num_2, num_1 + num_2
# n += 1

# print(n) if num_2 == A else print(-1)
