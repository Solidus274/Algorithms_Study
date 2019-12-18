# Задание 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена

import timeit
import cProfile

# Без решета:

def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, current_prime):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime

# s = """
# def prime(num):
#     count = 1
#     current_prime = 2
#
#     while count < num:
#         current_prime += 1
#         for i in range(2, current_prime):
#             if current_prime % i == 0:
#                 break
#         else:
#             count += 1
#
#     return current_prime
# prime(1000)
# """

# print(timeit.timeit(s, number=100))
# 0.0022119999999999987 prime(10)
# 0.20905279999999998 prime(100)
# 30.7690859 prime(1000)


# 0.000 cProfile.run('prime(10)')
# 0.002 cProfile.run('prime(100)')
# 0.281 cProfile.run('prime(1000)')

# Исходное решето Эратосфена
# n = 100
#
# sieve = [i for i in range(n)]
# sieve[1] = 0
# for i in range(2, n):
#     if sieve[i] != 0:
#         j = i + i
#         while j < n:
#             sieve[j] = 0
#             j += i
#
# print(sieve)
# res = [i for i in sieve if i != 0]
# print(res)

# Модифицируем решето:


def eratos(num):
    array = [i for i in range(num ** 2)]
    array[1] = 0
    for i in range(2, num ** 2):
        if array[i] != 0:
            j = i + i
            while j < num ** 2:
                array[j] = 0
                j += i

    res = [i for i in array if i != 0]
    return res[num - 1]

# cProfile.run('eratos(5000)')

# 1    1.276    1.276    1.348    1.348 eratos(1000)
# 1    5.329    5.329    5.643    5.643 eratos(2000)
# 1   34.650   34.650   36.565   36.565 eratos(5000)


s = """
def eratos(num):
    array = [i for i in range(num ** 2)]
    array[1] = 0
    for i in range(2, num ** 2):
        if array[i] != 0:
            j = i + i
            while j < num ** 2:
                array[j] = 0
                j += i

    res = [i for i in array if i != 0]
    return res[num - 1]

eratos(250)
"""

# print(timeit.timeit(s, number=100))

# 1.0665438  eratos(100)
# 7.2436296  eratos(250)
# 32.1213329 eratos(500)