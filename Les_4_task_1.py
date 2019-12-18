# Задание 1: Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# За испытуемого возмем 1 задание урока 3.

# По скорости работы быстрее всех алгоритм №3.
# Незначительно медленнее алгоритм №2, в котором используются множества
# Алгоритм №1 самый медленный возможно потому, что использует списки


import timeit
import cProfile


def natural_1(x):
    num = [0] * 8
    for i in range(2, x):
        for j in range(2, 10):
            if i % j == 0:
                num[j - 2] += 1
    return num


s = """
def natural_1(x):
    num = [0] * 8
    for i in range(2, x):
        for j in range(2, 10):
            if i % j == 0:
                num[j - 2] += 1
    return num

natural_1(500000) 
"""
# print(timeit.timeit(s, number=100))
# 7.2005517  natural_1(50000)
# 15.3991848 natural_1(100000)
# 32.6030774 natural_1(200000)
# 81.9885404 natural_1(500000)

# cProfile.run('natural_1(50000)')
# 1    0.097    0.097    0.097    0.097 Les_4_task_1.py:9(natural) natural_1(50000)
# 1    0.158    0.158    0.158    0.158 Les_4_task_1.py:9(natural) natural_1(100000)
# 1    0.353    0.353    0.353    0.353 Les_4_task_1.py:9(natural) natural_1(200000)
# 1    0.838    0.838    0.838    0.838 Les_4_task_1.py:9(natural) natural_1(500000)


def natural_2(x):
    num = {}
    for n in range(2, 10):
        num[n] = []
        for f in range(2, x):
            if f % n == 0:
                num[n].append(f)
    return num

s = """
def natural_2(x):
    num = {}
    for n in range(2, 10):
        num[n] = []
        for f in range(2, x):
            if f % n == 0:
                num[n].append(f)
    print(num)
    return num
    
natural_2(500000) 
"""
# print(timeit.timeit(s, number=100))
# 4.8519918 natural_2(50000)
# 10.7953385 natural_2(100000)
# 22.6662204 natural_2(200000)
# 57.6302349 natural_2(500000)

# cProfile.run('natural_2(500000)')

#         1    0.053    0.053    0.059    0.059 Les_4_task_1.py:42(natural_2) natural_2(50000)
#         1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
#     91442    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}

#         1    0.116    0.116    0.128    0.128 Les_4_task_1.py:42(natural_2) natural_2(100000)
#         1    0.000    0.000    0.130    0.130 {built-in method builtins.exec}
#    182891    0.012    0.000    0.012    0.000 {method 'append' of 'list' objects}

#         1    0.246    0.246    0.270    0.270 Les_4_task_1.py:42(natural_2) natural_2(200000)
#         1    0.000    0.000    0.273    0.273 {built-in method builtins.exec}
#    365788    0.023    0.000    0.023    0.000 {method 'append' of 'list' objects}

#         1    0.627    0.627    0.689    0.689 Les_4_task_1.py:42(natural_2) natural_2(500000)
#         1    0.000    0.000    0.697    0.697 {built-in method builtins.exec}
#    914478    0.062    0.000    0.062    0.000 {method 'append' of 'list' objects}


def natural_3(x):
    num = 0
    for i in range(2, 10):
        for j in range(2, x):
            if j % i == 0:
                num += 1
    return num


s = """
def natural_3(x):
    num = 0
    for i in range(2, 10):
        for j in range(2, x):
            if j % i == 0:
                num += 1
    return num

natural_3(500000)
"""

# print(timeit.timeit(s, number=100))
# 4.0735346 natural_3(50000)
# 10.8672627 natural_3(100000)
# 22.6952858 natural_3(200000)
# 52.4069692 natural_3(500000)

# cProfile.run('natural_3(500000)')
# 1    0.040    0.040    0.040    0.040 Les_4_task_1.py:89(natural_3) natural_3(50000)
# 1    0.091    0.091    0.091    0.091 Les_4_task_1.py:89(natural_3) natural_3(100000)
# 1    0.208    0.208    0.208    0.208 Les_4_task_1.py:89(natural_3) natural_3(200000)
# 1    0.497    0.497    0.497    0.497 Les_4_task_1.py:89(natural_3) natural_3(500000)
