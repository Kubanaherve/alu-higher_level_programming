#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element safely.
    
    Args:
        my_list_1: First list
        my_list_2: Second list
        list_length: Number of elements to divide
        
    Returns:
        list: Results of division or 0 for failed divisions
    """
    result = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            result.append(div)
        except (TypeError, ZeroDivisionError, IndexError):
            result.append(0)
        except Exception:
            result.append(0)
        finally:
            print("Inside result: {}".format(result[len(result) - 1] if result else 0))
    return result

if __name__ == "__main__":
    my_list_1 = [10, 10, 100, 100]
    my_list_2 = [2, 0, 10, 0]
    result = list_division(my_list_1, my_list_2, 4)
    print("Final result:", result)