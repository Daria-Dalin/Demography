# бросаемся исключениями
# (throw (java, c++, C# -> raise)
from multiprocessing.managers import Value

min_val = 1
max_val = 10

try:
    cur_val = int(input(f'введите целое числов от {min val} до {max_val}:'))
    if not min_val <= cur_val <= max_val:
        raise ValueError(f'введенное число вне диапозона ({min_val}...{max_val})')
    print(f'да, все верно. число {cur_val}'
          f'лежит в диапозоне от {min_val} до {max_val}')

except ValueError as exp:
    print('надо былть внимтельнее', exp)
