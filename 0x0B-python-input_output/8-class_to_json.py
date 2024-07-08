#!/usr/bin/python3
"""
This module defines a function that returns the dictionary
description with a simple data structure for JSON serialization
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary description of the object suitable for JSON
        serialization.
    """
    return obj.__dict__
