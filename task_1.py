'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
'''


from random import randrange

def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n): # уменьшаем количество итераций,
            # так как наименьшие числа уже сформированы слева списка и с ними сверяться, только лишняя
            # трата времени
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(arr) # Для отслеживания итерации
        n += 1
    print(arr)


SIZE = 10
array = [randrange(-100, 100) for _ in range(SIZE)]
print(array)
bubble_sort(array)