#!/usr/bin/python3

class Square:
    """
    This class represents a square where width is equal to height,
    with a single attribute for size.
    """
    size  0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key in {"size", "width", "height"}:
                self.size = value

    def area_of_my_square(self):
        """
        Calculate the area of the square using the formula size * size.
        """
        return self.size * self.size

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of the square using the formula 4 * size.
        """
        return 4 * self.size

    def __str__(self):
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":
    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
