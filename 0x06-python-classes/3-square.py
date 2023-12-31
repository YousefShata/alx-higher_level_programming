#!/usr/bin/python3
"""Module to create Square Class"""


class Square:
    """initate a square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        self.area = self.__size * self.__size
        return self.area
