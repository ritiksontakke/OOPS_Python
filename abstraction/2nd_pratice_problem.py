from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete class: Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Concrete class: Rectangle
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Example usage
c = Circle(7)
print("Circle Area:", round(c.area(), 2))        # ~153.94
print("Circle Perimeter:", round(c.perimeter(), 2))  # ~43.98

r = Rectangle(4, 6)
print("Rectangle Area:", r.area())              # 24
print("Rectangle Perimeter:", r.perimeter())    # 20