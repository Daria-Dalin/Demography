#Файлы
#бывают текстовые или бинарные (двоичные)
#Режимы: r - read, w - write, a - append
# подрежим: b- binary, t - text
#UTF-8 - Unicode Text Format (256-ASCII)

fo = open('sample.txt', 'wt', encoding='UTF-8') # по умолчанию режим rt

print(fo.name, fo.mode, fo.encoding)
num=fo.write('Это текст внутри файла')
print(num)
fo.close() # открытый файл обязателньо закрывать
