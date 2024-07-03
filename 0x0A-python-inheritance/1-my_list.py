#!/bin/usr/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """This class represent MyList class that sorts list
    in ascending oder.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        Assumes all elements of the list are of type int.
        """
        print(sorted(self))

