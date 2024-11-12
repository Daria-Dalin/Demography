#Функции-антонимы chr и ord
# ASCII (256) 8 бит (2 ^ 8)
#Unicode (65536) 16 бит (2 ^ 16)

print(ord('a'))
print(chr(97))

s = '«Привет»'
print(ord('«'))

print(f'{chr(171)}ПРИВЕТ{chr(187)}')

print(chr(10000))

#\xB0 = chr(176)
print('75'+chr(176))
print(f'75 {chr(176)}C')
print('75\xB0C') # hexadecimal hex ASCII

print('\u2710') # Unicode

import string as s
temp=s.digits + s.ascii_lowercase +s.ascii_uppercase
m_set = set(temp - {'l', 'O', 'I', '1', '0'})
print(m_set)


