#!/usr/bin/python3
"""Represents a python class to JSON function."""


def class_to_json(obj):
    """Return dictionary representation of data structure."""
    return obj.__dict__
