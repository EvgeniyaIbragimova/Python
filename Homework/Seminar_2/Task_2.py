# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число N -> '))
result = [1]
temp = 1
for i in range(2, N + 1):
    temp *= i
    result.append(temp)
print(f'- пусть N = {N}, тогда {result}')
