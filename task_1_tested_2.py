import timeit, cProfile

# 2. Цикл
def func_sum(n):
    sum_n = 0
    while n != 0:
        sum_n = sum_n + (n % BASE)
        n = n // BASE
    return sum_n

BASE = 10
lst = [3, 12, 4, 5, 55, 6, 13, 35]

sum_max = 0
num_max = 0

for i in lst:
    current_num = i
    current_sum = func_sum(i)
    if current_sum > sum_max:
        sum_max = current_sum
        num_max = current_num
print(f'Число {num_max} имеет в себе максимальную сумму - {sum_max}')

print(timeit.timeit('func_sum(100)', number=1000, globals=globals())) # 0.001813614000000005
print(timeit.timeit('func_sum(200)', number=1000, globals=globals())) # 0.0013457450000000024
print(timeit.timeit('func_sum(500)', number=1000, globals=globals())) # 0.0011698379999999994
print(timeit.timeit('func_sum(1000)', number=1000, globals=globals())) # 0.0015665450000000025
print(timeit.timeit('func_sum(2000)', number=1000, globals=globals())) # 0.0016589880000000001
print(timeit.timeit('func_sum(4000)', number=1000, globals=globals())) # 0.001581842
print(timeit.timeit('func_sum(8000)', number=1000, globals=globals())) # 0.0018881000000000037
print(timeit.timeit('func_sum(16000)', number=1000, globals=globals())) # 0.0019140379999999999

cProfile.run('func_sum(10)')
cProfile.run('func_sum(100)')
cProfile.run('func_sum(1000)')
cProfile.run('func_sum(10000)')

# Для всех cProfile:
# 4 function calls in 0.000 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_1_tested_2.py:4(func_sum)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}