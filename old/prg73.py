# syntax sugar (синтаксический сахар)
# списочные выражение (list comprehensions)
#[выражение for переменная in источник if условие]



ipaddress = '192.168.0.1'
s = ipaddress.split('.')
a = map(int, s)
print(s)
#a = [i for i in range(1, 11)]

# for i in range(1, 11):
# a.append(i)
#a = [i * i for i in range(1, 11)]
print(list(a))

a = [int(i) for i in ipaddress.s('.') if i > 0]
print(a)

b = [i for i in range(2, 11, 2)]
print(b)

greet = 'Hello World'
c = [i for i in greet if i.isupper()] #isupper()
d = [(pos, char) for pos, char in enumerate(greet)]
print(d)
