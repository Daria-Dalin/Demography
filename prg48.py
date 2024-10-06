#Файлы (запись нескольких строк в файл)
#бывают текстовые или бинарные (двоичные)
#Режимы: r - read, w - write, a - append
# подрежим: b- binary, t - text
#UTF-8 - Unicode Text Format (256-ASCII)
total = 0
fo = open('sample.txt', 'at', encoding='UTF-8') # по умолчанию режим rt
fo.write('\n') # перевод на новую строку
num=fo.write('Это первая строка внутри файла\n')
total += num
num = fo.write('Это втоаря строка внутри файла\n')
print(f'в файл записано {total} байт (символов).')
fo.close() # открытый файл обязателньо закрывать

total = 0
fo = open('sample.txt', 'wt', encoding='UTF-8') # по умолчанию режим rt
fo.write('\n') # перевод на новую строку
num=fo.write('Это первая строка внутри файла\n')
total += num
num = fo.write('Это втоаря строка внутри файла')
print(f'в файл {fo.name} записано {total} байт (символов).')
fo.close() # открытый файл обязателньо закрывать
