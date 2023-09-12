#!/usr/bin/python3
"""
Module doc
"""


class MyInt(int):
    """
    My int
    """

    def __eq__(self, other):
        """
        Uno
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Uno
        """
        return super().__eq__(other)
