'''В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.'''

RANGE_MIN = 2
RANGE_MAX = 99

FREQUENCY_MIN = 2
FREQUENCY_MAX = 9

counter = [0] * (FREQUENCY_MAX - FREQUENCY_MIN + 1)
for i in range(RANGE_MIN, RANGE_MAX + 1):
    for j in range(FREQUENCY_MIN, FREQUENCY_MAX + 1):
        if i % j == 0:
            counter[j - RANGE_MIN] += 1

for i, item in enumerate(counter, FREQUENCY_MIN):
    print(f'Натуральному числу {i} кратно {item} чисел.')
