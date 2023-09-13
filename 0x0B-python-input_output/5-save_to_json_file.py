#!/usr/bin/python3
"""
json module 
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save json file
    """
    with open(filename, 'w') as Myfile:
        Myfile.write(json.dumps(my_obj))
