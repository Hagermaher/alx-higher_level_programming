#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element

    Args:
        my_list_1 (list): first list
        my_list_2 (list): second list.
        list_length (int): number of elements

    Returns:
        A new list of length
    """
    new_list = []
    for w in range(0, list_length):
        try:
            div = my_list_1[w] / my_list_2[w]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
