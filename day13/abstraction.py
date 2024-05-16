# 추상화
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 4

class Triangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width * 8.5
