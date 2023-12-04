#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks an obj

    Args:
        obj (any): The obj
        a_class (type): The class
    Returns:
        obj is an inherited instance of a_class - True.
        Or - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
