# 1. Создать класс TrafficLight (светофор).
# Техническое задание:
#
# Хорошо подумайте какие из атрибутов являются атрибутами экземпляра, а какие класса.
# определить атрибут color (цвет) - приватный. Это текущий цвет светофора.
# Определить метод state (состояние), возвращающий текущий цвет в виде строки.
# определить метод running (запуск)
# в рамках метода реализовать переключение светофора в режимы(цвета): красный, жёлтый, зелёный.
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение.
# Подумайте о том как хранить продолжительности. В виде какой структуры и в качестве атрибута чего?
# переключение между режимами должно осуществляться как у реального светофора: красный, жёлтый, зелёный, жёлтый, красный и т.д.
# метод многократно меняет текущий цвет светофора в соответствии с продолжительностями в секундах и печатает текущий цвет с помощью state.
# Предусмотреть разумное ограничение на количество итераций.
# Проверить работу примера, создав экземпляр и вызвав метод running.
# Примечание:
#
# Для реализации задержек времени можно воспользоваться функцией sleep пакета time
# Циклическое переключение просто реализовать с помощью cycle пакета itertools
# Усложнение:
#
# Тайминги передаются при создании экземпляра светофора в виде трех чисел.
# Внутри конструктора их надо соединить в единую структуру с цветами, так, чтобы было максимально понятно и лаконично.
# Ограничение на количество итераций в методе running убрать.
# Прерывание работы светофора реализовать через нажатие Crtl-C (или stop в IDE) в процессе выполнения.
# Найти какое исключение при этом возникает. Обработать его и завершить программу с выводом диагностического сообщения.

import time


class Traffic_light():
    light_durations={'red': 7, 'yellow':2, 'green':7}
    colors = ['red', 'yellow', 'green']
    switch_direction = 1

    def __init__(self, color_index=0, switch_direction = 1):
        self.color_index = color_index
        self.__color = Traffic_light.colors[self.color_index]
        self.switch_direction = switch_direction

    def tl_state(self):
        return str(Traffic_light.colors[self.color_index])

    def tl_running(self):
        switch_direction = self.switch_direction    # создаю локальные переменные метода, для объекта, чтобы не обращаться к переменным Class
        colors = Traffic_light.colors
        durations = Traffic_light.light_durations
        for _ in range(20):
        # while True                            # для усложнения , для бесконечного цикла
            color = colors[self.color_index]         # создаю локальные переменные , для объекта, чтобы не обращаться к переменным Class
            duration = durations[color]
            print(self.tl_state())
            time.sleep(duration)
            if self.color_index == 0 : switch_direction = 1
            if self.color_index == len(Traffic_light.colors) -1 : switch_direction = -1
            self.color_index += switch_direction
            #print(self.tl_state())



tl1 = Traffic_light()
# print(tl1)
# print (tl1.color)
# print (tl1.switch_direction)
# print(Traffic_light.light_duration )
# print(Traffic_light.colors )
# print(Traffic_light.switch_direction)

try:
    tl1.tl_running()
except KeyboardInterrupt:
    print (' the prgramm interrupted by user ')
