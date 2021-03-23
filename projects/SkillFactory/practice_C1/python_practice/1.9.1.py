class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_width(self):
        return self.a

    def get_height(self):
        return self.b

    def get_area(self):
        return str(self.a * self.b)

    def get_perimeter(self):
        return str(self.a*2 + self.b*2)




class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_radius(self):
        return self.r ** 2 * 3.14
