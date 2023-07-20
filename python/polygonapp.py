# polygon 

# Goal: “Create class and sub-class objects which represent different geometrical shapes, such as Rectangles and Squares”
# objects should have methods to display area and perimeter
import math

class Shape:

    def __init__(self, name, length, height):
        self.name = name
        self.length = length
        self.height = height

    def area(self):
        area = float(self.length * self.height)
        return area
    
    def perimeter(self):
        perimeter = float(self.length * 2 + self.height * 2)
        return perimeter
    
class Circle(Shape):
    def __init__(self, name, radius, length, height):
        super().__init__(name, length, height)
        self.radius = radius
        self.lenght = length
        self.height = height
    def area(self):
        area = math.pi * self.radius ** 2
        return area
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
square = Shape("square", 20, 20)
rectangle = Shape("rectangle", 10, 20)
circle = Circle("circle", 10, 0, 0)


# testing 
# print(square.perimeter())
# print(rectangle.perimeter())
# print(square.area())
# print(rectangle.area())
# print(circle.area())
# print(circle.perimeter())
