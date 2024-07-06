#!/usr/bin/python3
"""
This module define a function that reads a text file
(UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to
        an empty string.
    """
    with open(filename, "r", encoding="utf-8") as d_file:
        file_content = d_file.read()
        print(file_content, end="")
