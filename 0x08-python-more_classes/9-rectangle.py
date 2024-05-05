#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """
    This class represents a rectangle

    Attributes:
        print_symbol: The symbol used for string representation
        number_of_instances: Increases during each new instance
            instantiation and Decreases during each instance deletion.
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """
    print_symbol = "#"
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of a rectangle

        Returns:
            int: The area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle

        Returns:
            int: The perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints a message when a instance of a rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a square with equal width and height.
        """
        return cls(size, size)
