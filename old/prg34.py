# от строк к спискам и наоборот

a = ['огурец', 'квас', 'кефир', 'соль', 'перец', 'колбаса', 'редис', 'картофель', 'укроп', 'укроп', 'петрушка']

b = a[:3]
b.sort()
# вывод списка строкой - способ 1
print(*b, sep=', ')
# вывод списка строкой - способ 2: из списка в строку
result = ", ".join(b)
print(result)

word = 'Pithon'

lst = list(word)
list[1] = 'y'
result = ''.join(lst)
print(result)