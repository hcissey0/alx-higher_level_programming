#!/usr/bin/python3
"""This script is used to retch useing requests"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.htbn.io/status'
    res = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
