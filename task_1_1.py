'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
# Попытался сделать с Counter, фигня какая-то получилась
from collections import Counter

QUARTER = 4 # в 1 году 4 квартала
group_company = []
profit_group_company = 0

quantity = int(input("Введите количество ваших компаний: "))

for i in range(1, quantity + 1):
    profit_company = 0
    name = input(f"Введите название {i}-й компании: ")
    for j in range(1, QUARTER + 1):
        n = int(input(f"Введите прибыль за {j}-й квартал: "))
        profit_company += n
    company = [{'name': name, 'quarter': Counter({'quarter': profit_company})}]
    profit_group_company += profit_company
    group_company.append(company)

avenger = profit_group_company / quantity
print(f"Средняя прибыль всех компаний составляет: {avenger}")

for i in group_company:
    if i[0]['quarter']['quarter'] > avenger:
        print(f'Компания {i[0]["name"]} заработала больше, чем средняя прибыль всех компаний '
              f'{i[0]["quarter"]["quarter"]} > {avenger}')
    elif i[0]['quarter']['quarter'] < avenger:
        print(f'Компания {i[0]["name"]} заработала меньше, чем средняя прибыль всех компаний '
              f'{i[0]["quarter"]["quarter"]} < {avenger}')

