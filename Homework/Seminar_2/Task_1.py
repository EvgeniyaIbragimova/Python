# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите вещественное число -> ')
num_gigits = []
for i in num:
    if i.isdigit():
        num_gigits.append(int(i))
sum = 0
for i in num_gigits:
    sum += i
print(f'- {num} -> {sum}')
