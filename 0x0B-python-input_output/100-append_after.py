#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to
a file, after each line containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a
    specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line of
        the file.
        new_string (str): The string to insert after each line containing
        the search string.
    """
    with open(filename, "r+", encoding="utf-8") as a_file:
        lines = a_file.readlines()
        a_file.seek(0)
        a_file.truncate()
        for line in lines:
            a_file.write(line)
            if search_string in line:
                a_file.write(new_string + '\n')
