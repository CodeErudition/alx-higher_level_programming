#!/usr/bin/python3
"""
This module defines a class Square that inherits
from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x coordinate of the square.
        y (int): The y coordinate of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): The size of the square (width and height will
                        be this size).
            x (int, optional): The x coordinate of the square. Default is 0.
            y (int, optional): The y coordinate of the square. Default is 0.
            id (int, optional): The id of the instance. Default is None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))
