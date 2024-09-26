import turtle as t  # подключили черепашку

# RAM - оперативная память random access memory
# DRY - do not repeat yourself (code should be clear)
sides = 8  # число сторон замкнутой фигуры
dist = 120  # переменной dist присвоено занчение 120
angle = 360 / sides  # угол, как 360 / sides
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.mainloop()
