# Задание 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

count_comp = int(input('Введите кол-во компаний: '))

companies = collections.deque()
sum_profit = 0

for i in range(count_comp):
    title = input('Введите название компании: ')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('Введите квартальные прибыли ч/з пробел: ').split(' '))
    profit_year = profit_q1 + profit_q2 + profit_q3 + profit_q4
    companies.appendleft((title, profit_year))

for company in companies:
    sum_profit += company[1]

avg_profit = sum_profit / count_comp

print(f'Среднегодовая прибыль среди всех компаний: {avg_profit}')
print(f'Прибыль выше средней: {[company[0] for company in companies if company[1] > avg_profit]}')
print(f'Прибыль ниже средней: {[company[0] for company in companies if company[1] < avg_profit]}')
