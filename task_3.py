'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
'''

from random import randrange


# Да, да - расчёсочка, алгоритм взял с википедии

def combsort(arr):
    lenght_array = len(arr)
    gap = (lenght_array * 10 // 13) if lenght_array > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(lenght_array - gap):
            if arr[i + gap] < arr[i]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return arr


def mediana(arr):
    new_arr = combsort(arr)
    print(new_arr)
    return new_arr[len(arr) // 2]


M = 3
array = [randrange(0, 50) for _ in range(2 * M + 1)]
print(array)
print(f'Медиана - {mediana(array)}')
