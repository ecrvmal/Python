# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Техническое задание:
#
# Создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# Перегрузить арифметические операторы: сложение ('add()'), вычитание ('sub()'), умножение ('mul()'), деление ('floordiv').
# Вспомнить/посмотреть какие аргументы у операторов и что они возвращают.
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение, и деление клеток, соответственно.
#
# Сложение. Число ячеек общей клетки равняться сумме ячеек исходных двух клеток.
# Вычитание. Число ячеек общей клетки равняться разности кол-ва ячеек исходных двух клеток.
# Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля, иначе использовать исключение
# - посмотрите какой тип исключения подойдет лучше всего.

# Умножение. Число ячеек общей клетки равняться произведению кол-ва ячеек исходных двух клеток.
# Деление. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# Реализовать метод 'make_order()',
# принимающий количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида '**\n\n***...', где количество ячеек между '\n' равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Возвращаемое значение предназначено для последующей передачи в функцию print, не используйте лишних слешей в строке.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод 'make_order()'
# вернёт строку: "*****\n*****\n**".
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод 'make_order()' вернёт строку:
# '*****\n*****\n*****'.
# Создать не менее пяти-семи экземпляров.
# Выполнить все арифметические операторы.
# Подтвердить тип полученного после операций объекта.
# Исходные клетки и результаты операций показать с помощью make_order


class Cell:

    def __init__(self, num_of_parts):
        if num_of_parts < 1 :
            raise ValueError('the Cell Object can not be created , parts < 1 ')
        self.num_of_parts = num_of_parts


    def print_info(self):
        print(f'Cell {self.get_name()}, of type : {type(self)}  with {self.num_of_parts} parts')

    def __add__(self, other):
        return Cell(self.num_of_parts + other.num_of_parts)

    def __sub__(self, other):
        if self.num_of_parts > other.num_of_parts:
            return Cell(self.num_of_parts - other.num_of_parts)
        else:
            raise ValueError('Not able to make substruction')

    def __mul__(self, other):
        return Cell(self.num_of_parts * other.num_of_parts)

    def __floordiv__(self, other):
        if other.num_of_parts == 0:
            raise ValueError('Not able to devide by 0 ')
        if self.num_of_parts < other.num_of_parts:
            raise ValueError('Not able to devide , a < b')
        result = self.num_of_parts // other.num_of_parts
        if result == 0:
            raise ValueError('the Cell Object can not be created , parts =0 ')
        else:
            return Cell(result)


    def get_name(self):
        for i, j in globals().items():
            if j is self:
                return i

    def make_order(self,n=10):                # Length of string is 10 by default, but can be changed by parameter n =
        string_res = ""
        strings = self.num_of_parts // n
        chars_left = self.num_of_parts % n
        for i in range(strings):
            for j in range(n):
                string_res += '*'
            string_res += '\n'
        for k in range(chars_left):
            string_res += '*'
        return string_res


print('\n----------------------')
c1 = Cell(4)
c1.print_info()
print(f'{c1.make_order()}')                 # Length of string is 10 by default, but can be changed by parameter n =

print('\n----------------------')
c2 = Cell(20)
c2.print_info()
print(f'{c2.make_order()}')

print('\n----------------------')
c3 = Cell(45)
c3.print_info()
print(f'{c3.make_order()}')

print('\n----------------------')
print("c4 = c1 + c3")
c4 = c1 + c3
c4.print_info()
print(c4.make_order())

print('\n----------------------')
print("c5 = c3 - c1")
c5 = c3 - c1
c5.print_info()
print(c5.make_order())

print('\n----------------------')
print("c6 = c1 * c2")
c6 = c1 * c2
c6.print_info()
print(c6.make_order())

print('\n----------------------')
print("c7 = c3 // c1")
c7 = c3 // c1
c7.print_info()
print(c7.make_order())

# Console Output:
#
# ----------------------
# Cell c1, of type : <class '__main__.Cell'>  with 4 parts
# ****
#
# ----------------------
# Cell c2, of type : <class '__main__.Cell'>  with 20 parts
# **********
# **********
#
#
# ----------------------
# Cell c3, of type : <class '__main__.Cell'>  with 45 parts
# **********
# **********
# **********
# **********
# *****
#
# ----------------------
# c4 = c1 + c3
# Cell c4, of type : <class '__main__.Cell'>  with 49 parts
# **********
# **********
# **********
# **********
# *********
#
# ----------------------
# c5 = c3 - c1
# Cell c5, of type : <class '__main__.Cell'>  with 41 parts
# **********
# **********
# **********
# **********
# *
#
# ----------------------
# c6 = c1 * c2
# Cell c6, of type : <class '__main__.Cell'>  with 80 parts
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
#
#
# ----------------------
# c7 = c3 // c1
# Cell c7, of type : <class '__main__.Cell'>  with 11 parts
# **********
# *

