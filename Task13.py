# # сколько дней длилась самая длинная оттепель.
# # Оттепелью они называют период,
# # в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# # Напишите программу, помогающую синоптикам в работе.
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

days_count = int(input())
len_plus_days = 0
max_len_plus_days = 0
days = []

# range(5) -> 0, 1, 2, 3, 4
# range(5, 11) -> 5, 6, 7, 8, 9, 10
# range(1, 11, 2) -> 1, 3, 5, 7, 9
for i in range(days_count):
    day = int(input(f'day_{i}--> '))
    days.append(day)
print(days)

for day in days:
    if day > 0:
        len_plus_days += 1
    else:
        if len_plus_days > max_len_plus_days:
            max_len_plus_days = len_plus_days
            len_plus_days = 0
print(max_len_plus_days)
