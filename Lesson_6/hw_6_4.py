import random


class Car:
    going = {'forward': "прямо", 'backwards': "назад", 'right': "направо", 'left': "налево"}
    speed_limit = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f"{self.name} поехал!!!")
        return self.speed

    def stop(self):
        if self.speed == 0:
            print(f"{self.name}  остановился.")
        return True

    def turn(self, direction):
        vector = self.going.get(direction)
        return vector

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            self.speed_limit = True
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            self.speed_limit = True
        return self.speed


class PoliceCar(Car):
    pass


a = TownCar(55, 'white', 'Volkswagen')
b = SportCar(100, 'red', 'Porsche')
c = WorkCar(45, 'grey', 'Ford')
d = PoliceCar(90, 'black-white', 'BMW', True)
direct = ('forward', 'backwards', 'left', 'right')
list_car = [a, b, c, d]
for elem in list_car:
    if elem.is_police:
        print(f"Создан полицейский автомобиль - {elem.name}, цвет - {elem.color}")
    else:
        print(f"Создан автомобиль - {elem.name}, цвет - {elem.color}")
    elem.go()
    direction = random.choice(direct)
    print(f"Автомобиль движется - {elem.turn(direction)} со скоростью - {elem.show_speed()}.", end='')
    if elem.speed_limit:
        print(" Превышаете!!!")
    else:
        print('')
    elem.speed = 0
    elem.stop()
