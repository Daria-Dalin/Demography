# обработка исключений

#try (начало обработки)
# здесь выполняется попытка какого-либо действия
# except (собственно обработчик)
# исключение обарбатывается
# finally (не обязательна)
# программа продолжается в этом месте
# независимо от того, было исключение или нет
# else
# если не было исключения

def divide():


    a = int(input('Введите А:'))
    b = int(input('Введите В: '))
    try:
        temp = a/b
        return temp
    except ZeroDivisionError:
        return "Не делите на ноль"
    except Exception as exp:
        return f'вот такое вот: {exp}'
   # except ValueError:
     #   return 'Нужно вводить только целые числа'
print(divide())

while True:
    try:
        int_val=int(input('введите целое число'))
        print(f'Успешно ввели: {int_val}')
        break
    except ValueError: # Ошибка в значении
       print('вас просят ввести число')
       print('Попробуйте снова')