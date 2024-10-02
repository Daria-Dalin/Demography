# Виды коллекций в Python (итерируемые):
# 1. множества - set()
# 2. списки - list() -> []
# 3. кортежи - tuple()
# 4. словари - dictionary -> dict() {}

# множество неупорядоченная структура данныъ
# множество не содержит повторов
empty_set = set() # пустое множество
#num_set = {1, 2, 'Строка', 36.6, True, False}
num_set = {1, 2, 3}
print(num_set)
letter_set = {'a', 'b', 'c', 'c', 'a'}

letter_set.add('d')
letter_set.add('a')

print(letter_set)

#letter_set.pop() #случайное удаление элемента
letter_set.remove('a') # удаление конкретног оэлементас проверкой
letter_set.discard('e') # удаление вслепую


word = 'молоток'
if 'о' in word:
    print('Да')
letter_set = set(word)
print(letter_set)

error_method = set('1, 2, 3')
print(error_method)