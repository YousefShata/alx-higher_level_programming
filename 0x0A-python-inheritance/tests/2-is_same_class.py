#!/usr/bin/python3
"""
Modules for object checking
"""


def is_same_class(obj, a_class):
    """
    Function that check if an object is the same type as the class

    Args:
        obj (obj): object
        a_class (obj): class to check the type

    Returns:
        bool: if same True else False
    """

    return type(obj) is a_class
