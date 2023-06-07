#!/usr/bin/python3
a = 1
for i in range(122, 96, -1):
    if a == 1:
        a = 0
    else:
        i = i - 32
        a = 1
    print("{}".format(chr(i)), end="")

