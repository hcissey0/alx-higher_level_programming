#!/usr/bin/python3
"""This scropt is used to send a post requst"""

import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    res = requests.post(url, data=payload)
    try:
        jsres = res.json()
        if jsres:
            print(f"[{jsres.get('id')}] {jsres.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
