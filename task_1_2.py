# с namedtuple было по проще

from collections import namedtuple

QUARTER = 4 # в 1 году 4 квартала
group_company = []
profit_group_company = 0
Company = namedtuple('Сompany', 'name, profit')

quantity = int(input("Введите количество ваших компаний: "))

for i in range(1, quantity + 1):
    profit_company = 0
    name = input(f"Введите название {i}-й компании: ")
    for j in range(1, QUARTER + 1):
        n = int(input(f"Введите прибыль за {j}-й квартал: "))
        profit_company += n
    current_company = Company(name, profit_company)
    profit_group_company += profit_company
    group_company.append(current_company)

avenger = profit_group_company / quantity
print(f"Средняя прибыль всех компаний составляет: {avenger}")

for company in group_company:
    if company.profit > avenger:
        print(f'Компания {company.name} заработала больше, чем средняя прибыль всех компаний '
              f'{company.profit} > {avenger}')
    elif company.profit < avenger:
        print(f'Компания {company.name} заработала меньше, чем средняя прибыль всех компаний '
              f'{company.profit} < {avenger}')