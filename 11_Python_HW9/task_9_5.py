# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
# Техническое задание:
#
# атрибут title (название)
# метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# Подумайте о том, имеет ли смысл при переопределении draw использовать draw базового класса.
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

from abc import ABC, abstractmethod


class Stationary(ABC):
    def __init__(self, title):
        self.title = title
        print(f'Item {self.title} created ')

    @abstractmethod
    def draw(self):
        pass


class Pen(Stationary):
    def __init__(self, title, color = "red", thickness = 1):
        super().__init__(title)
        self.color = color
        self.thickness = thickness


    def draw(self):
        print(f'Drawing Started by {self.title}, with {self.color} line , thickness = {self.thickness}')


class Pencil(Stationary):
    def __init__(self, title, color = "black", thickness = 3):
        super().__init__(title)
        self.color = color
        self.thickness = thickness


    def draw(self):
        print(f'Drawing Started by {self.title}, with {self.color} line , thickness = {self.thickness}')


class Handle(Stationary):
    def __init__(self, title, color = "green", thickness = 10):
        super().__init__(title)
        self.color = color
        self.thickness = thickness


    def draw(self):
        print(f'Drawing Started by {self.title}, with {self.color} line , thickness = {self.thickness}')



print('-----------------------------')
pen1 = Pen('Small_Pen')
pencil1 = Pencil('My_Lovely_Pencil')
handle1 = Handle('Old_Handle')
print('-----------------------------')
pen1.draw()
pencil1.draw()
handle1.draw()

# -----------------------------
# Item Small_Pen created
# Item My_Lovely_Pencil created
# Item Old_Handle created
# -----------------------------
# Drawing Started by Small_Pen, with red line , thickness = 1
# Drawing Started by My_Lovely_Pencil, with black line , thickness = 3
# Drawing Started by Old_Handle, with green line , thickness = 10
#
# Process finished with exit code 0