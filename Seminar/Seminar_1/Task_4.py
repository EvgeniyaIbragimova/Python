# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

num1 = float(input('Введите число -> '))
num2 = int(num1 * 10 % 10)
print(num2)