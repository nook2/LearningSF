class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y


rectangle = Rectangle(7, 9)

print(rectangle.get_area())
