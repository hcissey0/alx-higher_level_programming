#!/usr/bin/python3
"""This scropt prints the response if the status code is less tha 400"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    try:
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(res.status_code))
