class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def on_x_axis(self):
        return self.y == 0

    def distance_from(self, point):
        import math
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def in_unit_circle(self):
        return self.x ** 2 + self.y ** 2 <= 1

    def get_midpoint_to(self, point):
        x_diff = self.x - point.x
        y_diff = self.y - point.y
        return Point(self.x + x_diff / 2, self.y + y_diff / 2)


point = Point(5.0, 1.2)
print(point)

point2 = Point(1.4, 6.8)
print(point2.in_unit_circle())

print(point.distance_from(point2))
print(point.get_midpoint_to(point2))