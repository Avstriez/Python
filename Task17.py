# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
my_set = set(my_list)
print(my_set)
print(len(my_set)) 

# count = 0
# for i in my_set:
#     count += 1
# print(count) 
