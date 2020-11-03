https://drive.google.com/file/d/1KvKVqKNC0t7uwDtrIV6rLT9otKy4TPPJ/view?usp=sharing


a = int(input("Введите трёхзначное чило:  "))
a1 = a % 10
a2 = a % 100 // 10
a3 = a // 100
m = a1 + a2 + a3
p = a1 * a2 * a3
print(f'суммa числа {a} составляет: {m}, а произведение чисел составляет: {p}')