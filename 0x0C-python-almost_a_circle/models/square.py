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

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, w_value):
        self.validator("width", w_value)
        self.__width = w_value
        self.__height = w_value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        self.validator("width", w_value)
        self.__width = w_value
        self.__height = w_value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h_value):
        self.validator("height", h_value)
        self.__width = h_value
        self.__height = h_value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: A list of arguments. No-keyworded arguments.
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
            **kwargs: A dictionary of key/value arguments. Keyworded
                        arguments.Each key in this dictionary
                        represents an attribute to the instance.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.

        Returns:
            dict: The dictionary representation of the square.
        """
        attrs = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attrs}
