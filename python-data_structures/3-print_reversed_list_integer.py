#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if my_list:
        for num in my_list[::-1]:
            print("{:d}".format(num))
