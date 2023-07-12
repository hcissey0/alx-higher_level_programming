#!/usr/bin/python3
"""This module Parses logs"""


import sys


c = 0
tsize = 0
scodes = {200: 0,
          301: 0,
          400: 0,
          401: 0,
          403: 0,
          404: 0,
          405: 0,
          500: 0
          }
try:
    for lis in sys.stdin:
        tokens = lis.strip().split()
        if len(tokens) > 2:
            scode = int(tokens[-2])
            fsize = int(tokens[-1])
            tsize += fsize
            if scode in scodes:
                scodes[scode] += 1
        c += 1
        if c % 10 == 0:
            print("File size: {}".format(tsize))
            for cd, num in sorted(scodes.items()):
                if num > 0:
                    print("{}: {}".format(cd, num))
except KeyboardInterrupt:
    pass
print("File size: {}".format(tsize))
for cd, num in sorted(scodes.items()):
    if num > 0:
        print("{}: {}".format(cd, num))
