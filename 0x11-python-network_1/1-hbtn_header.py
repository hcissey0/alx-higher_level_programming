#!/usr/bin/python3
"""This script is used to send a requst to the url"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-id"))
