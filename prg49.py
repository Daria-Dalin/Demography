# Чтение нескольких строк
fo = open('sample.txt', 'rt', encoding='UTF-8')  # по умолчанию режим rt
# print(dir(fo))
text = fo.readline()
while text != '': #если строка существует
    print(text, end='')
    text=fo.readline()
fo.close()  # открытый файл обязателньо закрывать
