# Problem Description: https://practice.geeksforgeeks.org/problems/solve-the-sudoku/0

def isSafe(grid, row, col, value):
    row = row - row % 3
    col = col - col % 3

    for i in range(3):
        for j in range(3):
            if(grid[i+row][j+col] == value):
                return False
    return True


def printSolution(grid):
    for row in grid:
        for ele in row:
            print(ele, end=' ')
    print()


def findEmpty(grid, l):
    for i in range(9):
        for j in range(9):
            if(grid[i][j] == 0):
                l[0] = i
                l[1] = j
                return True
    return False


def solveSudokuUtil(grid):
    l = [0, 0]
    if(not findEmpty(grid, l)):
        printSolution(grid)
        return True

    row = l[0]
    col = l[1]

    option1 = set(range(1, 10))
    for i in range(9):
        if(grid[row][i] != 0):
            option1.remove(grid[row][i])

    option2 = set(range(1, 10))
    for i in range(9):
        if(grid[i][col] != 0):
            option2.discard(grid[i][col])
    options = option1.intersection(option2)

    for option in options:
        if(isSafe(grid, row, col, option)):
            grid[row][col] = option
        else:
            continue

        if(solveSudokuUtil(grid)):
            return True

        grid[row][col] = 0
    return False


def solveSudoku(grid):
    if(not solveSudokuUtil(grid)):
        print(-1)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        arr = [int(x) for x in input().split()]
        mat = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                mat[i][j] = arr[j+i*9]

        solveSudoku(mat)
