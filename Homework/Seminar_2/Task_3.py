# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = int(input('Введите число n -> '))
answer = []
temp = 1
for i in range(1, N + 1, 1):
    temp = (1 + 1 / i) ** i
    answer.append(temp)
print(f'- Для n = {N}: {answer}')
