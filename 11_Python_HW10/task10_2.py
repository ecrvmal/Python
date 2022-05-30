# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Техническое задание:
#
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название/имя (атрибут).
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это целые числа, например V и H, соответственно.
# Имена атрибутов можете сделать другими.

# Создать метод расчета ткани для каждого класса: пальто, костюм по формуле:
# для пальто '(V/6.5 + 0.5)', для костюма '(2*H + 0.3)'.
# Выполнить общий подсчёт расхода ткани для всех созданных экземпляров, отдельно для пальто, отдельно для костюма.
# Алгоритм должен работать для любого кол-ва экземпляров.
# Общий расход ткани на все экземпляры - это тоже данные. Где их логично хранить?

# Не принципиально будет ли накапливаться общий расход ткани определенным методом или будет скрыт
# внутри других методов/конструктора.
# Проверить на практике полученные на этом уроке знания. Использовать абстрактный класс для «одежды».
# Подумайте что должно быть абстрактным методом в классе «одежда». Вспомните что должно быть в коде метода,
# когда он еще не наполнен никакой логикой.
# Используйте наследование. Переопределите абстрактные методы в классах-наследниках.

# Проверить работу декоратора '@property'.
# Не допускайте дублирования кода или спагетти-кода (кода с многочисленными проверками условий).
# Тщательно продумайте что должно быть данными (атрибутами), а что методами.
#
# Создать не менее 3 экземпляров классов с различными данными.
# Провести расчет ткани для каждого - вывести на экран
# Продемонстрировать накопительный счетчик общего расхода ткани по каждому классу.
# Примеры/Тесты:
# Здесь специально не показан вывод общего количества ткани, чтобы это не было для вас избыточной подсказкой.
#
#
# >>> c1 = Coat(12)
# >>> c2 = Coat(1)
# >>> c3 = Coat(121)
# >>> c1.add_to_reserve
# >>> c2.add_to_reserve
# >>> c3.add_to_reserve
# >>> print(c1.cloth_require)
# 2.3461538461538463
# >>> print(c2.cloth_require)
# 0.6538461538461539
# >>> print(c3.cloth_require)
# 19.115384615384617
# >>>

from abc import ABC, abstractmethod


class Clothes(ABC):
    material_qty_total = 0
    def __init__(self, name, color="blue", matherial="cotton"):
        self.color = color
        self.matherial = matherial
        self.name = name

        print(f'\n CLothes  {self.name} created \n')

    @abstractmethod
    def material_qty(self):
        return self.material_qty

    @property
    def material_qty_print(self):
        print(f'for {self.get_name} you need {self.material_qty:5.2f} of {self.get_color} {self.matherial}')
        print(f'\tClothes.material_qty_total = {Clothes.material_qty_total:5.1f}')
        print(f'\tCoat_material_qty_total = {Coat.material_qty_coat:5.1f}')
        print(f'\tSuit_material_qty_total = {Suit.material_qty_suit:5.1f}')

    @property
    def get_name(self):
        return self.name

    @property
    def get_color(self):
        return self.color

    @property
    def get_matherial(self):
        return self.matherial


class Coat(Clothes):
    material_qty_coat = 0.

    def __init__(self, name, size, color = "blue", matherial = "cotton"):
        super().__init__( name, color, matherial)
        self.size = size

    @property
    def material_qty(self):
        qty = self.size / 6.5 + 0.5
        Coat.material_qty_coat += qty
        Clothes.material_qty_total += qty
        return qty


class Suit(Clothes):
    material_qty_suit = 0.
    def __init__(self, name, height, color= "blue", matherial="cotton"):
        super().__init__(name, color, matherial)
        self.height=height

    @property
    def material_qty(self):
        qty = self.height * 2 + 0.3
        Suit.material_qty_suit += qty
        Clothes.material_qty_total += qty
        return qty

# main()
c1 = Coat(name='Yellow_Coat H&M', size= 50, color="yellow", matherial="Sheep's Wool")
c1.material_qty_print

c2 = Coat (name='Red Coat Prada', size=60,color="Red", matherial="Sheep's Wool")
c2.material_qty_print

s1 = Suit(name='Black official Suit', height=1.70, color="Black", matherial="Thin Wool")
s1.material_qty_print

s2 = Suit(name='Blue casual Suit', height=1.80, color="Blue", matherial="Thin Wool")
s2.material_qty_print

# Console output:
#
#  CLothes  Yellow_Coat H&M created
#
# for Yellow_Coat H&M you need  8.19 of yellow Sheep's Wool
# 	Clothes.material_qty_total =   8.2
# 	Coat_material_qty_total =   8.2
# 	Suit_material_qty_total =   0.0
#
#  CLothes  Red Coat Prada created
#
# for Red Coat Prada you need  9.73 of Red Sheep's Wool
# 	Clothes.material_qty_total =  17.9
# 	Coat_material_qty_total =  17.9
# 	Suit_material_qty_total =   0.0
#
#  CLothes  Black official Suit created
#
# for Black official Suit you need  3.70 of Black Thin Wool
# 	Clothes.material_qty_total =  21.6
# 	Coat_material_qty_total =  17.9
# 	Suit_material_qty_total =   3.7
#
#  CLothes  Blue casual Suit created
#
# for Blue casual Suit you need  3.90 of Blue Thin Wool
# 	Clothes.material_qty_total =  25.5
# 	Coat_material_qty_total =  17.9
# 	Suit_material_qty_total =   7.6
#
# Process finished with exit code 0

