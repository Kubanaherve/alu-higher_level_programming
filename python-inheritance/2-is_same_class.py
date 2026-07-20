#!/usr/bin/python3
"""Defines a function to check exact class instance."""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
