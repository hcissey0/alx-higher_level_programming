#!/usr/bin/python3
"""This script is used to access commit messages"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".\
            format(sys.argv[2], sys.argv[1])
    res = requests.get(url)
    jsres = res.json()
    for k, v in enumerate(jsres):
        if k == 13:
            break
        print("{}: {}".format(v.get('sha'), v.get('commit').get('author').get('name')))
