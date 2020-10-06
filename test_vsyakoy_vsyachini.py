# import sys
# list_anything = [1, 23, 4, 54.2, 7]
#
# for number, item in enumerate(list_anything):
#     print(number, "and", item)
# array = [1, 6, 2, 3, 4]
# print(sorted(array, key = lambda x: x%2==1))
# print(list(map(lambda number: number**2, array)))
# print(list(filter(lambda number: number%2==0, array)))

# print(sys.platform)

# str_b = b'stroka'
# print(str_b[1])
# str_string = str_b.decode("ascii")
# print(str_string)
# str_b = str_string.encode("ascii")
# print(str_b)

# import json
# import pickle
# person = {"name": "Макс", "phones":[123,324]}
# json_str = json.dumps(person) # сохранит в строку словарь
# pickle_str = pickle.dumps(person) # сохранит в байты словарь
# print(json_str)
# print(type(pickle_str))
# new_person = pickle.loads(pickle_str)
# print(new_person)
# print("2" if 2 > 3 else "1")
# import calendar, datetime
# curr_date_tuple = datetime.datetime.now().timetuple()
# curr_month_len = calendar.monthrange(curr_date_tuple[0], curr_date_tuple[1])[1]
# print(curr_month_len)
# print(datetime.datetime.now().timetuple()[0])
# print(datetime.datetime.now().timetuple())

# print(calendar.itermonthdates(datetime.date[0], datetime.date[1])[-1])


# a = calendar.monthrange(2014, 2)

# print(calendar.calendar.itermonthdates(datetime.datetime.now().timetuple(), datetime.datetime.now().timetuple()))
"""
Define working directories
"""


# import os
#
# GUIDE_NAMES = [
#     {'name': "Lexys LOTD", 'profile': "Lexy's LOTD SE"},
#     {'name': "LOTD Plus", 'profile': "LOTD Plus"},
#     {'name': "LOTD Plus Plus", 'profile': "LOTD Plus Plus"},
#     {'name': "skipping selection", 'profile': "skip"},
#
# ]
# class Person:  # создание класса
#     counter = 0
#
#     def __init__(self, name, age):  # Первая функция, которая автоматически вызовется
#         self.name = name  # self - сам объект, который мы создаём. в данном случае p1
#         self.age = age  # если
#         Person.counter += 1
#
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#
#
# p1 = Person("John", 36)
# p1.myfunc()
# p2 = Person("Alex", 17)
# print(Person.counter)
# del p1.name
# p1.name = 'Jim'
# p1.myfunc()
# del Person.counter
# p3 = Person('Alfred', 16)

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# x = Person("John", "Doe")
# x.printname()
#
#
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         # Person.__init__(self, fname, lname)
#         super().__init__(fname, lname)  # можно использовать super вместо Person, можно не использовать self для род. инита
#         # self.firstname = lname
#         # self.lastname = fname
#         self.graduationyear = year
#
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#
#
# x = Student("Mike", "Olsen", 2019)
# x.printname()
# x.welcome()
# import sys
# import numpy
#
# arr = numpy.array([1, 2, 3, 4, 5])
# arr_list = [1, 2, 3, 4, 5]
#
# print(arr)
# print(sys.getsizeof(arr))
# print(sys.getsizeof(arr_list))
# if 'asd' < 'aasda':
#     print('sdfafs')
#
# def iterate(begin, end):
#     if begin == end:
#         return f"{end}"
#
#     if begin > end:
#         return f"{begin}, {iterate(begin-1, end)}"
#
#     if begin < end:
#         return f"{begin}, {iterate(begin+1, end)}"
#
#
# print(iterate(20, 10))
# import sys
#
#
# sys.setrecursionlimit(3000)
#
#
# def akk(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return akk(m-1, 1)
#     return akk(m-1, akk(m, n-1))
#
#
# print(akk(1, 1))
# import re
# password = input("Enter string to test: ")
# if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
#     print('eee')
# else:
#     print('nnnn')

# gen = (i**2 for i in range(5))
# # lst = [i**2 for i in range(5)]
# print(list(gen))
# print(list(gen))
#


# class Person:  # создание класса
#     counter = 0  # общеклассовая переменная, считает, сколько всего объектов было создано
#
#     def __init__(self, name, age):  # Первая функция, которая автоматически вызовется
#         self.name = name  # self - сам объект, который мы создаём. При создании p1 будет p1
#         self.age = age
#         Person.counter += 1  # обращение к переменной класса, добавляет 1
#
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#
#
# class Student(Person):  # создание класса
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)  # можно использовать Person вместо super, но нужно добавить self для род. инита
#         self.grade = grade
#
#     def wellcome(self):
#         print(f"Welcome, {self.name}, to the {self.grade}th grade")
#
#     # Если функцю ниже не объявлять, то вызовется родительская функция.
#     def myfunc(self):  # тут можно переназначить родительскую функцию, а можно не трогать
#         Person.myfunc(self)  # вызов родительской функции, можно использовать super() вместо Person и не передавать self
#         print(f"Это студент, надо добавить класс: {self.grade}")  # новая строчка
#
#
# x = Student("Mike", 12, 5)
# x.wellcome()
# x.myfunc()
#
# y = Student("Mike", 12, 5)
# print(getattr(Student, 'counter', '100'))
# import random
#
# lst = [i for i in range(1,11)]
# print(lst)
#
# a = sum(lst[:4])
# b = sum(lst[3:6])
# c = sum(lst[5:9])
# d = sum(lst[8:])+lst[0]
#
# print(a, b, c, d)
#
# start = 0
# while True:
#     random.shuffle(lst)
#     a = sum(lst[:4])
#     b = sum(lst[3:6])
#     c = sum(lst[5:9])
#     d = sum(lst[8:]) + lst[0]
#
#     if a == b == c == d:
#         break
#     start += 1
#
# print(a, b, c, d)
# print(lst)

# lst = [1, 2, 3, 4]
# lst = [i for i in range(1,11)]
#
# def variate(temp_lst: list, stage=-1):
#
#     if len(temp_lst) == 2:
#         print(lst)
#         lst[-2], lst[-1] = lst[-1], lst[-2]
#         print(lst)
#         lst[-2], lst[-1] = lst[-1], lst[-2]
#         return
#
#     stage += 1
#     for i in range(len(temp_lst)):
#         lst[stage], lst[stage+i] = lst[stage+i], lst[stage]
#         variate(temp_lst[1:], stage)
#         lst[stage + i], lst[stage] = lst[stage], lst[stage + i]
#
#
# variate(lst)
#
# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         # print(count)
#         return count
#     return inner
#
#
# a = counter()
# a()  # count = 1
# a()  # count = 2
# a()  # count = 3
# a()  # count = 4
# a()  # count = 5
# b = counter()
# b()  # new count = 1
# c = a()  # count = 6
# print(c)
# print(type(c))  # <class 'int'>
# print(type(a))  # <class 'function'>

# class Square:
#     def __init__(self, side):
#         self.__side = side
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def area(self):
#         if not self.__area:
#             print('calculate')
#             self.__area = self.__side**2
#         return self.__area
#
#
# a = Square(2)
# print(a.area)
# print(a.area)
# a.side = 5
# print(a.area)
# print(a.area)


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами коллекции')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Индекс за границами коллекции')

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return SimpleIterator(self)

    # def __iter__(self):                       # логичнее так, т.к. генератор является итератором
    #     for idx in range(len(self.values)):
    #         yield self.values[idx]


class SimpleIterator:
    def __init__(self, example):
        self.limit = len(example)
        self.example = example
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            result = self.example[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration


# v1 = Vector(1, 2, 7, 10)
# # print(v1[0])
# for v in v1:
#     print(v)

def test(test_func, right_func, *args):
    for id, value in enumerate(args):
        test_val, result = test_func(value), right_func(value)
        if test_val == result:
            print(f"test {id} OK")
        else:
            print(f"test {id} occurred. result must be {result}, tested function shows {test_val}")


def danil_func():
    number = int(input("Введите число от 1 до 10  "))
    while not (1 <= number <= 10):
        number = int(input("Вы совершили ошибку. Пожалуйста, введите число от 1 до 10  "))
    print("Вот ваше число: ", number ** 2)
    # todo переделать, чтоб тестилось


# danil_func()

def get_some_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f.readlines()[3::8]:
            print(line, end="")


get_some_text('input_text')