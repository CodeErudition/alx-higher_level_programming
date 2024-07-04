#!/usr/bin/python3
"""
This mode defines a Rectangle class that
inherits from the BaseGeometry class.
"""


class BaseGeometry():
    """
    Represents a BaseGeometry class.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Parameters:
            name (str): The name of the parameter.
            value (int): The value of the parameter.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class named Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
