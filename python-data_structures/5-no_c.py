#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all occurrences of the characters "c" and "C" from given string.
    Args:
        my_string (str): The input string.
    Returns:
        str: The modified string with all "c" and "C" characters removed.
    """
    new_string = ""
    for char in my_string:
        if char not in ("c", "C"):
            new_string += char
    return new_string
