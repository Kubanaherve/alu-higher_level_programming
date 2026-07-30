#!/usr/bin/python3
"""Module for printing a name.

This module provides a function to print a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first_name> <last_name>".

    Args:
        first_name: The first name (string).
        last_name: The last name (string), defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
