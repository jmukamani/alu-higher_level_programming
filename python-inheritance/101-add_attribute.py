#!/usr/bin/python3
"""This module represents a function that adds attributes to object"""


def add_attributr(obj, att, value):
    """Add new attribute to the object if possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj att, value)
