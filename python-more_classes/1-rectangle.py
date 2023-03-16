#!/usr/bin/python3
"""This module represents a rectangle."""


class Rectangle:
    """This module defines a class attribute Rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """Getter method for the width."""
    def width(self):
        return self.__width

    @width.setter
    """Get/set width of the rectangle."""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """Getter method for the height."""
    def height(self):
        return self.__height

    @height.setter
    """Get/set height of the rectangle."""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
