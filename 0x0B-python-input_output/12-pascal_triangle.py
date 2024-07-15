#!/usr/bin/python3
"""
This module defines a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    l_triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = l_triangle[i - 1][j - 1] + l_triangle[i - 1][j]
        l_triangle.append(row)

    return l_triangle
