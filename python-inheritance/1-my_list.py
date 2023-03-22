#!/usr/bin/python3
"""Represents a class Mylist."""


class MyList(list):
    """Defines a subclass of List."""
    def __init__(self):
        """Initializes a new instance of object."""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
