#!/usr/bin/python3
"""This module represents a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square with given size.
        Size of the square defaults to 0.
        """
        self.__size = size

    def area(self):
         """Returns the are of the square."""
         return self.__size ** 2

    @property
    def size(self):
         """Getter method for the __size attribute."""
         return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the __size attribute.
        Raises TypeError or ValueError.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square to the console using # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
