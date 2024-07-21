#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x coordinate of the rectangle.
        y (int): The y coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the rectangle. Default is 0.
            y (int, optional): The y coordinate of the rectangle. Default is 0.
            id (int, optional): The id of the instance. Default is None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validator(attr, attr_value, greater_than_zero=True):
        """
        Validates the attribute value.

        Args:
            attr (str): The name of the attribute.
            attr_value (int): The value of the attribute.
            greater_than_zero (bool): If True, the value must be > 0.
                                      If False, the value must be >= 0.
        """
        if not isinstance(attr_value, int):
            raise TypeError("{} must be an integer".format(attr))
        if greater_than_zero and attr_value <= 0:
            raise ValueError("{} must be > 0".format(attr))
        if not greater_than_zero and attr_value < 0:
            raise ValueError("{} must be >= 0".format(attr))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        self.validator("width", w_value)
        self.__width = w_value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h_value):
        self.validator("height", h_value)
        self.__height = h_value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_value):
        self.validator("x", x_value, False)
        self.__x = x_value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_value):
        self.validator("y", y_value, False)
        self.__y = y_value

    def area(self):
        """
        Returns the area value of the Rectangle instance.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: The string representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))
