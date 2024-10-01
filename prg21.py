#управление циклом с помощью break and continue
for x in range(5):
    if x == 2:
        continue
    print(x)

for x in range(5):
    if x == 2:
        break
    print(x)
else:
    print('Нормальное завершение цикла')

# выведите элементы строки без пробелов
string = '0 сколько!'

for i in string:
    if i == ' ':
        continue
    print(i, end='')
print()

string = '0 сколько!'
for i in string:
    if i == '2':
        break
    print(i, end='')
print()