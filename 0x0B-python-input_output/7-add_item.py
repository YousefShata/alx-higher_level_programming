#!/usr/bin/python3
"""
Json Module
"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    function to save arugments to json object"
    """
    fname = "add_item.json"
    if (path.isfile(fname)):
        final_list = load_from_json_file(fname)
    else:
        final_list = []
    for i in range(1, len(argv)):
        final_list.append(argv[i])
    save_to_json_file(final_list, fname)


add_item()
