# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_number = int(input('Введите десятичное число -> '))
binary_number = ''
temp = decimal_number
while temp > 0:
    binary_number = str(temp % 2) + binary_number
    temp = temp // 2
print(f'{decimal_number} -> {binary_number}')
