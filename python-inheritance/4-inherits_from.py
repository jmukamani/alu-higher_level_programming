#!/usr/bin/python3
"""Checks if object is an instance of class that inherited
specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of class
    inherited specified class, otherwise return False
    """

    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
