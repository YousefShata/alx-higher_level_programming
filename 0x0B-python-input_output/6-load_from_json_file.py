#!/usr/bin/python3
"""
Module to hande json
"""
import json


def load_from_json_file(filename):
    """
    function to create a json object
    """
    with open(filename, "r") as f:
        return json.loads(f.readline())
