#!/usr/bin/python3
"""This is a module for a square"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        """construct a private instance attribute of size
        Args:
            size: Length of side of the square.
        """

        self.__size = size
