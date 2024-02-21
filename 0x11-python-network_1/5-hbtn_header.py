#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = argv[1]
    response = requests.get(url)
    id = response.headers.get('X-Request-Id')
    print(id)
