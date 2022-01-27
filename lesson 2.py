# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# my_list = [None, 3.5, 100, 'stroka', 11,"%%", -5]
#
# for elem in range(len(my_list)):
#     print(type(my_list[elem]))


# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

# a = int(input("Введите количество элементов списка: "))
# my_list = []
# i = 0
# el = 0
# while i < a:
#     my_list.append(input("Введите значение списка: "))
#     i += 1
#
# for elem in range(int(len(my_list) / 2)):
#     my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
#     el += 2
# print(my_list)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# # Напишите решения через list и dict.

# seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
# seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
# month = int(input("Введите месяц по номеру: "))
# if month ==1 or month == 12 or month == 2:
#         print(seasons_dict.get(1))
#         print(seasons_list[0])
# elif month == 3 or month == 4 or month == 5:
#     print(seasons_dict.get(2))
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
#     print(seasons_list[2])
#
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
#     print(seasons_list[3])
# else:
#     print("Не верный месяц :)")


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
#
# stroka = input("введите строку: ")
# slowo = []
# num = 1
# for el in range(stroka.count(' ') + 1):
#     slowo = stroka.split()
#     if len(str(slowo)) <= 10:
#         print(f" {num} {slowo [el]}")
#         num += 1
#     else:
#         print(f" {num} {slowo [el] [0:10]}")
#         num += 1


# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
number = int(input("Введите число (для выхода введите: 0): "))
while number != 0:
    for el in range(len(my_list)):
        if my_list[el] == number:
            my_list.insert(el + 1, number)
            break
        elif my_list[0] < number:
            my_list.insert(0, number)
        elif my_list[-1] > number:
            my_list.append(number)
        elif my_list[el] > number and my_list[el + 1] < number:
            my_list.insert(el + 1, number)
    print(f"текущий список - {my_list}")
    number = int(input("Введите число: "))
