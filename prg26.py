# Примеры задач с множествами

forbidden = {'l', 'O', 'I'}
letters = {'a', 'b', 'c', 'd', 'l', 'O', 'I'}
digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# удаляем некорректные символы
remove_incorrect = letters - forbidden
# объединяем с цифрами
temp = remove_incorrect | digits
temp = list(temp)
for i in range(5):
    print(temp[i], end='') #[] - обратиться по индексу
