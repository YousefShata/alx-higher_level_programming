#!/usr/bin/python3
"""
readfile module
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, encoding=("utf-8")) as Myfile:
        print(Myfile.read())
            
