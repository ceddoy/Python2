import sys

def show(x):
    sum_mem = 0
    print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items(x):
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
                sum_mem += sys.getsizeof(item)
    sum_mem += sys.getsizeof(x)
    return sum_mem

list_memory = []
sum_memory = 0

my_list = list(map(int, input("Введите число для magic: ")))
list_memory.append(my_list)
new_list = list(reversed(my_list))
list_memory.append(new_list)
new_num = int(''.join(map(str, new_list)))
list_memory.append(new_num)
print(f'Результат: {new_num}')
print('*' * 50)
print(f'Работа с памятью:\n'
      f'{list_memory}')
for i in list_memory:
    sum_memory += show(i)

print(f'Общая сумма памяти: {sum_memory}')

'''
Введите число для magic: 12345
Результат: 54321
**************************************************
Работа с памятью:
[[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 54321]
type(x)=<class 'list'>, sys.getsizeof(x)=120, x=[1, 2, 3, 4, 5]
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=1
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=2
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=4
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=5
type(x)=<class 'list'>, sys.getsizeof(x)=120, x=[5, 4, 3, 2, 1]
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=5
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=4
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=2
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=1
type(x)=<class 'int'>, sys.getsizeof(x)=28, x=54321
Общая сумма памяти: 548

Process finished with exit code 0

'''