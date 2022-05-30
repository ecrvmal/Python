# 1. Реализовать класс Matrix (матрица).
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
#
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# |  3  5 32 |
# |  2  4  6 |
#
# | -1 64 -8 |
# | 3 5 8 3 |
# | 8 3 7 1 |
#
# Техническое задание:
#
# Элементы матрицы - целые числа(для простоты)
# Данные в матрице хранятся как список списков целых чисел.
# Реализовать перегрузку метода 'str()' для вывода матрицы в привычном виде - как в примере.
# Выравнивание чисел не обязательно, но желательно. Метод 'str()' возвращает строку.
# Реализовать перегрузку метода 'add()' для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица. Метод 'add()' возвращает новую матрицу. Исходные матрицы остаются неизменными.
# Сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
# Поэтому количество строк в обоих матрицах должно быть одинаковым. Аналогично со столбцами.
# Подумайте о проверках корректности данных при создании матрицы и при их сложении.
# Какие могут быть ошибки, когда мы работаем со списком списков.
# Что делают операторы (например сложения), когда выполнить операцию невозможно?
# Создать несколько матриц разного размера.
# Вывести их с помощью print
# Выполнить сложение матриц и вывести результат сложения.
# Подтвердить, что после сложения полученный объект имеет тип матрица.
# Усложнение:
#
# Добавить атрибуты - количество строк и столбцов матрицы.
# Использовать их в операторе сложения.


class Matrix:
    def __init__(self, matrix, start=0):
        self.matrix = matrix
        self.i = start -1
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


    def get_matrix_size(self):
        size = []
        if isinstance(self.matrix, list):       #   check 1D matrix
            size.append(len(self.matrix))       #   1D matrix size
        else:
            return size                         #   Not a Matrix
        if isinstance(self.matrix[0], list):    #   check 2D matrix
            size.append(len(self.matrix[0]))    #   2D matrix size
        else:
            return size                             #   return 1D matrix size
        if isinstance(self.matrix[0][0], list):     #   check 3D matrix
            size.append(len(self.matrix[0][0]))     #   3D matrix size
        else:
            return size                             #   return 2D matrix size
        if isinstance(self.matrix[0][0][0], list):  #   check 4D matrix
            size.append(len(self.matrix[0][0][0]))      #   4D matrix size
        return size                                 #   return 3D  or 4D matrix size

    def matrix_quality(self):
        a = self.get_matrix_size()
        if len(a) == 2:
            string_len = len(self.matrix[0])
            for i in range(a[0]):
                if len(self.matrix[i]) != string_len:
                    raise ValueError("Matrix is not correct")

        if len(a) == 3:
            string_len = len(self.matrix[0])
            raw_len = len(self.matrix[0][0])
            for i in range (a[0]):
                if len(self.matrix[i]) != string_len:
                    raise ValueError (" Matrix is not correct")

                else:
                    for j in range(a[1]):
                        if len(self.matrix[i]) != raw_len:
                            raise ValueError(" Matrix is not correct")

    def __str__(self):
        self.string1 = ""
        a = self.get_matrix_size()
        if not a:
            raise ValueError(" The input is not matrix")
        if len(a) == 1:
            self.string1 += self.print_line(self.matrix)
            return self.string1
        if len(a) == 2:
            for j in range(a[0]):
                self.print_line(list(self.matrix[j]))
            return self.string1
        if len(a) == 3:
            for j in range(a[1]):
                self.string1 += ' \n'
                for k in range(a[2]):
                   self.string1 += self.print_line(self.matrix[j][k])
            return self.string1

    def print_line(self, lst1):
        self.string1 += "\t |  "
        for i in range(len(lst1)):
            self.string1 += f' {lst1[i]} '
        self.string1 += " | \n"
        return self.string1

    def __add__(self, mtr2):
        size_mtr1 = Matrix.get_matrix_size(self)
        size_mtr2 = Matrix.get_matrix_size(mtr2)
        try:
            self.matrix_quality()
        except ValueError as e:
            print(self, e)
            exit()
        try:
            mtr2.matrix_quality()
        except ValueError as e:
            print(mtr2, e)
            exit()

        mtr2.matrix_quality()
        if size_mtr1 == size_mtr2:
            pass
        else:
            raise ValueError("Size of Matrix1 not equal to Size of Matrix2 ")
        m_list=[]
        for i in range(size_mtr1[0]) :
            m_list.append([])
            m_list[i] = [1,]
            for j in range(size_mtr1[1]-1) :
                m_list[i].append(0)

        if len(size_mtr1) == 2:
            for i in range(size_mtr1[0]):
                for j in range(size_mtr1[1]):
                    m_list[i][j] = self.matrix[i][j] + mtr2.matrix[i][j]
            m_matr =Matrix(m_list)
        return m_matr




#m3 = Matrix([[55, 66, 77],[88, 98, 99]])
# print(m3.print1000())



print('***********************************')
m1 = Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
m2 = Matrix([[10, 15, 20], [25, 30, 35], [40, 45, 50]])
print(f'type of m1 = {type(m1)}')
print(f'type of m2 = {type(m2)}')
print(f'size of m1 = {m1.get_matrix_size()}')
print(f'size of m2 = {m2.get_matrix_size()}')
print('\n')
print(m1)
print(m2)
try:
    print(m1 + m2 )
except ValueError as e:
    print(e)

print('***********************************')
m3 = Matrix([[1, 2, 3], [4, 5, 6]])
m4 = Matrix([[22, 33, 44], [55, 66, 77]])
m5 = m2 = Matrix([[10, 15, 20], [25, 30, 35], [40, 45, 50,55 ]])

print(m3)
print(m4)
try:
    print(m3 + m4 )
except ValueError as e:
    print(e)
print('***********************************')

print(m1)
print(m4)
print('***********************************')
try:
    print(m1 + m4 )
except ValueError as e:
    print(e)

try:
    print(m3 + m5 )
except ValueError as e:
    print(e)

# Console output:
# ***********************************
# type of m1 = <class '__main__.Matrix'>
# type of m2 = <class '__main__.Matrix'>
# size of m1 = [3, 3]
# size of m2 = [3, 3]
#
#
# 	 |   2  4  6  |
# 	 |   8  10  12  |
# 	 |   14  16  18  |
#
# 	 |   10  15  20  |
# 	 |   25  30  35  |
# 	 |   40  45  50  |
#
# 	 |   12  19  26  |
# 	 |   33  40  47  |
# 	 |   54  61  68  |
#
# ***********************************
# 	 |   1  2  3  |
# 	 |   4  5  6  |
#
# 	 |   22  33  44  |
# 	 |   55  66  77  |
#
# 	 |   23  35  47  |
# 	 |   59  71  83  |
#
# ***********************************
# 	 |   2  4  6  |
# 	 |   8  10  12  |
# 	 |   14  16  18  |
#
# 	 |   22  33  44  |
# 	 |   55  66  77  |
#
# ***********************************
# Size of Matrix1 not equal to Size of Matrix2
# 	 |   10  15  20  |
# 	 |   25  30  35  |
# 	 |   40  45  50  55  |
#  Matrix is not correct
#
# Process finished with exit code 0
