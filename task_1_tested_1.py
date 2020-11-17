'''
Для каждого упражнения написать программную реализацию.
Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию). Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_4_task_1, les_4_task_2, и т.д.
Для оценки «Отлично» необходимо выполнить оба задания.
Результаты анализа сохранить в виде комментариев в файле с кодом.

1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
*******
Lesson 2 - 9 задача.
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''

import timeit, cProfile

# 1. Рекурсия
def func_sum_recursion(n):
    if BASE > n:
        return n
    return n % BASE + func_sum_recursion(n // BASE)

BASE = 10
lst = [3, 12, 4, 5, 55, 6, 13, 35] # Ввиду с условиями задачи, я заменил input на массив

sum_max = 0
num_max = 0
for i in lst:
    current_num = i
    current_sum = func_sum_recursion(i)
    if current_sum > sum_max:
        sum_max = current_sum
        num_max = current_num
print(f'Число {num_max} имеет в себе максимальную сумму - {sum_max}')



print(timeit.timeit('func_sum_recursion(100)', number=1000, globals=globals())) # 0.0008785419999999995
print(timeit.timeit('func_sum_recursion(200)', number=1000, globals=globals())) # 0.0011073219999999974
print(timeit.timeit('func_sum_recursion(500)', number=1000, globals=globals())) # 0.0012922079999999996
print(timeit.timeit('func_sum_recursion(1000)', number=1000, globals=globals())) # 0.0017128570000000017
print(timeit.timeit('func_sum_recursion(2000)', number=1000, globals=globals())) # 0.001334107000000001
print(timeit.timeit('func_sum_recursion(4000)', number=1000, globals=globals())) # 0.0011325939999999972
print(timeit.timeit('func_sum_recursion(8000)', number=1000, globals=globals())) # 0.0011106479999999988
print(timeit.timeit('func_sum_recursion(16000)', number=1000, globals=globals())) # 0.001440849000000001


cProfile.run('func_sum_recursion(10)')
# 5 function calls (4 primitive calls) in 0.000 seconds
# Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      2/1    0.000    0.000    0.000    0.000 task_1_tested_1.py:9(func_sum_recursion)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('func_sum_recursion(100)')
# 6 function calls (4 primitive calls) in 0.000 seconds
# Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      3/1    0.000    0.000    0.000    0.000 task_1_tested_1.py:9(func_sum_recursion)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('func_sum_recursion(1000)')
# 7 function calls (4 primitive calls) in 0.000 seconds
# Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      4/1    0.000    0.000    0.000    0.000 task_1_tested_1.py:9(func_sum_recursion)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('func_sum_recursion(10000)')
# 8 function calls (4 primitive calls) in 0.000 seconds
# Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      5/1    0.000    0.000    0.000    0.000 task_1_tested_1.py:9(func_sum_recursion)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
