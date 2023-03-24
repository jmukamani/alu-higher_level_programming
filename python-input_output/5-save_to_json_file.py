#!/usr/bin/python3
"""Represents Object to atext file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to txt file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
