#!/usr/bin/python3
"""Defines a class MyInt that inherits from Int."""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Overide == operator with != behaviour"""
        return self.real != value

    def __ne__(self, value):
        """Overide != operator with == behaniour"""
        return self.real == value
