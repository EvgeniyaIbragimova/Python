# Напишите программу вычисления арифметичоского выражения заданного строкой
# Используйте операции +, -, /, *
# Пример:
# 2 + 2 => 4
# 1 + 2 * 3 => 7
# 1 - 2 * 3 => -5
# Добавьте возможность использования скобок, меняющих приоритет операции
# 1 + 2 * 3 => 7
# (1 + 2) * 3 => 9

user_input = input('Введите выражение: ')
num_str = ' '
parse = []
for sym in user_input:
    if sym.isdigit():
        num_str = num_str + sym
    else:
        parse.append(int(num_str))
        num_str = ' '
        parse.append(sym)
parse.append(int(num_str))
print(parse)

for i in range(1, len(parse) - 1):
    if parse[i] == '*' or parse[i] == '/':
        operand1 = parse[i-1]
        operand2 = parse[i+1]
        print(operand1)
        print(operand2)
