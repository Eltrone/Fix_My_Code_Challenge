#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return 4 * self.size

    def __str__(self):
        return "{}/{}".format(self.size, self.size)

if __name__ == "__main__":
    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
