#!/usr/bin/python3
"""Represents a class student."""


class Student:
    """A class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation of the strudent."""
        return self.__dict__
