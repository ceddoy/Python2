'''В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.'''

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Список: {array}')

if array[0] > array[1]:
    min_num_1 = 1
    min_num_2 = 0
else:
    min_num_1 = 0
    min_num_2 = 1

for i in range(2, len(array)):
    if array[i] < array[min_num_1]:
        num = min_num_1
        min_num_1 = i
        if array[num] < array[min_num_2]:
            min_num_2 = num
    elif array[i] < array[min_num_2]:
        min_num_2 = i
print(f'Минимальное число в списке {array[min_num_1]}, и следом минимальное число {array[min_num_2]}')