#!/usr/bin/python3
"""This module represents a square"""


class Square:
    """This defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize an insatnce of Square with size and position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size o the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get or set position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """setter function for position attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # character"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """Define print representation of a square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
