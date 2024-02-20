from core import get_solution


def file_input():
    print("""
    файл должен идти по шаблону
    размер матрицы который n <= 20
    матрица n*n, где каждая строчка матрицы должна идти с новой строки, а сами значения разделяться пробелом
    дальше n свободных членов каждый с новой строки
    в конце напишите точность вычислений
    """)
    while True:
        try:
            s = input("Введите название файла")
            with open(s, "r") as f:
                line = f.readline()
                try:
                    n = int(line)
                    if 20 < n and n < 1:
                        print("размерность должна быть 1<=n<=20 ")
                        return
                except ValueError:
                    print("Некорректно введена размерность")
                    return
                matrix = []
                for i in range(n):
                    arr = []
                    s = f.readline()
                    if len(s.split()) != n:
                        print("Неверное количество коэффицентов")
                        return
                    else:
                        for (j, c) in enumerate(s.split()):
                            try:
                                c = c.replace(",", ".")
                                arr.append(float(c))
                            except ValueError:
                                print(f"строка {i + 1} аргумент {str(j + 1)} некорректный")
                                return
                    if len(arr) == n:
                        matrix.append(arr)

                b = []
                for i in range(n):
                    s = f.readline()
                    try:
                        s = s.replace(",", ".")
                        b.append(float(s))
                    except ValueError:
                        print(f"Некорректный {i + 1} коэффициент")
                        return
                s = f.readline()
                try:
                    s = s.replace(",", ".")
                    eps = float(s)
                except ValueError:
                    print("Некорректно введена точность")
                    return
                get_solution(matrix, b, eps)
                return
        except Exception:
            print("Ошибка при попытке чтения файла")
