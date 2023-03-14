#!/usr/bin/python3
"""Define a class square"""


class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """Inialize a new square.
        Args:
            size (init): size of new square.
        """

        if not isinstance(size, init):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
