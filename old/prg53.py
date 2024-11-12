# Функции (encapsulation - инкапсуляция)
# Возвращаемое занчение

def odd_even(num) -> str:
    """
    Функция возвращающая чет или нечет
    :param name: целое число
    :return: строку в которой чет или нечет
    """
    if not isinstance(num, int):
        return 'Ну ты даешь!'
    if num % 2:
        return 'нечет'
    return 'чет'


    # вызов
    res = odd_even(6)
    print(res)
