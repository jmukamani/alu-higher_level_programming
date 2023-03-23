#!/usr/bin/python3
"""Checks if an object is an instance of class or an inheritated class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or the object is an instance of inheritated class.
    """

    return isinstance(obj, a_class)
