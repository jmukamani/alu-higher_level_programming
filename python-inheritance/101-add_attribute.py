#!/usr/bin/python3
"""Defines a function that adds attributes to object"""


def add_attributr(obj, att, value):
    """Add new attribute to the object if possible."""
    if hasattr(obj, "__dict__"):
        obj.__setattr__(name, value)
    elif (hasattr(type(obj), '__slots__' and name in type(obj).__slots__)
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
