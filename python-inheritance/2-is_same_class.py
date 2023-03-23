#!/usr/bin/python3
""" Check if object is exactly an instance of specified class."""


def is_same_class(obj, a_class):
    """Returns true if object is an instance of a_class"""
    return type(obj) is a_class
