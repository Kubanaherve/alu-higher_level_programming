#!/usr/bin/python3

def safe_print_list(list_to_print, x):
    """Print x elements from list_to_print safely using try/except.
    
    Args:
        list_to_print: The list to print from
        x: Number of elements to attempt to print
        
    Returns:
        int: Number of elements successfully printed
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(list_to_print[i]))
            count += 1
    except IndexError:
        pass
    return count

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
        my_list = ["School", 1, "Python", 2, "University"]
        safe_print_list(my_list, x)