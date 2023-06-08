#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if not len(sys.argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2][0] != '+' and sys.argv[2][0] != '-'\
            and sys.argv[2][0] != '*' and sys.argv[2][0] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = ".format(sys.argv[1], sys.argv[2], sys.argv[3]), end="")
    match sys.argv[2]:
        case "+":
            print(add(int(sys.argv[1]), int(sys.argv[3])))
        case "-":
            print(sub(int(sys.argv[1]), int(sys.argv[3])))
        case "*":
            print(mul(int(sys.argv[1]), int(sys.argv[3])))
        case "/":
            print(div(int(sys.argv[1]), int(sys.argv[3])))
