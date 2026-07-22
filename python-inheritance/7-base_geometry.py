#!/usr/bin/python3
"""Module that defines BaseGeometry with integer_validator."""


class BaseGeometry:
    """A base geometry class with area and integer_validator methods."""

    def area(self):
        """Raises an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
