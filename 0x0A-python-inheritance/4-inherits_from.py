#!/usr/bin/python3
"""
Module Doc
"""


def inherits_from(obj, a_class):
    """
    Function to check the object type
    """

    return isinstance(obj, a_class) and type(obj) != a_class
