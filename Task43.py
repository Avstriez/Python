# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

mylist = []
n = int(input("enter n "))
count = 0

for _ in range(n):
    mylist.append(int(input("enter: ")))
print(mylist)
#++++++++++++++++++++++++++++++++++++++++++++++
for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)):
        if mylist[i] == mylist[j]:
            count = count + 1
print(count)
#1 2 3 2 3