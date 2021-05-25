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
N = int(sys.argv[1])
if type(N) is not int:
    print("N must be a number")
    exit(1)
elif N < 4:
    print("N must be at least 4")
    exit(1)

"""N x N matrix with all elements 0"""
board = [[0] * N for i in range(N)]

def is_attack(i, j):
    """checking if there is a queen in row or column"""
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    """checking diagonals"""
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queen(n):
    """if n is 0, solution found"""
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            """checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied"""
            if (not(is_attack(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                """recursion"""
                """wether we can put the next queen with this arrangment or not"""
                if N_queen(n - 1) == True:
                    return True
                board[i][j] = 0

    return False

N_queen(N)
for i in range(0, N):
        for j in range(0, N):
            print(board[i][j])
