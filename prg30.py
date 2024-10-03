# Форматирование строк\
# Place holders (плейсхолдеры)
# %s - для подстановки str
# %d - для подстановвки int (digit, decimal)
# %f - для подстановки float
# stackoverflow

name = 'Виктор'
age = 9
height = 141.5

# метод плейсхолдеров
f_string = '%10s, \nвозраст: %d, \nрост: %f см' % \
           (name, age, height)
print(f_string)

# использование метода format (именованные аргументы)
f_string = ('Имя: {N}, \nвозраст: {A}, \nрост: {H}'
            .format(N=name, A=age, H=height))

# использование метода format (позиционные аргументы)
f_string = ('Имя: {0}, \nвозраст: {1}, \nрост: {2}'
            .format(name, age, height))
# использование метода format (позиционные аргументы и плейсхолдеры)
f_string = ('Имя: {:s}, \nвозраст: {:d}, \nрост: {:.2f}'
            .format(name, age, height))

# интерполяция строк (f-строка)
f_string = f'Имя: {name}, Рост: {height:.2f}, Возраст: {age}'

f_string += f'При фигуре из 4 сторон угол будет: {360 / 4}'

print(f_string)
