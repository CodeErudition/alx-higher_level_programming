#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from Base
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
            x (int, optional): The x coordinate of the rectangle.
                                Default is 0.
            y (int, optional): The y coordinate of the rectangle.
                                Default is 0.
            id (int, optional): The id of the instance. Default is None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        self.__width = w_value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h_value):
        self__height = h_value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_value):
            self.__x = x_value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_value):
    self.__y = y_value
