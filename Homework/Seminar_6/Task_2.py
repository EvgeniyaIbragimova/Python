# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Первоначальный вариант

list_check = list(map(int,input('Введите числа через пробел -> ').split()))
result = 0
index = 1
for i in list_check:
    if index < len(list_check):
        result += list_check[index]
        index += 2
print(f'{list_check} -> ответ: {result}')

# Новый вариант

lst = list(map(int, input('Введите числа через пробел -> ').split()))
print(f'{lst} -> ответ:\
 {sum([lst[i] for i in range(len(lst)) if i % 2])}')