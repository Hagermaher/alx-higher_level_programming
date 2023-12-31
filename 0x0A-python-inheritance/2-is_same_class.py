#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check an obj

    Args:
        obj (any): The object
        a_class (type): The class
    Returns:
        obj is exactly an instance of a_class - True.
        Or - False.
    """
    if type(obj) == a_class:
        return True
    return False
