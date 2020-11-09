'''
Напишите программу, доказывающую или проверяющую, что для
множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''

def sum_num(n):
    if n == 1:
        return n
    sum_n = n + sum_num(n - 1)
    return sum_n

num = int(input("Введите любое натуральное число до 998 включительно: "))

left_num = sum_num(num)
right_num = num * (num + 1) / 2

if left_num == right_num:
    print(f'Левая сумма - {left_num} совпала с правой суммой - {int(right_num)}')
else:
    print(f'Левая сумма - {left_num} не совпала с правой суммой - {int(right_num)}')
