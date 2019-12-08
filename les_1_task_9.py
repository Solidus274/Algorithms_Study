# Задание 9: Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

X = a
Y = b

if (a >= c >= b or a >= b >= c):
    X = a
elif (b >= a >= c or b >= c >= a):
    X = b
elif (c >= a >= b or c >= b >= a):
    X = c
if (a <= c <= b or a <= b <= c):
    Y = a
elif (b <= a <= c or b <= c <= a):
    Y = b
elif (c <= a <= b or c <= b <= a):
    Y = c
Z = (a + b + c) - (X + Y)

print(f'Среднее = {Z}')

