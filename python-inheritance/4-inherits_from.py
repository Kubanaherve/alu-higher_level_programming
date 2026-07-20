#!/usr/bin/python3
"""Defines a function to check inherited class instance."""


def inherits_from(obj, a_class):
    """Returns True if obj inherited from a_class but not exact match.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj inherited from a_class, but type is not a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
