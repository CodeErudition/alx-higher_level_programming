#!/usr/bin/python3
"""This module defines a Square Class"""


class Square:
    """
    This class represents a Square.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
        size (int): The size of the Square.
        """
        self.__size = size
