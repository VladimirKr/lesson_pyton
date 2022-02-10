# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

# from time import sleep
#
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается \n '
#                   f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(5)
#             i += 1
#
# TrafficLight = TrafficLight()
# TrafficLight.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

# class Road:
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#     def mass(self):
#         return self._length * self._width
#
# class MassCount(Road):
#     def __init__(self, _length, _width, weight, thickness):
#         super().__init__(_length, _width)
#         self.weight = weight
#         self.thickness = thickness
#         self.volume = (self.weight * self.thickness)/1000
#
#     def mass(self):
#         print(f'Для асфальтирования догоги длиной {self._length} и шириной {self._width} метров, \n'
#               f'потребуется {int(self.volume * Road.mass(self))} тонн асфальта')
#
# r = MassCount(5000, 20, 25, 5)
# r.mass()


# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#
#
#
# a = Position('Федор', 'Смирнов', 'Системный администратор', 70000, 25000)
# print(a.get_full_name())
# print(a.position)
# print(a.get_total_income())


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

# class Car:
#     # atributes
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     # methods
#     def go(self):
#         return f'{self.name} поехал'
#
#     def stop(self):
#         return f'{self.name} остановился'
#
#     def turn_right(self):
#         return f'{self.name} повернул направо'
#
#     def turn_left(self):
#         return f'{self.name} повернул налево'
#
#     def show_speed(self):
#         return f'Текушая скорость {self.name} составляет {self.speed}'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Текущая скорость для town car {self.name} составляет {self.speed}')
#
#         if self.speed > 40:
#             return f'Скорость {self.name} выше разрешенной для town car'
#         else:
#             return f'Скорость {self.name} является разрешенной для town car'
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.name} : {self.speed}')
#
#         if self.speed > 60:
#             return f'У автомобиля {self.name} превышение скорости'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} из полиции'
#         else:
#             return f'{self.name} не из полиции'
#
#
# BMW = SportCar(100, 'Синий', 'BMW', False)
# Lada = TownCar(50, 'Белый', 'Lada', False)
# Renault = WorkCar(70, 'Красный', 'Renault', False)
# ford = PoliceCar(110, 'Черный',  'Ford', True)
# print(Renault.turn_right())
# print(f'Если {Lada.turn_right()}, то {BMW.stop()}')
# print(f'Автомобиль {Renault.name} имеет {Renault.color} цвет')
# print(f'Автомобиль {BMW.name} из полиции? {BMW.is_police}')
# print(f'Атомобиль {Renault.name} из полиции? {Renault.is_police}')
# print(BMW.show_speed())
# print(Lada.show_speed())
# print(ford.police())
# print(ford.show_speed())

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
