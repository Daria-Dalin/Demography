#сложное условие (логическое "ИЛИ")
#AND, a потом OR
string = '' #пустая строка

name = input('your name: ')
surname = input('your surname: ')
age = input('your age:')
gender = input('your gender: ')


if name == 'Вася' and surname == 'Пупкин':
    print('Уважайте Ваше имя!!!')
else:
    #основные условия
    if (gender == 'М' or gender == 'м'
            or gender == 'v' or gender == 'V'):
        string = 'Уважаемый '
    elif (gender == ':' or gender == ';'
            or gender == 'Ж' or gender == 'ж'):
        string = 'Уважаемая '
    else:
        string = 'Уважаемый товарищ, '

    string = (string + name + ' ' + surname + ' ' +
              'Ваш возраст: ' + age + '.')
    ##################
print(string)