#!/usr/bin/python3
"""N Queens problem"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    """Recursive utility function to solve N Queens problem"""

    # Base case: If all queens are placed then return True
    if col >= len(board):
        solutions.append([[i, j] for i, row in enumerate(board) for j, val in enumerate(row) if val])
        return True

    # Consider this column and try placing this queen in all rows
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen

            # Recur to place rest of the queens
            solve_nqueens_util(board, col + 1, solutions)

            # If placing queen in board[i][col] doesn't lead to a solution then remove queen from board[i][col]
            board[i][col] = 0

    return False


def solve_nqueens(n):
    """Main function to solve N Queens problem"""

    # Initialize empty board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    # Start from first column and solve recursively
    solve_nqueens_util(board, 0, solutions)

    return solutions


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)

