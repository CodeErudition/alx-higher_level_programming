#!/usr/bin/python3
"""This module defines a locked class"""


class LockedClass():
    """
    This class represents a locked class restricts the creation
    Attributes:
        first_name (str): The first name of the instance,
            initially set to None.
   """

    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = None
