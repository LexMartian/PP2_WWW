class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point is at ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return self.x , self.y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
Atyrau = Point(4, 5)
print(Atyrau.show())
Atyrau.move(1, 1)
print(Atyrau.show())

other = Point(1, 1)
distance = Atyrau.dist(other)
print(f"Distance from Atyrau to other_point: {distance:.3f}")