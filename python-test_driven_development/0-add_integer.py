#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function to add two integers or floats
(with floats being cast to integers first).
"""


def add_integer(a, b=98):
    """Adds two integers or floats (cast to int).

    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
