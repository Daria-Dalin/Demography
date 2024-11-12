# умножение списка на число = повторяющееся значение в списке
# csv - разделенная точкой с запятой
a = [0] * 5
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[x for x in range(i, 13, 4)] for i in range(1, 5)]

print(c)

with open('personal.csv', encoding = 'utf-8') as f:
    text = f.read()

table = [r.split(';') for r in text.split('\n')]
print(table[2][1])