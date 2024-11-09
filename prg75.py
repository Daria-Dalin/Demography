#r - строка(row - "сырая")
import re # regular expressions(поиск по образцу)

pattern = '20'
test_string = '10 pluxs 20'
result = re.findall(pattern, test_string)
print(result)


string = r'C:\\Program\word.exe'
print(string)


pattern = r'\b\w{4}\b' #слова из 4 букв
pattern = r'\d'

pattern = r'\+7\d{10}'
test_string= '+791115864566554'