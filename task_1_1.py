'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843 - Lesson_2 ПЗ 3.
'''
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

num = int(input("Введите число для magic: "))
list_memory.append(num)
new_num = 0
while num > 0:
    new_num = new_num * 10 + num % 10
    num = num // 10
list_memory.append(new_num)
print(f'Результат: {new_num}')

print('*' * 50)

print(f'Работа с памятью:\n'
      f'{list_memory}')
for i in list_memory:
    sum_memory += show(i)

print(f'Общая сумма памяти: {sum_memory}')

'''
Версия - Windows 7 Профессиональная (версия 6.1 сборка 7601: Servise Pack 1)
Разрядность - 64
Версия интерпретатора Python - sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0)

Введите число для magic: 12345
Результат: 54321
**************************************************
Работа с памятью:
[12345, 54321]
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=12345
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=54321
Общая сумма памяти: 56
'''