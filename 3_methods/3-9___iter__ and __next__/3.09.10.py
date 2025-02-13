class Matrix:
    @staticmethod
    def __raise_error_type():
        raise TypeError('аргументы rows, cols - целые числа;'
                        'fill_value - произвольное число')

    @staticmethod
    def __raise_error_index():
        raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __validate_matrix(self, matrix):
        if type(matrix) == list:
            if type(matrix[0]) == list:
                temp_len = len(matrix[0])
                for i in range(len(matrix)):
                    if len(matrix[i]) == temp_len:
                        for j in range(len(matrix[i])):
                            if type(matrix[i][j]) not in (int, float, complex):
                                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
                    else:
                        self.__raise_error_index()
            else:
                self.__raise_error_index()
        else:
            self.__raise_error_index()
        return True

    def __init__(self, *args):
        if len(args) == 3:
            self.rows, self.cols = args[0], args[1]
            if type(args[2]) in (int, float, complex):
                self.fill_value = args[2]
                self.list2d = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
            else:
                self.__raise_error_type()
        if len(args) == 1:
            if self.__validate_matrix(args[0]):
                self.list2d = args[0]

    def __getitem__(self, index):
        if type(index[0]) == int and index[0] < len(self.list2d):
            if type(index[1]) == int and index[1] < len(self.list2d[index[0]]):
                return self.list2d[index[0]][index[1]]

    def __setitem__(self, index, value):
        pass

    def __add__(self, other):
        slf_data = self.list2d if isinstance(self, Matrix) else self
        oth_data = other.list2d if isinstance(other, Matrix) else other
        res, temp = [], []
        for row in range(len(slf_data)):
            for col in range(len(slf_data[row])):
                if type(oth_data) == int:
                    temp.append(slf_data[row][col] + oth_data)
                else:
                    temp.append(slf_data[row][col] + oth_data[row][col])


# -----TEST-TASK-----
list2D = [[1, 2], [3, 4], [5, 6]]
st1 = Matrix(list2D)
print(st1.list2d)
print()
st2 = Matrix(4, 5, 6)
print(st2[2, 2])
# try:
#    st = Matrix(list2D)
# except TypeError:
#    assert True
# else:
#    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

"""list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"""
