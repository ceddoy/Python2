'''В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.'''

import random

SIZE = 10
MIN_ITEM = -150
MAX_ITEM = -99

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Список: {array}')

index_num = -1
for i in range(len(array)):
    if array[i - 1] < 0 and index_num == -1:
        index_num = i
    elif 0 > array[i] > array[index_num]:
        index_num = i

print(f'Максимальное отрицательное число - {array[index_num]}, позиция в массиве {index_num + 1}')
