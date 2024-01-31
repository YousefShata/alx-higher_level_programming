#!/usr/bin/python3
from sys import argv
from urllib import request, parse

url = argv[2]

if __name__ == "__main__":

    data = parse.urlencode({'email': url})
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
