# Функции калькулятора
def summ(a, b):
    """

    :param a: любое
    :param b: число
    :return: сумма
    """
    try:
        res = a + b
    except TypeError:
        print('Складываю только числа')
    else:
        return res


def sub(a, b):
    a = int(a)
    b = int(b)
    try:
        res = a - b
    except TypeError:
        return 'Вычитаю только числа'
    else:
        return res


def divide(a, b):
    """
    частное двух чисел
    :param a: любое
    :param b: число
    :return: частное
    """
    a = int(a)
    b = int(b)
    try:
        res = a - b
    except TypeError:
        return 'Делю только числа'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    else:
        return res


def multiply(a, b):
    """
    произведение двух чисел
    :param a: любое
    :param b: число
    :return: произведение
    """
    a = int(a)
    b = int(b)
    try:
        res = a * b
    except TypeError:
        return 'Умножаю только числа'
    else:
        return res


# __name__
print(__name__)
print('ЭТот модуль был полключен', __name__)
print('модуль functions подключен')
if __name__ == '__main__':
    print('не запускается меня. это библиотека функций')
