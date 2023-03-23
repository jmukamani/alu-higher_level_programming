#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    def area(self):
        """Raise Exception message."""

        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates a value as an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueEror("{} mustt be greater than 0".format(name))
