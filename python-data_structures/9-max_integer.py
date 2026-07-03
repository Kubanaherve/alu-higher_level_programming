#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer in a list."""
    if not my_list:
        return None
    biggest = my_list[0]
    for num in my_list[1:]:
        if num > biggest:
            biggest = num
    return biggest
