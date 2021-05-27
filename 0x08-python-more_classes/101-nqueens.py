#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard. This
program solves the N queens problem.
---------------------------------------------------
Usage: nqueens N
where N must be an integer greater or equal to 4
---------------------------------------------------
The program will print every possible solution
to the problem, one solution per line
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if type(N) is not int:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)

BOARD_SIZE = N


def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens) - i for i, x in enumerate(queens))


def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = [solution + [i + 1]
                     for solution in solutions
                     for i in range(BOARD_SIZE)
                     if not under_attack(i + 1, solution)]
    return solutions

for answer in solve(BOARD_SIZE):
    print(list(enumerate(answer, start=1)))
