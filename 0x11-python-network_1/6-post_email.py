#!/usr/bin/python3
"""This script is used to post an email address"""

import requests
import sys


if __name__ == "__amin__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    res = requests.post(url, data=values)
    print(res.text)
