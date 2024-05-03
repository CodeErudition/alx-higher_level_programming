#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with an optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer, or if position is not a tuple
                of 2 positive integers.
            ValueError: If size is less than 0, or if position contains
                negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """tuple: The position of the square (getter)."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains negative integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not all(isinstance(v, int) for v in value) or
                any(v < 0 for v in value)):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        If size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns a string representation of the square."""
        result = ""
        self.my_print()
        return result
