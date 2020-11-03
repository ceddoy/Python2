a = float(input("Введите длину 1-го отрезка: "))
b = float(input("Введите длину 2-го отрезка: "))
c = float(input("Введите длину 3-го отрезка: "))

if a + b >= c and a + c >= b and c + b >= a:
    if a == b and b == c:
        print("Треугольник равносторонний")
    elif a != b and b != c and c != a:
        print("Треугольник разносторонний")
    else:
        print("Треугольник равнобедренный")
else:
    print("Треугольник не получится")