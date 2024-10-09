# утверждение (assertion) для разработчика, исключения для пользователя
from prg20 import length
length = 3

try:
    text = input('введите любой текст')
    assert len(text) > length # утверждеие
    print(f'вы ввели: {text}')
except AssertionError:
    print(f'нет. ваш текст корочеб чем {length} Заготовка')