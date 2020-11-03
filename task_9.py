print("Введите три разных числа")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if b < a < c or b > a > c:
    print(f'Среднее число: {a}')
elif a < b < c or a > b > c:
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')