'''Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
'''
import timeit, cProfile

def sieve(n):
    lst = []
    for i in range(2, (n * 100) + 1):
        if i > 10:
            if i % 2 == 0 or i % 10 == 5:
                continue
        for j in lst:
            if j > (i ** 2) + 1:
                lst.append(i)
            if i % j == 0:
                break
        else:
            lst.append(i)
    return f'Список простых чисел: {lst}\n' \
           f'Запрашиваемое число по счёту - {lst[n - 1]}'

print(sieve(6))

print(timeit.timeit('sieve(10)', number=1000, globals=globals())) # 7.880149146
print(timeit.timeit('sieve(100)', number=1000, globals=globals())) # 0.042455789

cProfile.run('sieve(10)')
'''
         21 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_1.py:9(sieve)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       17    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
cProfile.run('sieve(100)')
'''
  113 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.004    0.004 task_2_1.py:9(sieve)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      109    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


