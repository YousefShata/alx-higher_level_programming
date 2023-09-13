#!/usr/bin/python3
"""
Json Module
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        function to initate Student attr
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function to return attribute as json
        """

        return self.__dict__
