#!/usr/bin/python3
"""
This module defines a class that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Parameters:
    obj (any): The object to inspect.

    Returns:
    list: A list of strings representing the names of the attributes
    and methods of the object.
    """
    return (dir(obj))
