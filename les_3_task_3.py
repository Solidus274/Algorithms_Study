# Задание 3: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print(f'Минимальное число: {mn}, Максимальное число: {mx}')
arr[imn], arr[imx] = arr[imx], arr[imn]

for i in range(15):
    print(arr[i], end=' ')
print()

