#!/usr/bin/python3
""" Defines a Square class. """


class Square:
    """ Represents a geometric square with width and height attributes. """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new Square instance with given dimensions. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Computes and returns the area of the square. """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Calculates and returns the perimeter of the square. """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns the string representation of the square dimensions. """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    # Execution block to test Square functionality:
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
