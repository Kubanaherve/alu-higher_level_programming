#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute and method names as strings.
    """
    return dir(obj)
