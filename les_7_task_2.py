# Задание 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
import numpy as np
data = [i for i in np.arange(0, 50, random.uniform(0, 10))]
random.shuffle(data)
print(f'Исходный массив: {data}')


def merge_sort(data):
    b = 1
    while b < len(data):
        a = 0
        while a + b < len(data):
            merge_process(a, b, b)
            a = a + b + b
        b = b + b
    print(f'Отсортированный алгоритмом массив: {data}')


def merge_process(a, b, c):
    if a + b < len(data):
        if c == 1:
            if data[a] > data[a + b]:
                data[a], data[a + b] = data[a + b], data[a]
        else:
            c = c // 2
            merge_process(a, b, c)
            if a + b + c < len(data):
                merge_process(a + c, b, c)
            merge_process(a + c, b - c, c)
    return data


merge_sort(data)