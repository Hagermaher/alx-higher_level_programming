#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class)
    """"check an obj

    Args:
        obj (any): The object
        a_class (type): The class
    Returns:
        obj is an instance or inherited instance of a_class - True.
        Or - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
