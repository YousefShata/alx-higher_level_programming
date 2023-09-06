#!/usr/bin/python3
""" 
Module that prevents the user from dynamically creating new instance attributes
"""


class LockedClass:
    """
    a clas with no objects or attributes 
    that only accept the attriube named "first_name"
    """
    __slots__ = "first_name"
