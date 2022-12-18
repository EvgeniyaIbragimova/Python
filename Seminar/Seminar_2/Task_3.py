# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой

first_string = str(input('Введите строку, в которой будем искать -> '))
second_string = str(input('Введите строку, которую будем искать -> '))
count = 0
for i in range(len(first_string) - len(second_string)):
    if first_string[i] == second_string[0]:
        if (i + len(second_string)) < len(first_string):
            flag = True
        for j in range(1, len(second_string)):
            if second_string[j] != first_string[i + j]:
                flag = False
        if flag:
            count += 1
print(count)


string1 = str(input('Введите строку, в которой будем искать -> '))
string2 = str(input('Введите строку, которую будем искать -> '))
print(string1.count(string2))
