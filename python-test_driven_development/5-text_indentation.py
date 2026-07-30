#!/usr/bin/python3
"""Module for printing indented text.

This module provides a function to print text with 2 new lines
after each '.', '?', and ':' character.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The input string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in ".?:":
            stripped = line.strip()
            if stripped:
                print(stripped)
                print()
            line = ""

    remaining = line.strip()
    if remaining:
        print(remaining, end="")
