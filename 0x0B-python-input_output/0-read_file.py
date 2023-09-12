#!/usr/bin/python3
"""
readfile module
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, "r",encoding=("utf-8")) as Myfile:
        Myfile.read()
