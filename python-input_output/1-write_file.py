#!/usr/bin/python3
"""Represents a function that writes string to a text file"""


def write_file(filename="", text=""):
    """Write string to UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
            return f.write(text)
