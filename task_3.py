'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Список: {array}')

index_min = 0
index_max = 0

for i in range(len(array)):
    if array[i] < array[index_min]:
        index_min = i
    elif array[i] > array[index_max]:
        index_max = i

array[index_min], array[index_max] = array[index_max], array[index_min]
print(f'Измененный список: {array}')

