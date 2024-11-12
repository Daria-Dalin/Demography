# Функции (encapsulation - инкапсуляция)
# Область видимости переменных

# global scope
b = 5


def calc(x: int = 1, y: int = 0) -> int:
    # local scope
    b = 3
    res = 2 * x + y + b
    return res


def multy(*args: int) -> int:
    """
    фунцкия вычисления произведения перемеого числа аргументов
    :param args: ноль или несколько целых
    :return: произведение аргументов
    """
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args
    res=1
    for i in range(len(args))
        res *= args[i]
    return res

def increment():
    global b
    b += 1


print(multy(1, 2, 5, 8))
increment()
result = calc(b)
# garbage collector - сборщик мусора
print(result)
