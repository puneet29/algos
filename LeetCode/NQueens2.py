import numpy as np


class Solution:
    def totalNQueens(self, n: int) -> int:

        board = np.zeros((n, n))

        def isunderattack(row: int, col: int) -> bool:
            if(1 in board[row]):
                return True
            if(1 in board[:, col]):
                return True
            if(1 in [board[i][j] for i, j in zip(range(row+1, n), range(col+1, n))]):
                return True
            if(1 in [board[i][j] for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1))]):
                return True
            if(1 in [board[i][j] for i, j in zip(range(row+1, n), range(col-1, -1, -1))]):
                return True
            if(1 in [board[i][j] for i, j in zip(range(row-1, -1, -1), range(col+1, n))]):
                return True
            return False

        def helper(row: int, positions: int) -> int:
            if(row >= n):
                return positions
            for col in range(n):
                if not isunderattack(row, col):
                    board[row][col] = 1
                    if(row == n-1):
                        positions += 1
                    positions = helper(row+1, positions)
                    board[row][col] = 0
            return positions

        return helper(0, 0)
