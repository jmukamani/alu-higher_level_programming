#!/usr/bin/python3
"""This module represents a rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a class square"""

    def __init__(self, size):
        """Iniatialize a new square."""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns str() representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__sizeP
