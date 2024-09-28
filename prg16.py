# цикличное выполнение программы
# вечный цикл и flag

name = input('ваше имя: ')

if name:
    pass
else:
    print('Введите хоть что-то')

choice = ''  # инициализация выбора пользователя
work = True

while work:
    choice = input('Введите R - для поворота направо '
                   'L - для поворота налево, или Q для выхода: ')
    if choice == 'L' or choice == 'l':
        print('Вы повернули налево: ', choice)
    elif choice == 'R' or choice == 'r':
        print('Вы повернули направо: ', choice)
    elif choice == 'Q':
        work = not work  # ивертировал булева значение мягкий разрыв
    else:
        print('Вы продолжили прямо', choice)

else:
    print('До свидания')

# Ключевая слова Import keyword. keyword.kwlist
#   ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
#  'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#help(input) in python consol