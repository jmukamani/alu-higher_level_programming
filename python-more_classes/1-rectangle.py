#!/usr/bin/python3
"""This module represents a rectangle."""


class Rectangle:
    """This module defines a class attribute Rectangle."""
    
    def __init__(self, width=0, height=0):
        """Initialize an instance of the Rectangle with width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the attribute __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the __with attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the attribute __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the __height attributr."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
