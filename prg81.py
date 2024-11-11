#Декораторы
import time
def decoration(func):
    def wrapper(): # обертка
        origin = func()
        modified = origin + 'декоратор'
        return modified
    return wrapper

def time_measure(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'затраченное время {end - start}')
    return wrapper()

@decoration
def say_hello():
    return 'Hello'

def make_list():
    a = [i for i in range(5000000)]
    return a

make_list()

#greet = no_decoration(say_hello)

print(say_hello())