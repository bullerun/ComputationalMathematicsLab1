import numpy as np


def correcting_the_matrix(matrix: list[list[float]], b):
    print("Корректировка")
    arr = []
    for i in range(len(matrix)):
        summ = sum(map(abs, matrix[i]))
        maximum = 0.0
        for j in matrix[i]:
            if abs(maximum) < abs(j):
                maximum = j
        summ -= abs(maximum)
        if abs(maximum) > summ:
            arr.append(matrix[i].index(maximum))
        elif abs(maximum) >= summ:
            f = matrix[i].index(maximum)
            j = f + 1
            is_two = False
            while j < len(matrix):
                if maximum == matrix[i][j]:
                    is_two = True
                    break
                j += 1
            if is_two:
                arr.append((f, j))
            else:
                arr.append(f)
    if len(matrix) == len(set(arr)):
        added_indexes = []
        new_matrix = [[] for _ in range(len(matrix))]
        new_arr = [-1 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            if type(arr[i]) == int:
                new_arr[i] = arr[i]
                added_indexes.append(arr[i])
        ignored_indexes = []
        while len(added_indexes) != 0:
            for i in range(len(arr)):
                for j in range(2):
                    if type(arr[i]) == tuple and arr[i][j] == added_indexes[0] and i not in ignored_indexes:
                        new_arr[i] = arr[i][(j + 1) % 2]
                        added_indexes.append(arr[i][(j + 1) % 2])
                        ignored_indexes.append(i)
            added_indexes.pop(0)
        if len(new_arr) == len(set(new_arr)) and -1 not in new_arr:
            new_b = b[:]
            for i in range(len(new_arr)):
                new_matrix[new_arr[i]] = matrix[i]
                b[new_arr[i]] = new_b[i]
            return new_matrix
        return matrix
    return matrix


def check_converge(iterator, x, x_new, eps) -> bool:
    maximum = 0
    flag = True
    for i in range(len(x)):
        maximum = max(maximum, abs(x_new[i] - x[i]))
        if abs(x_new[i] - x[i]) > eps:
            flag = False
    print(f'{iterator}. max|x{chr(0x2071)} - x{chr(0x2071)}{chr(0x207B)}{chr(0x00B9)}| = {maximum}')
    return flag


def check_diagonal(matrix: list[list[float]]):
    is_correct = True
    flag = False
    for i in range(len(matrix)):
        summ = sum(map(abs, matrix[i]))
        summ -= abs(matrix[i][i])
        if abs(matrix[i][i]) > summ:
            flag = True
            print(f"{abs(matrix[i][i])} > {summ}")
        elif abs(matrix[i][i]) >= summ:
            print(f"{abs(matrix[i][i])} >= {summ}")
        else:
            is_correct = False
            print(f"{abs(matrix[i][i])} < {summ}")
    a = is_correct and flag
    return a


def print_solution(matrix, x):
    for i in matrix:
        summa = 0
        for j in range(len(i)):
            if i[j] * x[j] < 0 or j == 0:
                char = ""
            else:
                char = "+"
            summa += i[j] * x[j]
            print(char + '{:.4}'.format(i[j] * x[j]), end=" ")
        print(' ={:.4}'.format(summa))


def print_matrix(matrix: list[list[float]]):
    mlen = (max(map(len, map(str, col))) for col in zip(*matrix))
    s = f"{' '.join(f'{{:>{ml}}}' for ml in mlen)}"
    for x in matrix:
        print(s.format(*x))


def get_solution(matrix: list[list[float]], b: list[float], eps: float):
    n = len(matrix)
    if not check_diagonal(matrix):
        matrix = correcting_the_matrix(matrix, b)
        if not check_diagonal(matrix):
            print("Неудалость привести к диагональьному виду")
            return
        print_matrix(matrix)
    x = np.zeros(n)
    iterator = 0
    converge = False
    while not converge:
        iterator += 1
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(matrix[i][j] * x_new[j] for j in range(i))
            s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / matrix[i][i]
        print(f'{iterator}. ', *x_new)
        converge = check_converge(iterator, x, x_new, eps)
        x = x_new
    print(f'количество итераций: {iterator}')
    print("конечное решение")
    print_solution(matrix, x)
