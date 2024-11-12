# задача

while True:
    a = input('Введите первое число:')
    b = input('Введите второе число')
    if a.isdigit() and b.isdigit():  # строки a b числа?
        if int(b) == 0:  # если второе число равно нулю
            print(' на ноль делить нельзя')
        else:
            print(int(a) / int(b))
            break
    else:
        print('Необходимо вводитель толь числа')

while True:
    # ввод значений a b c помощью тз
    a = input('Введите первое число:')
    b = input('Введите второе число')
    try:
        a = int(a)
        b = int(b)
        c = a / b

    except ValueError:  # некорректный ввод
        print('необхдоимо вводить целое число')
    except ZeroDivisionError:  # деление на ноль
        print('на ноль делить нельзя')

    else:
        print(c)
    break
