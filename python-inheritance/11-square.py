#!/usr/bin/python3
"""This module represents a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a class Square"""
    def __init__(self, size):
        super().integer_validatior("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns str() of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
