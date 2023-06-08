#!/usr/bin/python3
if __name__ == '__main__':
    for name in dir(__import__("hidden_4.pyc")):
        if not name.startswith("__"):
            print(name)
