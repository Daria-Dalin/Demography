#Операции между кортежами и другими объектами



s = 'Python'
s = (255, 128, 64)
print(len(s))
lst = ['Бремя', 'время', 'стремя']
# функция sorted() сортирует
# итерируемую последовательность
# и возвращает в виде списка
print(sorted(s))
temp = list(enumerate(lst))
print(temp)
print('Существительное:')
for index, value in enumerate(lst):
    print(f'\t{index + 1}. {value}')


for index, value in enumerate(lst):
    print(f'ДЛя данного списка:\n индекс - {index}\n Значение - {valie}')



