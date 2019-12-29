# Задание 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random
array = [i for i in range(1 + 2 * int(input("Введите натуральное число: ")))]
random.shuffle(array)
print(f'Исходный массив: {array}')


def pigeon_sort(array):
    i = 0
    small = min(array)
    big = max(array) - small + 1
    holes = [0] * big
    for x in array:
        holes[x - small] += 1
    for count in range(big):
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + small
            i += 1
    print(f'Отсортированный алгоритмом массив: {array}')
    print(f'Медиана: {array[len(array)//2]}')

pigeon_sort(array)