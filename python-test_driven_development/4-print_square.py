#!/usr/bin/python3
"""Module for printing a square.

This module provides a function to print a square using the # character.
"""


def print_square(size):
    """Prints a square of # characters of the given size.

    Args:
        size: The side length of the square (integer).

    Raises:
        TypeError: If size is not an integer (or is a negative float).
        ValueError: If size is a negative integer.
    """
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
