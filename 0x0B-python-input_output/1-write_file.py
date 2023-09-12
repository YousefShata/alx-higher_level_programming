#!/usr/bin/python3
"""
write module
"""


def write_file(filename="", text=""):
    """
    function to write into a file
    """

    with open(filename, "w", encoding="utf-8")as myFile:
        words = myFile.write(text)
    return words
