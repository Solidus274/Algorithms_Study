# Задание 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random
import cProfile

# Исходный алгоритм для сравнения:


def bubble(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    print(f'Отсортированный исходным алгоритмом массив: {array}')

# Новый алгоритм. Каждый проход количество сравнений уменьшатся на величину i


def bubble_new(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(f'Отсортированный новым алгоритмом массив: {array}')


array = [i for i in range(-100, 100)]
random.shuffle(array)
print(f'Исходный массив: {array}')

bubble(array)
bubble_new(array)
# cProfile.run('bubble(array)')
# 404 function calls in 0.006 seconds
# cProfile.run('bubble_new(array)')
# 205 function calls in 0.003 seconds
