#Файлы(чтение)
#бывают текстовые или бинарные (двоичные)
#Режимы: r - read, w - write, a - append
# подрежим: b- binary, t - text
#UTF-8 - Unicode Text Format (256-ASCII)

fo = open('sample.txt', 'rt', encoding='UTF-8') # по умолчанию режим rt

print(fo.name, fo.mode, fo.encoding)
fo.read(10)
text=fo.read(6)
text = fo.read()
lst = text.split()
# Как извлечь нужный фрагмент из текста(способ 1)
if 'внутри' in lst:
    for word in lst:
        if word == 'Внутри':
            print(word)
else:
    print('Такого слова в файле нет')

# Как извлечь нужный фрагмент из текста(способ 2)
if 'внутри' in lst:
   index = lst.index('внутри') #метод списка index
   print(lst[index])
else:
    print('Такого слова в файле нет')

print(lst[2])
print(text)
fo.close() # открытый файл обязателньо закрывать
