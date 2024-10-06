#словари
# d = dict() # пустой словарь
# d = {} # пустой словарь
d ={
    'меню': ['суп', 'тефтели', 'чай'],
    1: 'chair',
    'стол': 'table',
    'яблоко': 'apple',
}

print(d['стол'])
print(d[1])
d['слива'] = 'plum'
print(d['груша'])
d[0] = 'one'
d[36.6] = 'normal'
print(d[36.6])
d[True] = 'Истина'
print(d[True])
print(dir(d))

print(len(d))
print(list(d.keys())) # список ключей словаря
print(list(d.values())) # список значений словаря
print(list(d.items())) # список кортежей (пар) (ключ, значение)
if 'слива' in d.keys():
    print('Слива есть среди ключей')
if 'Истина' in d.values():
    print('Истина есть среди ключей')
for key in d.keys():
    print(f'Ключ: {key}, Значение: {d[key]}')

for key, value in d.items():
    if value == 'Истина'
        print(f'Для Истина ключ - {key}')
    print(f'Ключ: {key}, Значение: {d[key]}')

print(d.get()['груша'])

del d['стул']
print(d)