#!/usr/bin/python3
def no_c(my_string):
    """Remove all 'c' and 'C' characters from a string."""
    return "".join(char for char in my_string if char not in "cC")
