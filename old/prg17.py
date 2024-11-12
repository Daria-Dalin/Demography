# Введение в цикл for система 3 с
# s - start (по умолчанию ноль, включая это значение)
# s - stop (не включая)
# s - step (шаг - по умолчанию - 1)
# range (start, stop, step) 5-1 = 4 шага

for x in range(1, 5, 1):
    print(x)

for x in range(2, 22, 2):
    print(x)

for x in range(1, 12, 2):
    print(x)

for x in range(0, 5, 1):
    print(x)

for x in range(1, 6):
    print(x)

for x in range(3):
    print(x)

for x in range(3, 0, -1):
    print(x)

for x in reversed(range(1, 11)):
    print(x)

start = 1
stop = 10
step = 3

for g in reversed(range(start, stop, step)):
    print(g)
#for <переменная> in range(начало, финиш, шаг)


#первый способ
for i in range(1, 51, 1):
    if i%10==4:
        print(i)

#второй способ
for i in range(4, 50, 10):
        print(i)