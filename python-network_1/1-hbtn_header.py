#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a URL."""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
