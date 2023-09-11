#!/usr/bin/python3
"""
Module to lookup for methods
"""


def lookup(obj):
    """
    function to return all listed methods and function

    Args:
        obj(object):object to print

    Returns:
        List:list of attribute
    """

    return dir(obj)
