#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists containing numbers (int or float).
        div (int or float): The divisor.

    Returns:
        list: A new matrix representing the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists, or if it contains
            non-numeric elements.
        TypeError: If rows of the matrix have different lengths.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("All rows of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]

