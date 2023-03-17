#!/usr/bin/python3
"""Represents a Bytecode."""


import math

class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initialize magic class."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area of circle"""
        return (self.radius ** 2 * math.pi)

    def circumferemce(self):
        """Calculates circumference of circle."""
        return (2 * math.pi * self.__radius)
