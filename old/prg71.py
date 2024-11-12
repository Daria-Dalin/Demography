# syntax sugar (синтаксический сахар)
печать = print  # передал ссылку на print

печать('Здравствуйте')

a = list(range(1, 11))  # создание списка с помощью range

# функция высшего порядка
b = list(map(str, a))
print(b)
res = ' и '.join(b)

print(res)


# список квадратов чисел из исходного списка
def square(num):
    return num ** 2


# square, поскольку простая, может быть записана и так
# ll = lambda num: num ** 2
# sum = lambda a, b: a+b

sq = list(map(lambda num: num * 2, a))
print(sq)

fruits = ['арбуз', 'ананас', 'банан', 'яблоко', 'манго']
fruits.sort(key=lambda letter: letter[1])
print(fruits)