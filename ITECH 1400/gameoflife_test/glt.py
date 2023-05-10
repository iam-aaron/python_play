import numpy as np

# set the grid size
n = 20

# initialize the board
board = np.zeros((n, n), dtype=int)

# set some initial conditions
# board[n//2, n//2] = 1
# board[n//2+1, n//2] = 1
# board[n//2-1, n//2] = 1
# board[n//2, n//2+1] = 1
# board[n//2, n//2-1] = 1

board[0, 0] = 1
board[0, 1] = 1
board[0, 2] = 1
board[1, 0] = 1
board[1, 1] = 1


def printBoard(board):
    # i=row, j=column
    for i in board:
        for j in i:
            print(f"{'_' if j == 0 else '*'}", end=" ")
        print()
    print()

def neighborSum(board, i, j, n):
    neighbors = (board[(i-1+n)%n][(j-1+n)%n] +
        board[(i-1+n)%n][j] +
        board[(i-1+n)%n][(j+1)%n] +
        board[i%n][(j+1)%n] +
        board[(i+1)%n][(j+1)%n] +
        board[(i+1)%n][j] +
        board[(i+1)%n][(j-1+n)%n] +
        board[i][(j-1+n)%n])
    return neighbors

def nextPattern(board, n):
    new_board = board.copy()
    for i in range(n):
        for j in range(n):
            neighbors = neighborSum(board, i, j, n)
            if board[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[i, j] = 0
            else:
                if neighbors == 3:
                    new_board[i, j] = 1
    return new_board



printBoard(board)

# print(neighborSum(board, 10, 10, n))

printBoard(nextPattern(board, n))