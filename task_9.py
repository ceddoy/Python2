'''Найти максимальный элемент среди минимальных элементов столбцов матрицы.'''

import random

SIZE = 3
MIN_ITEM = -5
MAX_ITEM = 9

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]

for line in matrix:
    print(*line, sep='\t')

max_ = None

for i in range(len(matrix[0])):
    min_ = matrix[0][i]
    for j in range(len(matrix)):
        if matrix[j][i] < min_:
            min_ = matrix[j][i]
    if max_ is None or max_ < min_:
        max_ = min_
print(f'Максимальный элемент среди минимальных элементов - {max_}')
