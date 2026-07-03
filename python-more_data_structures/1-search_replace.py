#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element in a new list."""
    return [replace if x == search else x for x in my_list]
