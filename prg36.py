from prg32 import okroshka

#Методы списков и строк
#print(dir([]))
okroshka = ['Огурец', 'квас', 'кефир', 'соль', 'перец']
additional = ['колбаса', 'редис', 'картофель']

final = okroshka + additional + ['петрушка']
final.append('укроп') #final += ['укроп']

#Способ 3
print('Ингредиентов в окрошке:', len(final))
print('вот они', end=':')
final.sort()
print('\t', *final, sep='\n\t')