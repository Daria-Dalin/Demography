#проверка строки на палиндром


mr = input('введите строку: ')

temp = mr[::-1]

if temp == mr:
    print('Строка', mr, '-', 'палиндром')
else:
    print('Строка', mr, '-', 'не палиндром')
"""
s = set() # '', [], (), {}
res = dir(s)
print(s) #список методов для данного обхекта
print(help(s.lower)) # помощь по отдельному методу"""