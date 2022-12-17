# Напишите программу, которая принимаетна вход два числа и проверяет,
# является ли одно число квадратом другого
# Пример:
# 5, 25 -> да
# 8, 9 -> нет

num1, num2 = int(input('Введите число -> ')), int(input('Введите число -> '))
if num1 / num2 == num2:
    print(f'{num1}, {num2} -> да')
elif num2 / num1 == num1:
    print(f'{num1}, {num2} -> да')
elif num1 / num2 != num2:
    print(f'{num1}, {num2} -> нет')
elif num2 / num1 != num1:
    print(f'{num1}, {num2} -> нет')

num3, num4 = int(input('Введите число -> ')), int(input('Введите число -> '))
if num3 ** 2 == num4 or num4 ** 2 == num3:
    print(f'{num3}, {num4} -> да')
else:
    print(f'{num3}, {num4} -> нет')
