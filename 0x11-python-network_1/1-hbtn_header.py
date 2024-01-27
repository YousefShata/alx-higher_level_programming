#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    id = response.headers.get("X-Request-Id")

    if id is not None:
        print(id)
    else:
        print("No ID")
