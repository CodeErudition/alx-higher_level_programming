#!/usr/bin/python3
"""
This module defines a function that appends a string at the end of a
text file (UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to
        an empty string. text (str): The string to append to the end of
        the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        char_count = a_file.write(text)
    return (char_count)
