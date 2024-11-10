# умножение списка на число = повторяющееся значение в списке
# csv - разделенная точкой с запятой
import csv

with open('personal.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
    print(row)


with open('personal.csv', encoding = 'utf-8') as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"')
    row = list(reader)
    print(row[0]['ФИО'])
    for r in row:
        print(r['ПОЛ'])
