# с использованием "Решета Эратосфена" тут линейная сложность, и намного эффективнее, чем в 1 без Эратосфена

import timeit, cProfile

def sieve_n(n):
    size = 1000
    new_sieve = []
    sieve = [i for i in range(size)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < size:
                sieve[j] = 0
                j += i
    for i in sieve:
        if i != 0:
            new_sieve.append(i)
    return f'Список простых чисел: {new_sieve}\n' \
           f'Запрашиваемое число по счёту - {new_sieve[n - 1]}'
print(sieve_n(4))

print(timeit.timeit('sieve_n(10)', number=1000, globals=globals())) # 0.35920639699999996
print(timeit.timeit('sieve_n(100)', number=1000, globals=globals())) # 0.514469385



cProfile.run('sieve_n(10)')
'''
236 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2_2.py:3(sieve_n)
        1    0.000    0.000    0.000    0.000 task_2_2.py:6(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      231    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
cProfile.run('sieve_n(100)')
'''
173 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 task_2_2.py:3(sieve_n)
        1    0.000    0.000    0.000    0.000 task_2_2.py:6(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''