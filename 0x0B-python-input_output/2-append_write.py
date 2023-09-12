#!/usr/bin/python3
"""
write module
"""


def append_write(filename="", text=""):
    """
    function to write into a file
    """

    with open(filename, "a", encoding="utf-8")as myFile:
        words = myFile.write(text)
    return words
