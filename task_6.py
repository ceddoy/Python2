n = int(input("Введите порядковый номер алфавита: "))
letter = (ord('a') - 1) + n
if letter < ord("z"):
    print(chr(letter))
else:
    print('Необходимо вводить числа от 1 до 26')