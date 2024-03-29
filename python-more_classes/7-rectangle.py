#!/usr/bin/python3
"""This module represents a rectangle."""


class Rectangle:
    """This defines a rectangle."""
    number_of_instances = 0
    """public class atrribute initialized to 0."""
    print_symbol = '#'
    """used as symbol for string representation."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        symbol = ""
        if self.width != 0 and self.height != 0:
            symbol += "\n".join(str(self.print_symbol) * self.width
                                for j in range(self.height))
        return symbol

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
