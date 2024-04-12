#!/usr/bin/python3

class Square:
    """
    This class represents a square where width is equal to height.
    """
    size = 0  # Unique attribute for both width and height

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key in {"size", "width", "height"}:  # Accept width or height keywords for compatibility
                self.size = value

    def area_of_my_square(self):
        """
        Calculate the area of the square.
        """
        return self.size * self.size

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of the square.
        """
        return 4 * self.size

    def __str__(self):
        return "{}/{}".format(self.size, self.size)

if __name__ == "__main__":
    s = Square(size=12)  # Create a square with size 12
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
