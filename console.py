from core import get_solution


def input_free_members(n: int):
    arr = []
    for i in range(n):
        s = input("Введите свободный член для " + str(i + 1) + " уравнения: ")
        try:
            arr.append(float(s))
        except ValueError:
            print("Некорректный коэффициент")
    return arr


def input_coefficients(n: int, i: int) -> list[float]:
    while True:
        arr = []
        s = input("Введите коэффициенты " + str(i + 1) + " строки матрицы через пробел: ")
        if len(s.split()) != n:
            print("Неверное количество коэффицентов")
        else:
            for (j, c) in enumerate(s.split()):
                try:
                    c = c.replace(",", ".")
                    arr.append(float(c))
                except ValueError:
                    print("аргумент " + str(j + 1) + " некорректный")
        if len(arr) == n:
            return arr


def input_of_the_dimension() -> int:
    while True:
        s = input("Введите размер матрицы: ")
        try:
            if 1 <= int(s) <= 20:
                return int(s)
            else:
                print("ошибка 1 <= n <= 20")
        except ValueError:
            print("Некорректно введена размерность, она должна быть целым числом и меньше 21")


def input_accuracy() -> float:
    while True:
        s = input("Введите точность вычислений: ").replace(",", ".")
        try:
            s = s.replace(",", ".")
            return float(s)
        except ValueError:
            print("Некорректно введена точность")


def console_input():
    n = input_of_the_dimension()
    matrix = []
    for i in range(n):
        matrix.append(input_coefficients(n, i))
    b = input_free_members(n)
    eps = input_accuracy()
    get_solution(matrix, b, eps)
