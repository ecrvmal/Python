# 4. Реализуйте класс Car (машина).
# Техническое задание:
#
# атрибуты: speed, color, name, 'is_police': (булево). speed - текущая скорость машины.
# Внимательно по отношению выбора атрибут класса/экземпляра.
#
# методы: go, stop, turn(direction), которые должны сообщать(выводить на экран),
# что машина поехала, остановилась, повернула (куда). turn(direction) - метод, принимающий параметр: направление поворота.
# Сами определите как вызов этих методов меняет скорость машины. На ваше усмотрение.
#
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# добавьте в базовый класс Car метод show_speed, который должен показывать текущую скорость автомобиля
# для классов TownCar и WorkCar переопределите метод 'show_speed'.
# При значении скорости машины свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Ограничения на скорость - очевидно данные. Где их нужно хранить?
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    speed_increment = 20
    directions = ["North", "East", "South", "West"]


    def __init__(self, name, speed = 0, color="black",  is_police=False, direction_index =0):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.direction_index = direction_index
        self.direction = self.directions[direction_index]

    def show_speed(self):
        print(f'Car {self.name} speed = {self.speed}')
        return self.speed

    def go(self):
        self.speed += self.speed_increment
        print(f'Car {self.name} speed = {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Car {self.name} stopped')

    def show_direction(self):
        if self.speed != 0:
            print(f'Car {self.name} drives to {self.direction}')
        else:
            print(f'Car {self.name} haven"t speed')
        pass

    def turn(self, turn_direction):
        if self.speed > 30 :
            self.speed -= (self.speed - 30)/2
        if self.speed !=0:
            if turn_direction == 'left' and self.direction_index != 0:
                self.direction_index -= 1
            if turn_direction == 'left' and  self.direction_index == 0:
                self.direction_index = len(self.directions)-1
            if  turn_direction == 'right' and self.direction_index != len(self.directions):
                self.direction_index += 1
            if  turn_direction == 'right' and  self.direction_index == len(self.directions):
                self.direction_index = 0
            print(f'Car {self.name} turned {turn_direction} and goes to ',
                        f'{self.directions[self.direction_index]} with speed {self.speed}')
        else :
            print(f'Car {self.name} haven"t speed')


class TownCar(Car):
    def __init__(self, name , speed_limit = 60):
        super().__init__(name )
        self.speed_limit = speed_limit
        print(f'\tCreated TownCar :  {self.name}')

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Car {self.name} speed = {self.speed} , Speed Limit exceed')
        else:
            print(f'Car {self.name} speed = {self.speed}')
        return self.speed

class SportCar(Car):
    def __init__( self, name, speed_limit=300 ):
        super().__init__(name)
        print(f'\tCreated SportCar: {self.name}')
        self.speed_increment = 40

class WorkCar(Car):
    def __init__(self, name ,speed_limit=40 ):
        super().__init__(name  )
        print(f'\tCreated WorkCar : {self.name}')
        self.speed_limit = speed_limit

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Car {self.name} speed = {self.speed} , Speed Limit exceed')
        else:
            print(f'Car {self.name} speed = {self.speed}')

class PoliceCar(Car):
    def __init__(self, name, is_police=True ):
        super().__init__(name, is_police)
        print(f'\tCreated PoliceCar : {self.name}')

car_sp = SportCar('Lamborghini_Uracan')
car_tn = TownCar('VW Passat')
car_pl = PoliceCar('Chevrolet_Blazer')
car_wk = WorkCar('MAN')


car_sp.show_speed()
car_sp.show_direction()

car_sp.go()
car_sp.go()
car_sp.go()
car_sp.go()
car_sp.go()
car_sp.show_speed()
car_sp.show_direction()
car_sp.turn('left')
car_sp.turn('left')
car_sp.turn('left')
car_sp.turn('left')
car_sp.turn('right')
car_sp.turn('right')
car_sp.turn('right')
car_sp.turn('right')
car_sp.stop()
car_sp.show_direction()
car_sp.show_speed()

car_tn.go()
car_tn.go()
car_tn.go()
car_tn.go()
car_tn.go()
car_tn.show_speed()

# 	Created SportCar: Lamborghini_Uracan
# 	Created TownCar :  VW Passat
# 	Created PoliceCar : Chevrolet_Blazer
# Car Lamborghini_Uracan speed = 0
# Car Lamborghini_Uracan haven"t speed
# Car Lamborghini_Uracan speed = 10
# Car Lamborghini_Uracan speed = 20
# Car Lamborghini_Uracan speed = 30
# Car Lamborghini_Uracan speed = 40
# Car Lamborghini_Uracan speed = 50
# Car Lamborghini_Uracan speed = 50
# Car Lamborghini_Uracan drives to North
# Car Lamborghini_Uracan turned left and goes to  West with speed 40.0
# Car Lamborghini_Uracan turned left and goes to  South with speed 35.0
# Car Lamborghini_Uracan turned left and goes to  East with speed 32.5
# Car Lamborghini_Uracan turned left and goes to  West with speed 31.25
# Car Lamborghini_Uracan turned right and goes to  North with speed 30.625
# Car Lamborghini_Uracan turned right and goes to  East with speed 30.3125
# Car Lamborghini_Uracan turned right and goes to  South with speed 30.15625
# Car Lamborghini_Uracan turned right and goes to  West with speed 30.078125
# Car Lamborghini_Uracan stopped
# Car Lamborghini_Uracan haven"t speed
# Car Lamborghini_Uracan speed = 0
#
# Process finished with exit code 0

