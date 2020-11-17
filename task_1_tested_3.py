import timeit, cProfile

# 3. Вложенные циклы
def calculation(list_lst):
    BASE = 10
    sum_max = 0
    num_max = 0
    for i in list_lst:
        current_num = i
        current_sum = 0
        while i != 0:
            current_sum = current_sum + (i % BASE)
            i = i // BASE
        if current_sum > sum_max:
            sum_max = current_sum
            num_max = current_num
    return f'Число {num_max} имеет в себе максимальную сумму - {sum_max}'

lst = [3, 12, 4, 5, 55, 6, 13, 35]
print(calculation(lst))


print(timeit.timeit('calculation(lst)', number=1000, globals=globals())) # 0.007831726999999997
print(timeit.timeit('calculation(lst)', number=1000, globals=globals())) # 0.008026257000000002
print(timeit.timeit('calculation(lst)', number=1000, globals=globals())) # 0.007763558999999996


cProfile.run('calculation')
# 3 function calls in 0.000 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}