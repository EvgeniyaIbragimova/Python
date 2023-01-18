# Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого

# Первоналчальный вариант

num1, num2 = int(input('Введите число -> ')), int(input('Введите число -> '))
if num1 / num2 == num2:
    print(f'{num1}, {num2} -> да')
elif num2 / num1 == num1:
    print(f'{num1}, {num2} -> да')
elif num1 / num2 != num2:
    print(f'{num1}, {num2} -> нет')
elif num2 / num1 != num1:
    print(f'{num1}, {num2} -> нет')

# Новый вариант

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = lambda a, b: a**2 == b or b**2 == a
print(x(a, b))
