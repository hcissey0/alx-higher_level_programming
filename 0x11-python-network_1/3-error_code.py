#!/usr/bin/python3
"""This script takes a url and sends a request to the url"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
