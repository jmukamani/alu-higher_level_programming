#!/usr/bin/python3
"""Checks if object is an instance of class that inherited
from specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of class
    inherited from specified class, otherwise return False
    """

    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
