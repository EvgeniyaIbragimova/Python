# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(my_list)
my_set = list(set(my_list))
print(my_set)