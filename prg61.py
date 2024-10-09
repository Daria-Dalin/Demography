# модули
import functions as f


# from functions import * - все подтянуть
# from function import summ, sub

def main():
    # если это главный исполняемый модуль
    # global
    try:
        first = 3
        second = 4





        print(f.summ(first, second))
        print(f.sub(first, second))
        print(f.divide(first, second))
        print(f.multiply(first, second))
        print(__name__)
    except:
        pass


if __name__ == '__main__':
    main()
