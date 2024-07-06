#!/usr/bin/python3
"""
This module defines a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to write to the file (will be serialized to JSON).
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, "w", encoding="utf-8") as w_Jfile:
        json.dump(my_obj, w_Jfile)
