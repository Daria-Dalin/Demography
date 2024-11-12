# спецметоды (operators for

class Square:
    def __init__(self, s):
        self.side = s

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

sq1 = Square(5)
sq2 = Square(5)
complex_sq = [Square(2), Square(3)]
square = sq1 + sq2
square = sq1 - sq2
print(square)
print(sq1 == sq2)
print(sq1 >= sq2)
