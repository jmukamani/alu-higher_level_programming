#!/usr/bin/python3
"""This module represents an object(Python data structures)."""
import json


def from_json_string(my_str):
    """Returns an object(Python data structure) represented by JSON string
    """
    return json.loads(my_str)
