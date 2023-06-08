#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print(0)
    else:
        res = 0
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            res += int(sys.argv[i])
        print(res)
