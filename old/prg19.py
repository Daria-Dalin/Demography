#стандартный вывод (stdout) - в консоль (print) console - con
# именованные аргументы: sep=' ' и end='\n'
#стандартный ввод (stdin) - c клавиатуры (input)

print('строка1', 'строка2', sep=' и ', end='.\n---')
print('Новая строка')

print('И смех', 'слезы','любовь', sep=', и ', end='.')

print('Сегодня в меню:', 'суп', 'пюре', 'компот', sep='\n\t- ')

num=5
#AYYYYYY первый спсобо
print('A' + 'y'*num)
#второй способ
print('A', end='')
for x in range(num):
    print('y', end='')
print()


"""
help(print) - Python console
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
"""
