#!/usr/bin/python3
"""Represents a class square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a  class square."""

    def __init__(self, size):
        """Inialize  a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
