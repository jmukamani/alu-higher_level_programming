#!/usr/bin/python3
"""Represents a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents Rectacngle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new instance of Rectangle."""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """print() and str() representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
