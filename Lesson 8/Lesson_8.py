# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


# class Data:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#         for i in day_month_year.split():
#             if i != '-':
#                 my_date.append(i)
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2050 >= year >= 0:
#                     return f'Всё верно'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
#
# today = Data('11 - 1 - 2001')
# print(today)
# print(Data.valid(13, 11, 2022))
# print(today.valid(1, 12, 2011))
# print(Data.extract('11 - 11 - 2021'))
# print(today.extract('11 - 11 - 2020'))
# print(Data.valid(1, 11, 2000))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

# class DivisionByNull:
#     def __init__(self, divider, denominator):
#         self.divider = divider
#         self.denominator = denominator
#
#     @staticmethod
#     def divide_by_null(divider, denominator):
#         try:
#             return (divider / denominator)
#         except:
#             return (f"Нельзя делить на нуль.")
#
#
# div = DivisionByNull(10, 2)
# print(DivisionByNull.divide_by_null(10, 0))
# print(DivisionByNull.divide_by_null(10, 0.1))
# print(div.divide_by_null(3, 0))


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст
# (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.


# class NotNumberError(Exception):
#     def __init__(self, text):
#         self.text = text
#
#     def __str__(self):
#         return self.text
#
# my_list = []
#
# while True:
#     user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")
#
#     if user_input == "stop":
#         break
#
#     try:
#         if not user_input.isdigit():
#             raise NotNumberError(f"'{user_input}' не число")
#
#         my_list.append(int(user_input))
#     except NotNumberError as e:
#         print(e)
#
# print(my_list)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from datetime import datetime

class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
# внесение в словарь название оборудования, серийный номер и время передачи на склад
        t = datetime.now()
        self.lists.update({equipment.serial_number:[equipment.title, self,t]})
        print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title+' ,серийный номер - '+ str(equipment.serial_number)+', Дата:'
              + str(t.day)+'.'+str(t.month)+'.'+str(t.year))


    def give_to_depot(self, equipment, other):
# передача оборудование на другой склад или подразделение
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title,other, t]})
        print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
            equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)


    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))




class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number, print_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title,serial_number,resolution):
        Office_equipment.__init__(self,title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.resolution)

class Copier(Office_equipment):
    def __init__(self, title,serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.addit)


store1 = Depot('Основной склад')
store2 = Depot('Склад магазина')
a = Printer('HP',345678,100)
b = Scanner('Epson',123456,4000)
c = Copier('Brother',987654, 50)
d = Printer('HP',245678,200)

print(a)
print(b)
print(c)

store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)
store1.take_to_depot(d)

store1.give_to_depot(a,store2)

store1.list_equipments()
store2.list_equipments()


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


# class ComplexNum:
#
#     def __init__(self, re, im):
#         self.re = re
#         self.im = im
#
#     def __str__(self):
#         return f'{self.re} + {self.im}i'
#
#     def __add__(self, other):
#         return f'Результат сложения комплексных чисел: ' \
#                f'{ComplexNum(self.re + other.re, self.im + other.im)}'
#
#     def __mul__(self, other):
#         return f'Результат умножения комплексных чисел: ' \
#                f'{ComplexNum(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)}'
#
#
# mc1 = ComplexNum(1, 4)
# mc2 = ComplexNum(2, 4)
#
# print(mc1 * mc2)
# print(mc1 + mc2)
