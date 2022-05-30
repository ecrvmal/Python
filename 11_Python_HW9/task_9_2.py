# 2. Реализовать класс Road (дорога).
# Техническое задание:
#
# определить атрибуты: length (длина), width (ширина). Подумайте атрибуты чего?
# значения атрибутов должны передаваться при создании экземпляра класса
# атрибуты сделать защищёнными
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги
# метод возвращает массу асфальта в виде строки в требуемом формате (см примеры/тесты)
# формула 'длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна';
# проверить работу метода и вывести массу асфальта для 2-3 наборов параметров.
# Примеры/Тесты:
# '20 м*5000 м*25 кг*5 см = 12500 т'

class Road:
    asphalt_dencity =   2.5           #   Tonns per cubic meter
    asphalt_thickness = 0.05            #   asphalt_thickness is in meter

    def __init__(self, road_length=1000, road_width = 12 ):
        self._road_length = road_length
        self._road_width = road_width

    def asphalt_mass(self):
        result = self._road_length * self._road_width * Road.asphalt_dencity * Road.asphalt_thickness
        return f'{result:.0f}'

    def GetName(self):
        for i, j in globals().items():
            if j is self:
                return i

    def get_parameters(self):
        parameter_list = [
                        self.GetName(),
                        self._road_length,
                        self._road_width ,
                        self.asphalt_thickness,
                        self.asphalt_dencity ]
        return parameter_list

def mk_param_line(l1):
    return str(f"\n Road Param's : Name: '{l1[0]}', Length: {l1[1]}, Width: {l1[2]}, Asph.Thickns: {l1[3]}, Asph.Density: {l1[4]},   ")

test_road = Road(5000, 20)
print(f"{mk_param_line(test_road.get_parameters())}", end='')
print(f'Asphalt_mass = {test_road.asphalt_mass()} tonns')

country_road = Road()
print(f"{mk_param_line(country_road.get_parameters())}", end='')
print(f'Asphalt_mass = {country_road.asphalt_mass()} tonns')

m11_road = Road(684000, 22)
print(f"{mk_param_line(m11_road.get_parameters())}", end='')
print(f'Asphalt_mass = {m11_road.asphalt_mass()} tonns')


