#!/usr/bin/python3
"""
Module Doc
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[2]

    data = urllib.parse.urlencode({'email': url[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
