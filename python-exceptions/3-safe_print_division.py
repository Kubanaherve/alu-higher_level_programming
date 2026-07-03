#!/usr/bin/python3

def safe_print_division(a, b):
    """Safely divide a by b using try/except/finally.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        float/None: Division result or None if division failed
    """
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

if __name__ == "__main__":
    print(safe_print_division(10, 2))
    print(safe_print_division(10, 0))