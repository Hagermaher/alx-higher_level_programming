#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts

    Args:
        my_list (list): The list to print
        x (int): The number of elements

    Returns:
        The number of
    """
    rt = 0
    for w in range(x):
        try:
            print("{}".format(my_list[w]), end="")
            rt += 1
        except IndexError:
            break
    print("")
    return (rt)
