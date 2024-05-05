#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """
    This class represents a rectangle

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: if not an integer.
            ValueError: if value is less than 0.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """int: the width of the rectangle (getter)."""
            return self.__width

        @width.setter
        def width(self, value):
            """
            Sets the width of the rectangle.

            Args:
                value (int): the new width of the rectangle.

            Raises:
                 TypeError: if not an integer.
                 ValueError: if value is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """int: the height of the rectangle (getter)."""
            return self.__height

        @height.setter
        def height(self, value):
            """
            Sets the height of the rectangle.

            Args:
                value (int): the new width of the rectangle.

            Raises:
                 TypeError: if not an integer.
                 ValueError: if value is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__height = value
