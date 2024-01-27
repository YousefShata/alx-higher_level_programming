#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body request:")
    print("\t- type:{}".format(type(html)))
    print("\t- content:{}".format(html))
    print("\t- utf8 contect:{}".format(html.decode("utf-8")))
