# операции над множествами
a = {1, 2, 3, 4}
b = {2, 3, 5, 7, 11}

# объединение множеств (union)
result = a.union(b)
print(result)

#result = a | b # здесь объединение | - 'или'

# пересечение множеств
#result = a.intersection(b)
result = a & b # & - И
# print(result)

# разность множеств
result = a.difference(b) # входит в одно, в другое не входит
result = a - b
result = b - a
print(result)

# симметричная разность
result = a.symmetric_difference(b)
result = a ^ b
print(result)



