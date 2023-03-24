#!/usr/bin/python3
"""Represents a function that creates an Object from JSON file."""
import json


def load_from_json_file(filename):
    """Create am object from JSON file."""
    with open(filename) as f:
        return json.load(f)
