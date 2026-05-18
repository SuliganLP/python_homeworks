# Фигуры и площади
# создайте абстрактный класс Shape.
# ● В классе должен быть метод area(), который возвращает площадь фигуры.
# ● Реализуйте два класса:
# ○ Circle, который принимает радиус.
# ○ Rectangle, который принимает ширину и высоту.

# Доработайте фигуры:
# ● Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
# ● Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение
# InvalidSizeError.

from abc import ABC, abstractmethod
from math import pi


class InvalidSizeError(Exception):
    pass


class Shape(ABC):
    @abstractmethod
    def area(self) -> int | float:
        pass


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    @property
    def radius(self) -> int | float:
        return self.__radius

    @radius.setter
    def radius(self, value: int | float) -> None:
        if value <= 0:
            raise InvalidSizeError("Radius must be positive")
        self.__radius = value

    def area(self) -> float:
        return round(pi * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> int | float:
        return self.__width

    @width.setter
    def width(self, value: int | float) -> None:
        if value <= 0:
            raise InvalidSizeError("Width must be positive")
        self.__width = value

    @property
    def height(self) -> int | float:
        return self.__height

    @height.setter
    def height(self, value: int | float) -> None:
        if value <= 0:
            raise InvalidSizeError("Height must be positive")
        self.__height = value

    def area(self) -> int | float:
        return self.width * self.height


circ = Circle(3)
print(circ.area())
rec = Rectangle(5, 3)
print(rec.area())
