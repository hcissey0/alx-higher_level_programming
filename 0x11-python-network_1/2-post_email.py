#!/usr/bin/python3
"""This scrip is used to send a post request with email as the parameter"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    url = url + "?email=" + email
    with urllib.request.urlopen(url) as res:
        print(res.read().decode('utf-8'))
