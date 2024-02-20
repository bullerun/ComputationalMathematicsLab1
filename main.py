from console import console_input
from file import file_input


def main():
    print("как вы хотите ввести данные?")
    print("введите 1, если вы хотите ввести данные через консоль")
    print("введите 2, если вы хотите ввести данные через файл")
    print("введите 3, чтобы выйти")
    n = 4
    while n > 3:
        s = input()
        try:
            n = int(s)
            if n > 3 or n < 0:
                print("ошибка введна некорректная цифра")
        except ValueError:
            print(f'{s} не является числом')
    if n == 1:
        console_input()
    elif n == 2:
        file_input()


if __name__ == '__main__':
    main()
