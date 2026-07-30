#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib."""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1] if len(argv) > 1 else "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
