print("Введите две буквы от 'a' до 'z'")
letter1 = input("Введите 1-ую букву: ")
letter2 = input("Введите 2-ую букву: ")

number1 = ord(letter1) - ord("a") + 1
number2 = ord(letter2) - ord("a") + 1

print(f'Позиция букв в алфавите "{letter1}" = {number1} и "{letter2}" = {number2}, между ними букв составляет: {abs(number1 - number2) - 1}')