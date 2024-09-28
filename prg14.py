# цикл while FOR
# count += 1 count = count + 1
import turtle as t

sides = 12
dist = 50
angle = 360 / sides
count = 0  # счетчик числа витков цикла
sq_count = 0  # счетчик числа сторон квадрата

t.speed(0)

while count < sides:
    sq_count = 0  # обнуляем счетчик сторон квадрата
    while sq_count < 4:  # внутренний
        t.forward(dist)  # вложенный цикл
        t.right(90)
        sq_count += 1
    t.right(angle)
    count += 1  # инкремент счетчика (увеличение на один), а декремент счетчика (уменьшение на 1)
else:  # необязательная часть используется редко
    print('Цикл завершен')

t.mainloop()
