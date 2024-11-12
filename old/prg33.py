# операции со списками и методы списков
okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
additional = ['колбаса', 'редис', "картофель"]

final = okroshka + additional + ['укроп']
final.append('укроп') #final += ['укроп']
print(final + ['петрушка'])
print(final.pop(2))
temp = final.pop(2)
print(temp)
print(final.remove('соль'))
final.insert(4, temp)
print(final.index('перец'))
# final.clear()

# Способ 1
print('Ингредиентов в окрошке:', len(final))
print('ВОт они:')
count = 1
for item in final:
    print(f'\t{count}.{item}')
    count += 1

final.sort()

for item in range(len(final)):
    print(f'\t{item + 1}. {final[item]}')

# print(dir[])

# способ №3
print('Ингредиентов в окрошке:', len(final))
print('ВОт они:')
final.sort()
print(*final)
