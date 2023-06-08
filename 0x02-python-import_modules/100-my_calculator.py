#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = ".format(a, operator, b), end="")

    if operator == "+":
        print(add(a, b))
    elif operator == "-":
        print(sub(a, b))
    elif operator == "*":
        print(mul(a, b))
    elif operator == "/":
        print(div(a, b))


if __name__ == "__main__":
    main()
