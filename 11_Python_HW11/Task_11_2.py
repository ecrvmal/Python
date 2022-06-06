# 2. Создать собственный класс-исключение, для обработки ситуации деления на ноль и функцию, выполняющую деление двух чисел.
# Техническое задание:
#
# Собственный Класс-исключение используется только для «подмены» исключения.
# Вы можете создать в нем конструктор, если хотите наполнить его данными.
# Функция принимает два числа и возвращает результат их деления. Она не является методом класса-исключения.
# В случае деления на ноль выкидывает исключение, упомянутое выше.
# В основой программе выполните вызов функции для различных значений (в том числе для деления на ноль - обязательно).
# Сформируйте обработку исключения в основной программе и выводите сообщение в случае деления на ноль.
# Усложнение:
# Сформируйте для класса-исключения сообщение, включающее делимое и делитель и
# сообщение о невозможности деления. Для этого придется наполнить исключение данными.


class MyZeroDevisionError(ZeroDivisionError):
    def __init__(self, text, a ):
        self.a = a
        self.text = text
        pass


class MyClass:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        if other.value == 0:
            raise MyZeroDevisionError("Trying to divide by 0", other.value )
        else:
            self.value = float(self.value / other.value)
            return MyClass(self)

    def __str__(self):
        return f"{self.value}"

print(f'The programm creates new class of variables and trying division by 0 \n  ')
a = MyClass(5)
print(f' variable a  = {a} created ')
b = MyClass(2)
print(f' variable b  = {b} created ')
print ("trying c = a/b ")
try:
    c = a/b
    print(f"c = {c}")
except MyZeroDevisionError  as err:
    print(f' {err.text} , value = {err.a}')
print('----------------------------------------------------')
a = MyClass(5)
print(f' variable a  = {a} created ')
d = MyClass(0)
print(f' variable d  = {d} created ')
print ("trying c = a/d ")
try:
    c = a/d
    print(f"c = {c}")
except MyZeroDevisionError  as err:
    print(f' {err.text} , value = {err.a}')

