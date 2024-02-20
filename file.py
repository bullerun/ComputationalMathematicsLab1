from core import get_solution


def file_input():
    print("""
    файл должен идти по шаблону
    размер матрицы который n <= 20
    матрица n*n, где каждая строчка матрицы должна идти с новой строки, а сами значения разделяться пробелом
    дальше n свободных членов каждый с новой строки
    в конце напишите точность вычислений
    """)
    s = input("Введите название файла")
    with open(s, "rb") as f:
        line = f.readline()
        try:
            n = int(line)
        except ValueError:
            print("Некорректно введена размерность, она должна быть целым числом и меньше 21")
            return
        matrix = []
        for i in range(n):
            arr = []
            s = f.readline()
            if len(s.split()) != n:
                print("Неверное количество коэффицентов")
                return
            else:
                for (i, c) in enumerate(s.split()):
                    try:
                        arr.append(int(c))
                    except ValueError:
                        print("аргумент " + str(i + 1) + " некорректный")
                        return
            if len(arr) == n:
                matrix.append(arr)

        b = []
        for i in range(n):
            s = f.readline()
            try:
                b.append(int(s))
            except ValueError:
                print("Некорректный коэффициенты ")
                return
        s = f.readline()
        try:
            eps = float(s)
        except ValueError:
            print("Некорректно введена точность")
            return
        get_solution(matrix, b, eps)
