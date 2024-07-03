#!/usr/bin/python3
"""
This module defines a class that checks if the object is an
instance of a class that inherited (directly or indirectly) from
the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Parameters:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
