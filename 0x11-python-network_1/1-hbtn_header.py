#!/usr/bin/python3
from sys import argv
from urllib import request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    id = response.headers.get("X-Request-Id")
    print(f"{id}")
