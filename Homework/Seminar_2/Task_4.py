# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

N = int(input('Введите число N -> '))
set = []
for i in range(-N, N + 1, 1):
    set.append(i)
print(f'- Для N = {N}: {set}')
numbers_index = list(map(int, input('Введите через пробел индексы элементов -> ').split()))
print(numbers_index)
product_elements = 1
for i in numbers_index:
    product_elements *= set[i]
print(f'Произведение элементов на указанных позициях -> {product_elements}')
