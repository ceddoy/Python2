import timeit, cProfile

# 4. Со встроенной функцией max
def calculation(lst):
    BASE = 10
    num_max = max(lst)
    sum_max = 0
    while num_max != 0:
        sum_max = sum_max + (num_max % BASE)
        num_max = num_max // BASE
    return f'Число {max(lst)} имеет в себе максимальную сумму - {sum_max}'

lst = [3, 12, 4, 5, 55, 6, 13, 35]
print(calculation(lst))


print(timeit.timeit('calculation(lst)', number=1000, globals=globals())) # 0.0019991650000000007
print(timeit.timeit('calculation(lst)', number=1000, globals=globals())) # 0.0024231400000000007
print(timeit.timeit('calculation(lst)', number=1000, globals=globals())) # 0.0017454460000000012
print(timeit.timeit('calculation(lst)', number=1000, globals=globals())) # 0.0018811170000000016

cProfile.run('calculation(lst)')
# 6 function calls in 0.000 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_1_tested_4.py:3(calculation)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''Выводы:
Мною было подготовлено 4 варианта кода (первый был изначально с прошлых практических заданий)
1) Первый вариант с рекурсией идет по схеме линейной функции.
2) Во втором варианте для эксперимента я заменил рекурсию на обычный цикл while, и линейная сложность 
никак не поменялась, но результат через timeif показал асимпототическую динамику чуть в большую сторону.
3) В третьем варианте я объединил в одной функции весь блок кода, кроме массива и использовал 
его для приема данных в функцию - calculation, по факту получилось 2 вложенных цикла, но сложность алгоритма
не поменялся остался - линейной.
4) В четвертом варианте я заменил часть блока кода из третьего варинта встроенной функцией max. И при этом
заметно лучше оптимизировал асимпототическую динамику в отличие от третьего варианта.
Для меня наилучшем вариантом способа реализации задачи является 1 вариант, но также не побрезговал 4 вариантом.
 '''

