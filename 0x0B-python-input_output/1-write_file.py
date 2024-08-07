#!/usr/bin/python3
"""
This module defines a function that writes a string to a
text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to
        an empty string. text (str): The string to write to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as w_file:
        char_count = w_file.write(text)
    return (char_count)
