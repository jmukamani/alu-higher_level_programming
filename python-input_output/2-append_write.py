#!/usr/bin/python3
"""Represents a function that appends a string."""


def append_write(filename="", text=""):
    """Defines function that appends a string at the end of text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
