#!/usr/bin/python3
from sys import argv
from urllib import request, parse

url = argv[2]

data = urllib.parse.urlencode({'email': url})
data = data.encode('ascii')
req = urllib.request.Request(argv[1], data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode('utf-8'))
