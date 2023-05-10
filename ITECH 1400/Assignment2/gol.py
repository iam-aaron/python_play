import numpy as np

class GameOfLife():
    def __init__(self, n):
        self.n = n
        self.board = np.zeros((n, n), dtype=int)
    
    def printBoard(self):
        # i=row, j=column
        for i in self.board:
            for j in i:
                print(f"{' ' if j == 0 else '*'}", end=" ")
            print()
        print()
    
    def neighborSum(self, i, j):
        neighbors = (self.board[(i-1+self.n)%self.n][(j-1+self.n)%self.n] +
            self.board[(i-1+self.n)%self.n][j] +
            self.board[(i-1+self.n)%self.n][(j+1)%self.n] +
            self.board[i%self.n][(j+1)%self.n] +
            self.board[(i+1)%self.n][(j+1)%self.n] +
            self.board[(i+1)%self.n][j] +
            self.board[(i+1)%self.n][(j-1+self.n)%self.n] +
            self.board[i][(j-1+self.n)%self.n])
        return neighbors
    
    def nextPattern(self):
        new_board = self.board.copy()
        for i in range(self.n):
            for j in range(self.n):
                neighbors = self.neighborSum(i, j)
                if self.board[i, j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_board[i, j] = 0
                else:
                    if neighbors == 3:
                        new_board[i, j] = 1
        self.board = new_board
        return self.board