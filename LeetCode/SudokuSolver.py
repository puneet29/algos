class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row: int, col: int, val: str) -> bool:
            if(val in board[row]):
                return False
            if(val in [board[r][col] for r in range(9)]):
                return False
            for r in range(3*(row//3), (3*(row//3))+3):
                for c in range(3*(col//3), (3*(col//3))+3):
                    if(val == board[r][c]):
                        return False
            return True

        def helper(board: List[List[str]], row: int = 0, col: int = 0) -> bool:
            if(col >= 9):
                return helper(board, row+1, 0)
            if(row >= 9):
                return True
            if(board[row][col] == '.'):
                for value in range(1, 10):
                    if isValid(row, col, str(value)):
                        board[row][col] = str(value)
                        finished = helper(board, row, col+1)
                        if(finished):
                            return finished
                        board[row][col] = '.'
                return False
            else:
                return helper(board, row, col+1)

        helper(board)
