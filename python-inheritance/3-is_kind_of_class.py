#!/usr/bin/python3
"""Defines a function to check class or inherited instance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherits from, a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or subclass instance, else False.
    """
    return isinstance(obj, a_class)
