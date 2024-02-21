import math
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2 * math.pi
    
Stiv = Square(4)
print(Stiv.area())

Alex = Rectangle(3, 5)
print(Alex.area())

Shar = Circle(5)
print(Shar.area())
