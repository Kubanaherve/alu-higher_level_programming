#!/usr/bin/python3
"""Defines a MyList class inheriting from list."""


class MyList(list):
    """Represents a custom list that can print sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
