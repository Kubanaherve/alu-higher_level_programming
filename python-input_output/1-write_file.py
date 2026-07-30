#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return the number of chars."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
