# pass - Заглушка
for i in range(5):
    pass
    print('Привет', i)

for _ in range(5):
    print('Привет')

string = 'Телевизор'
# определение числа элементо итерируемого объекта


length = len(string)
# число 5600 - 4-значное
print('в слове', string, length, 'букв.')
print('число')
number = input('Введите целое число: ')
length = len(number)
print('Число', number, str(length) + '- x', 'значное.')

total = 0

for item in number:
    total += int(item)

print('Сумма разрядов числа', number, 'равна:', total)

total = 1
for item in number:
    total *= int(item)
print('Произведение разрядов числа', number, 'равно:', total)
