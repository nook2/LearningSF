class Rectangle:
    def __init__(self, a, b, width, height):
        self.a = a
        self.b = b
        self.width = width
        self.height = height

    def __str__(self):
        return f' a = {self.a}, b = {self.b}, width = {self.width}, height = {self.height}'


rectangle = Rectangle(5, 10, 50, 100)
print(rectangle)