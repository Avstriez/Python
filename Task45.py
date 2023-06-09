# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284

def sum_del(num: int) -> int:
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += i
    return sum_

k = 300

for num_1 in range(2, k):
    sum_num_1 = sum_del(num_1)
    sum_num_2 = sum_del(sum_num_1)
    if (sum_num_2 == num_1) and (sum_num_1 != num_1):
        print(num_1, sum_num_1)
