#!/usr/bin/python3
"""
Module Doc
"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        id = response.getheader("X-Request-Id")
        print(f"{id}")
