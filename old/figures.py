# классы фигур (наследование)
# родительский (базовый) класс (superclass)
# дочерний (производный, наследник)
from math import pi


class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return round((self.width + self.height) * 2, 1)

    # геттер
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # сеттер
    def set_width(self, new_w):
        self.width = new_w

    def set_height(self, new_h):
        self.height = new_h

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return round(self.side * 4, 1)

    def __str__(self):
        return f'это квадрат со стороной {self.side}'

    def __eq__(self, other):
        return self.side == other.side

    def __gt__(self, other):
        return self.side > other.side

    def __ge__(self, other):
        return self.side >= other.side

    def __add__(self, other):
        return Square(self.side + other.side)

    def __sub__(self, other):
        return Square(self.side - other.side)

    def __del__(self):
        print(f'Квадрат со стороной {self.side} стерт')

    def __repr__(self):
        return f'Квадрат со стороной {self.side}'


class Square(Rectangle):
    def __init__(self, s=1): # вызов конструктора базового класса
        super().__init__(s, s)
        self.side = s


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return round(2 * pi * self.radius, 1)
