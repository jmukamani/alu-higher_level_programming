#!/usr/bin/python3
"""Represents class Rectangle tha inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new instance of Rectangle."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
