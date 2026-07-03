#!/usr/bin/python3
"""Module for safe_print_division."""


def safe_print_division(a, b):
    """Divide two integers and print the result, safely."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
