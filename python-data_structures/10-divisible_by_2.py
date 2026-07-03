#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return list of booleans for divisibility by 2."""
    return [num % 2 == 0 for num in my_list]
