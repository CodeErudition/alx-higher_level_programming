#!/usr/bin/python3
"""
This module defines as clas  if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of
    the specified class; otherwise False.

    Parameters:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
