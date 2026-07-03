#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print x integers from my_list safely using try/except.
    
    Args:
        my_list: The list to print integers from
        x: Number of elements to attempt to print
        
    Returns:
        int: Number of integers successfully printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
            count += 1
        except (IndexError, ValueError, TypeError):
            continue
    return count

if __name__ == "__main__":
    my_list = [1, 2, 3, "School", 5]
    count = safe_print_list_integers(my_list, 5)
    print("Count:", count)