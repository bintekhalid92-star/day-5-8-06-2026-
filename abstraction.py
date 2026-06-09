from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        print("\nArea of Square:", self.side * self.side)


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)


side = int(input(print("enter the side : ")))
square = Square(side)
#square.area()

length = int(input(print("enter the length of rectangle : ")))
width = int(input(print("enter the width of the rectangle : ")))
rectangle = Rectangle(length,width)
square.area()
rectangle.area()