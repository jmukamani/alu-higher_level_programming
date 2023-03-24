#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Defines a class BaseGeometry."""

    def area(self):
        """Raise Exception message."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer."""
        self.__value = value
        self.__name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
