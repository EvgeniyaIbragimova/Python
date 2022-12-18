# Реализуйте алгоритм перемешивания списка
# придумать алгоритм как перемешать список

from random import randint
start_line = int(input('Введите стартовую границу -> '))
end_line = int(input('Введите конечную границу -> '))
count_elements = int(input('Введите количество элементов -> '))
random_numbers = []
for i in range(count_elements):
    random_numbers.append(randint(start_line, end_line))
print(random_numbers)
import random 
random.shuffle(random_numbers)
print(random_numbers)
