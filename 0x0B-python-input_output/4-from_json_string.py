#!/usr/bin/pythom3
"""
module returns object into json
"""
import json


def from_json_string(my_str):
    """
    function to return object in json form
    """

    return json.loads(my_str)
