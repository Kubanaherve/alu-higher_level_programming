#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an exception to indicate area is not implemented.

        Raises:
            Exception: Always, with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
