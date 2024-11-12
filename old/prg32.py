# Списки - iterable object, mutable - изменяемый тип коллекции

s = {'a', 1, 36.6} # множество
empty_set = set()
array = [] # пустой список
array = list() # пустой список
# index    0          1        2
array = ['ясно', 'пасмурно', 36.6]
print(array[0][0])
okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
print(okroshka[::2])

word = 'pithon' # immutable
# word[1] = 'y'  - Так делать нельзя
lst = list(word)

lst[1] = 'y'

print(*lst, sep='')

dishes = ['Борщ', 'пюре', 'компот', 'сок']
#first, second, third = dishes
# *eat, drink = dishes
first, second, *drink = dishes
print(drink)
