# Задание 6: Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Номер буквы в алфавите: '))
n = ord('a') + n - 1
print('Это буква', chr(n))