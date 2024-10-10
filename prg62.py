# объектно-ориентированный подход
# инкапсуляция
class Ball:
    # спецюметоды (члены класса)
    def __init__(self, diametr, color):
        self.diametr = diametr
        self.color = color
        print('выделил место под мяч')

    # методы класса
    def info(self):
        print('мяч имеет цвет, ', self.color)
        print('размер мяча ', self.diametr)


ball1 = Ball(5, 'красный')  # ball1 - экзампеляр класса Ball #1
ball2 = Ball(10, 'синий')
ball3 = Ball()
ball4 = ball3

print(id(ball1))
print(id(ball2))
print(id(ball3))
print(id(ball4))

ball1.info()
ball2.info()
ball3.info()

print(ball1.diametr, ball1.color)
print(ball2.diametr, ball2.color)
