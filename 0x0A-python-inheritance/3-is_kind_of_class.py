#!/usr/bin/python3
"""
This module defines a class that checks if the object
is an instance of, or if the object is an instance of a
class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise False.

    Parameters:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
