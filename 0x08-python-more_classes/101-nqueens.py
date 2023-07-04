#!/usr/bin/python3
import sys


def valid(brd, r, c):
    """check if the placement is valid"""
    # Checking the row on left side
    for i in range(c):
        if brd[r][i]:
            return False

    # Checking lower left diagonal
    for i, j in zip(range(r, len(brd)), range(c, -1, -1)):
        if brd[i][j]:
            return False

    # Checking upper diagonal on the left
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if brd[i][j]:
            return False

    return True


def solve(brd, c, solns):
    """Recursively solve the puzzle"""
    if c == len(brd):
        q = []
        for i in range(len(brd)):
            for j in range(len(brd)):
                if brd[i][j]:
                    q.append([i, j])
        solns.append(q)
        return

    for i in range(len(brd)):
        if valid(brd, i, c):
            brd[i][c] = 1
            solve(brd, c + 1, solns)
            brd[i][c] = 0


def main():
    """This is the entry point of the program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = [[0 for j in range(n)] for i in range(n)]
    solns = []

    solve(brd, 0, solns)

    for i in solns:
        print(i)


if __name__ == '__main__':
    main()
