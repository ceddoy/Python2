print("Введите координаты первой точки: ")
x1 = float(input("Введите х1 = "))
y1 = float(input("Введите y1 = "))

print("Введите координаты второй точки: ")
x2 = float(input("Введите х2 = "))
y2 = float(input("Введите y2 = "))

if (y2 - y1) != 0:
    k = (x2 - x1)/(y2 - y1)
    b = y2 - k * x2
    print(f"y = {k}x + {b}")
else:
    print("Нет решений")