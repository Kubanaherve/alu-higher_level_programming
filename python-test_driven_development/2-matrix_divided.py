#!/usr/bin/python3
"""Module for dividing all elements of a matrix.

This module provides a function to divide all elements of a matrix
by a given divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor (int or float).

    Returns:
        A new matrix with each element divided by div, rounded to 2
        decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error_msg)
    if len(matrix) == 0:
        raise TypeError(error_msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        if len(row) == 0:
            raise TypeError(error_msg)
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(error_msg)
    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(val / div, 2) for val in row] for row in matrix]
