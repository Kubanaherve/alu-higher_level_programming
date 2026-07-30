#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1] if len(argv) > 1 else "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
