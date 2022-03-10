# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    # def __init__(self, matrix):
    #     self.matrix = matrix

    def __init__(self, matrix):
        self.matrix = matrix

    def fill_matrix(self, rows_num, columns_num):
        self.i = 0
        while self.i < rows_num:
            self.row = []
            self.j = 0
            while self.j < columns_num:
                self.el = int(input(f'Введите [{self.i}:{self.j}] элемент матрицы: '))
                self.row.append(self.el)
                self.j += 1
            self.matrix.append(self.row)
            self.i += 1

    def __str__(self):
        self.matrix_str = ''
        for self.row in self.matrix:
            for self.el in self.row:
                self.matrix_str += f'{self.el} '
            self.matrix_str += '\n'
        return self.matrix_str

    def __add__(self, other):
        matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                result = self.matrix[i][j] + other.matrix[i][j]
                row.append(result)
            matrix.append(row)
        return Matrix(matrix)
a = []
b = []
matrix_a = Matrix(a)
matrix_a.fill_matrix(2, 3)
matrix_b = Matrix(b)
matrix_b.fill_matrix(2, 3)
print(matrix_a)
print(matrix_b)
print(matrix_a + matrix_b)
