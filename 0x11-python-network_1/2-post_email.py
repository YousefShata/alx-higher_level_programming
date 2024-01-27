#!/usr/bin/python3
import urllib.request

url = argv[2]

data = urllib.parse.urlencode({'email': url[2]})
data = data.encode('ascii')
req = urllib.request.Request(argv[1], data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode('utf-8'))
