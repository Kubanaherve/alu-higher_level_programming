#!/usr/bin/python3

def raise_exception_msg():
    """Raise a NameError exception with custom message."""
    raise NameError("NameError exception")

if __name__ == "__main__":
    try:
        raise_exception_msg()
    except NameError as e:
        print("NameError caught:", str(e))