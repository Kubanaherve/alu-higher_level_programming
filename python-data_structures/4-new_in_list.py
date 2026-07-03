#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element in a copy of the list without modifying original."""
    copy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy
