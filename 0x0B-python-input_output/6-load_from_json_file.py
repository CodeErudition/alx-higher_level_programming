#!/usr/bin/python3
"""
This module defines a function that creates an Object from a
“JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.
        
    Returns:
        The Python object represented by the JSON data in the file.
    """
    with open(filename, "r", encoding="utf-8") as j_file:
        return json.load(j_file)
