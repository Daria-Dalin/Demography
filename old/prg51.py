# Обучаемый словарь #2
# d = {
#   'меню': ['суп', 'тефтели', 'чай'],
#   'стул': 'chair',
#  'стол': 'table',
#  'яблоко': 'apple',
# }

d = {}  # наполнять будем из файла dict.dat
with open('dict.dat', encoding='UTF-8') as fo:
    line = fo.readline().rstrip('\n')
    while line != '':  # если строка существует
        k, v = line.split('|')
        d[k] = v
        line = fo.readline().rstrip('\n')

# rus = ''
rus = input('Введите слово на русском для перевода (или "q" для выхода): ')
while rus != 'q' and rus != 'Q':
    if rus in d:
        print(f'Слово "{rus}" переводится как "{d[rus]}"')
    else:
        print(f'К сожалению, я не знаю перевода слова "{rus}"')
        new_word = input(f'А как слово "{rus}" Переводится: ')
        d[rus] = new_word
        print(f'Теперь я знаю перевод слова "{rus}". Это - "{d[rus]}')

    rus = input('Введите слово на русском для перевода (или "q" для выхода): ')
# менеджер контекста
# fo = open('dict.dat', 'wt', encoding='UTF-8')
with open('dict.dat', 'wt', encoding='UTF-8') as fo:
    for k, v in d.items():
        print(k, v, sep='|', file=fo)

# fo.close()
print('Приятно было пообщаться!')
