from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def get_area(self):
        return self.shape.area()


circle = Circle(5)
rectangle = Rectangle(4, 6)

circle_area_calculator = AreaCalculator(circle)
rectangle_area_calculator = AreaCalculator(rectangle)

print(f"Circle area: {circle_area_calculator.get_area()}")
print(f"Rectangle area: {rectangle_area_calculator.get_area()}")
