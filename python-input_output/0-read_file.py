#!/usr/bin/python3
"""Represents function that reads a file"""


def read_file(filename=""):
    """Print the contents of UTF8 file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
