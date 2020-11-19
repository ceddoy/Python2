'''Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
'''

# Без "Решета Эратосфена" - здесь квадратичная сложность, и довольно не эффективно в сравнении с использованием Эратосфена
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

print(timeit.timeit('sieve(10)', number=1000, globals=globals())) # 8.078319832


cProfile.run('sieve(10)')
'''
         172 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.008    0.008    0.008    0.008 task_2_1.py:9(sieve)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
cProfile.run('sieve(100)')
'''
  1233 function calls in 0.427 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.427    0.427 <string>:1(<module>)
        1    0.426    0.426    0.427    0.427 task_2_1.py:9(sieve)
        1    0.000    0.000    0.427    0.427 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


