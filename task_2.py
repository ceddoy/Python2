'''
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

from random import uniform


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(lft, rft):
    sort_list = []
    idx_lft, idx_rht = 0, 0
    while idx_lft < len(lft) and idx_rht < len(rft):
        if lft[idx_lft] < rft[idx_rht]:
            sort_list.append(lft[idx_lft])
            idx_lft += 1
        else:
            sort_list.append(rft[idx_rht])
            idx_rht += 1
    sort_list += lft[idx_lft:]
    sort_list += rft[idx_rht:]
    return sort_list


SIZE = 10
array = [uniform(0, 50) for _ in range(SIZE)]
print(array)
print(merge_sort(array))
