# Задание 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

Base = 16

Hex = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

Bin = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
       'D': 13, 'E': 14, 'F': 15}


def sum_hex(first, second):

    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    while len(first) != 0:
        first_num = Bin[first.pop()]
        second_num = Bin[second.pop()]
        result_num = first_num + second_num + overflow

        if result_num >= Base:
            overflow = 1
            result_num -= Base
        else:
            overflow = 0

        result.appendleft(Hex[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


a = deque(input('Введите первое число в hex формате (только цифры от 0 до f): ').upper())
b = deque(input('Введите второе число в hex формате (только цифры от 0 до f): ').upper())

print(f'{list(a)} + {list(b)} = {list(sum_hex(a, b))}')

