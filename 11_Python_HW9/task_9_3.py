# 3. Реализовать класс Worker (работник).
# Техническое задание:
#
# определить атрибуты: name, surname, position (должность), income (доход)
# атрибут income должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, '{"wage": wage, "bonus": bonus}'
# При создании экземпляра параметры wage, bonus передаются как числа.
# создать класс Position (должность) на базе класса Worker. Это наследование.
# в классе Position реализовать методы получения полного имени сотрудника '(get_full_name)' и дохода с учётом премии '(get_total_income)'.
# Методы возвращают соответсвующие значения. Подумайте, корректно ли в классе наследнике напрямую обращаться к защищенному атрибуту income.
# Или нужен getter? Аргументируйте ответ.
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position = "supermaster", wage=50000, bonus=30000):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {"wage": wage, "bonus": bonus}

    def get_name(self):                     # Returns name of instance
        for i, j in globals().items():
            if j is self:
                return i


class Position(Worker):
    def __init__(self, name, surname, wage=50000, bonus=60000):
        super().__init__( name, surname, wage, bonus)


    def get_full_name(self):
        return str(f'{self.name} {self.surname}')

    def get_total_income(self):
        return self._Worker__income['wage'] + self._Worker__income['bonus']




worker2 = Position(name ="Petr", surname ="Petrovich", wage=30000, bonus=40000 )
print(f'\nObject {worker2.get_name()} created')
print(f'worker2.get_full_name   = {worker2.get_full_name()}')
print(f'worker2.get_total_income = {worker2.get_total_income()}')

print('\nTesting variables : ')
print(f' worker2.name = {worker2.name}')
print(f' worker2.surname = { worker2.surname}')
print(f' worker2.position = {worker2.position}')
print(f' worker2.wage = {worker2.wage}')
print(f' worker2.bonus = {worker2.bonus}')
print(f' worker2.__income = {worker2._Worker__income}')
