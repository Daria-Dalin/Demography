# Функции (encapsulation - инкапсуляция)
# Описание (define) функции

def say_hello(name='noname'):
    """
    Функция приветствия
    :param name: имя, с которым здороваются
    :return: None
    """
    print('Hello', name)

# вызов
say_hello('Дмитрий')
say_hello('Петр')
say_hello()