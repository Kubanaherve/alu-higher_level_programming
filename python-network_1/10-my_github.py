#!/usr/bin/python3
"""Uses GitHub API with Basic Authentication to display user id."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
