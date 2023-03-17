#!/usr/bin/python3
"""Represents a square."""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Iniatializes a new instance of the class square with given size.
            The size of the square defaults to 0.
         """
        self.__size = size

    def area(self):
        """Returns area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for __size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the __size attribute.Raises TypeError or ValueError.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __le__(self, other):
        """Compare square."""
        return self.size <= other.size

    def __eq__(self, other):
        """Compare square if is equal to another."""
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is nor equal to another."""
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another."""
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another."""
        return self.size > other.size
