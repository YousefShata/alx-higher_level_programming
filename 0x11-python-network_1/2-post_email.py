#!/usr/bin/python3
from sys import argv
from urllib import request, parse

url = argv[2]

if __name__ == "__main__":

    data = urllib.parse.urlencode({'email': url[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
