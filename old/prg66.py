#импортирование классов
from figures import Square

if __name__ == '__main__':
    sq1 = Square(10)
    print(sq1.get_height())
    print(sq1.get_width())