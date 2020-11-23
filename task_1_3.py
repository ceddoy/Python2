import sys

def show(x):
    sum_mem = 0
    print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items(x):
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
                sum_mem += sys.getsizeof(item)
    sum_mem += sys.getsizeof(x)
    return sum_mem

list_memory = []
sum_memory = 0

num = input("Введите число для magic: ")
new_num = int(num[::-1])
list_memory.append(num)
list_memory.append(new_num)
print(f'Результат: {new_num}')
print('*' * 50)
print(f'Работа с памятью:\n'
      f'{list_memory}')

for i in list_memory:
    sum_memory += show(i)

print(f'Общая сумма памяти: {sum_memory}')
'''
Введите число для magic: 12345
Результат: 54321
**************************************************
Работа с памятью:
['12345', 54321]
type(x)=<class 'str'>, sys.getsizeof(x)=54, x='12345'
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=54321
Общая сумма памяти: 82

Вывод: Для эксперимента я воспользовался переменными состоящими из int (task_1_1) - 1 вариант (56 байт),
list + int (task_1_2) - 2 вариант (548 байт) и str + int (task_1_3) - 3 вариант (82 байта).
* 2 вариант сразу отпадает от удобства и оптимальности в решение текущей задачи, так как занимает больше памяти и
асимптотика будет куда больше, чем в остальных примерах.
* 3 вариант занимает больше памяти, чем 1 вариант, ну а также в этом варианте присутствует срез, 
а он нагружает асимптотику алгоритма O(n).
* 1 вариант является самым оптимальныи по занимаемой памяти, а также асимптотике алгоритма.
'''