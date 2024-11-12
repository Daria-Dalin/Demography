# обработка исключений
def f_open(name: str) -> str:
    """
    читает текстовый файл
    и возвращает его содержимое
    :param name: имя файла на чтение
    :return: содержимое файла
    """


try:
    with open(name, encoding='UTF-8') as f:
        return f.read()
except FileNotFoundError:
    with open(name, 'w', encoding='UTF-8') as f:
        f.write('Файл был заново создан')

    return f'Файл {name} не существует или удалено'

res = f_open('sample.txt')
print(res)
