#!/usr/bin/python3
"""This script is used to access github through their api"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    res = requests.get(url, auth=(username, token))
    jsres = res.json()
    print(jsres.get('id'))
