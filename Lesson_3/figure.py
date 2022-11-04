"""
Урок 3. Принципы SOLID

Написать любом языке программирования, в которой идёт со следующими геометрическими фигурами:
1. Треугольник
2. Квадрат
3. Прямоугольник.
4. Круг
В программе имеется массив фигур, с которым можно сделать следующие операции:
1. Добавить новую фигуру
2. Посчитать периметр у всех фигур
3. Посчитать площадь у всех фигур
Для фигуры использовать базовый абстрактный класс фигуры, у которого есть методы посчитать
периметр и посчитать площадь фигуры. Массив фигур в программе должен быть представлен как
массив объектов этого базового класса. Массив фигур должен создаваться и вся работа с ним
идёт внутри main. При создании фигур необходимо осуществлять проверку входных данных на
возможность создания данной фигуры и в случае ошибки выдавать соответствующие сообщения.
"""

from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):
    @abstractmethod
    def func_square(self):
        pass

    def func_perimeter(self):
        pass

    def func_circ_length(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func_square(self):
        return self.a * self.b

    def func_perimeter(self):
        return 2 * (self.a + self.b)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c) / 2

    def func_square(self):
        return '%.2f' % ((self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5)

    def func_perimeter(self):
        return '%.2f' % (self.a + self.b + self.c)


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self.pi = 3.14159

    def func_square(self):
        return '%.2f' % (self.pi * self.r ** 2)

    def func_circ_length(self):
        return '%.2f' % (2 * self.pi * self.r)


if __name__ == "__main__":
    sqr = Rectangle(5, 5)
    print(sqr.func_square())
    print(sqr.func_perimeter())
    print(sqr.func_perimeter())

    rct = Rectangle(5, 6)
    print(rct.func_square())
    print(rct.func_perimeter())

    trn = Triangle(5, 5, 5)
    print(trn.func_square())
    print(trn.func_perimeter())

    crc = Circle(5)
    print(crc.func_square())
    print(crc.func_circ_length())
    print(crc.func_perimeter())
