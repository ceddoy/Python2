'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''


def func_sum(n):
    sum_n = 0
    while n != 0:
        sum_n = sum_n + (n % 10)  # sum_n = n % 10 + func_sum(n // 10) - рекурсией
        n = n // 10
    return sum_n


num = int(input("Введите натуральное число,"
                "\nДля выхода введите '0': "))
sum_max = 0
num_max = 0
while num != 0:
    current_num = num
    current_sum = func_sum(num)
    if current_sum > sum_max:
        sum_max = current_sum
        num_max = current_num
    num = int(input("Введите натуральное число."
                    "\nДля выхода введите '0': "))
print(f'Число {num_max} имеет в себе максимальную сумму - {sum_max}')
