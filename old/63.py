# private __ доступ извне напрямую закрыт
# public - доступ открыт для всех
# protected _ доступ открыт только для членов производных классов

class Man:
    def __init__(self, n='noname', a=0):  # конструктор
        self.name = n
        self.age = a
        self.non_legal_names = ['Васек', 'Павлик']

    def info(self):
        print(f'{self.name}, возрастом {self.age}')

    # ГЕТТЕРЫ (getters)
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # сеттер (setter)
    def set_age(self, new_age):
        if new_age < 0:
            self.age = -new_age
        else:
            self.age = new_age

    def set_name(self, new_name):
        if new_name not in self.non_legal_names:
            self.name = new_name
        print('имя недопустимо. замены не было.\n'
              'cписок запрещенных имен', end=': ')

    def print_non_legal_names(self):
        print(*self.non_legal_names, sep=', ')


dima = Man('Дмитрий', 17)
dima.set_name('Васек')
dima.set_age(-18)
# print(dima.age)
dima.info()
n = dima.get_name()
print(n)
