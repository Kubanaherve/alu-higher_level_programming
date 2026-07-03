#!/usr/bin/python3

def safe_print_integer(value):
    """Print value as integer safely using try/except and formatted strings.
    
    Args:
        value: The value to attempt to print as integer
        
    Returns:
        bool: True if value printed as integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(safe_print_integer(sys.argv[1]))