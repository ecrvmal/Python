# 4. Реализовать проект «Операции с комплексными числами».
# Техническое задание:
#
# Создайте класс «Комплексное число». Комплексное число - это упорядоченная пара чисел, например x,y. Для простоты числа берем только целые.
# Перегрузите методы(операторы) сложения/вычитания и умножения комплексных чисел (три метода). Правила сложения/умножения можно найти в сети.
# Перегрузите метод 'str' для вывода числа в виде x + yj, где x,y - атрибуты. Попробуйте учесть, что y может быть отрицательным.
# Создайте экземпляры класса (комплексные числа), выполните сложение/вычитание/умножение созданных экземпляров. Выведите на экран результат.
# Убедитесь, что операторы возвращают объект нужного типа.
# Встроенным типом данных complex пользоваться нельзя. Найдите в интернете описание правил сложения/вычитания и умножения комплексных чисел.
# При переопределении операторов помним, что возвращается новый объект, Аргументы остаются неизменными.
# Примеры/Тесты:
# Например так:
#
#
# Число 1: 2+3j
# Число 2: -1+1j
# Сложение: 1+4j
# Вычитание: 3+2j
# Умножение: -5-1j
#
# https://pyprog.pro/python/py/nums/complex.html


class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img
        pass

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        if isinstance(other,int):
            # kA = k(a + bi) = ka + kbi
            return Complex(self.real * other, self.img *other )

        if isinstance(other,Complex):
            # (a + bi)⋅(c + di) = (ac−bd) + (bc + ad)i
            return Complex((self.real * other.real-self.img * other.img), (self.img * other.real + self.real * other.img))

    def __str__(self):
        if self.img >= 0:
            return(f" {self.real} + {self.img}j ")
        else:
            return(f" {self.real} {self.img}j ")

# Число 1: 2+3j
# Число 2: -1+1j
# Сложение: 1+4j
# Вычитание: 3+2j
# Умножение: -5-1j

print("\n\t The programm operates with complex didits \n ")
a = Complex(2, 3)
print(f'object a {a} created of type {type(a)}')
b = Complex(-1, 1)
print(f'object b {b} created of type {type(b)}')

print("\n\tNow Calculations : ")

c = a+b
print(f'\n c = a + b ')
print(f' c = {c}')
print(f' type(c) = {type(c)}')

d = a - b
print(f'\n d = a - b ')
print(f' d = {d}')
print(f' type(d) = {type(d)}')

e = a * b
print(f'\n e = a * b')
print(f' e = {e}')
print(f' type(e) = {type(e)}')


# Console printout:
# object a  2 + 3j  created of type <class '__main__.Complex'>
# object b  -1 + 1j  created of type <class '__main__.Complex'>
#
# 	Now Calculations :
#
#
#  c = a + b
#  c =  1 + 4j
#  type(c) = <class '__main__.Complex'>
#
#  d = a - b
#  d =  3 + 2j
#  type(d) = <class '__main__.Complex'>
#
#  e = a * b
#  e =  -5 -1j
#  type(e) = <class '__main__.Complex'>
#
# Process finished with exit code 0
