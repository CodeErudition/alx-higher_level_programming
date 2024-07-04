#!/usr/bin/python3
"""This module defines MyInt class that inherits from int claas"""


class MyInt(int):
    """
    Represents MyInt class that inherits from int.
    MyInt has == and != operators inverted.
    """
    def __eq__(self, n):
        """
        Overrides the == operator with !=.
        """
        return super().__ne__(n)

    def __ne__(self, n):
        """
        Overrides the != operator with ==.
        """
        return super().__eq__(n)
