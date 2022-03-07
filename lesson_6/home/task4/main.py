# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'машина "{self.name}" поехала')

    def stop(self):
        print(f'машина "{self.name}" остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'машина "{self.name}" повернула {self.direction}')

class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'машина "{self.name}" едет со скоростью {self.speed} км/ч. Внимание!!! Превышение скорости. Пожалуйста, сбавьте до 60 км/ч')
        else:
            print(f'машина "{self.name}" едет со скоростью {self.speed} км/ч.')


class SportCar(Car):
    def show_speed(self):
        print(f'машина "{self.name}" едет со скоростью {self.speed} км/ч.')


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'машина "{self.name}" едет со скоростью {self.speed} км/ч. Внимание!!! Превышение скорости. Пожалуйста, сбавьте до 40 км/ч')
        else:
            print(f'машина "{self.name}" едет со скоростью {self.speed} км/ч.')


class PoliceCar(Car):
    def show_speed(self):
        print(f'машина "{self.name}" едет со скоростью {self.speed} км/ч.')

    def police(self):
        if self.is_police is True:
           print(f'машина "{self.name}" - полицейская машина')


priora = TownCar('80', 'white', 'Priora', False)
mclaren = SportCar('280', 'black-blue', 'McLaren', False)
vesta_police = PoliceCar('100', 'white-blue', 'Веста', True)
gazelle = WorkCar('100', 'orange', 'Газель', True)

priora.go()
priora.stop()
gazelle.turn('налево')
priora.turn('направо')
gazelle.show_speed()
priora.show_speed()
mclaren.turn('направо')
mclaren.show_speed()
vesta_police.police()


