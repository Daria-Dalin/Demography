# итерируемый объект (iterable object) - последовательность
# int и float не являются интерируемым объектом
# и операции с ним
string = 'абвгдейка'

for symbol in string:
    print(symbol)

string2 = 'росток'

if 'ток' in string2:
    print('ток есть в строке', string2)

string2 = 'Вася Пупкин'

if 'Пупкин' in string2:
    print('Не надо писать:', '"' + string2 + '"')


