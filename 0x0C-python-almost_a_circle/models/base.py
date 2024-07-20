#!/usr/bin/python3
"""
This module defines a class Base, which will be the base of
all other classes in this project.
"""


class Base():
    """
    Base class for managing 'id' attribute in future classes.

    Attributes:
        __nb_objects (int): A private class attribute that counts
        the number of instances created.

    Methods:
        __init__(self, id=None): Initializes the instance with a
        unique 'id'.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int, optional): If provided, assigns the value to the
                                instance's id attribute.
                                If not provided, increments the __nb_objects
                                count and assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
