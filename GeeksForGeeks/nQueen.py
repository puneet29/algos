# Problem Description: https://practice.geeksforgeeks.org/problems/n-queen-problem/0


def isSafe(board, row, col):

    for i in range(row):
        if(board[i][col] == 1):
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if(board[i][j] == 1):
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if(board[i][j] == 1):
            return False
    return True


def getConfig(board, n):
    s = '['
    for i in range(n):
        for j in range(n):
            if(board[i][j] == 1):
                s += str(j+1) + ' '
    s += '] '
    return s


def nQueenUtil(board, row, n, result):
    if(row >= n):
        result.append(getConfig(board, n))
        return

    for i in range(n):
        if(isSafe(board, row, i)):
            board[row][i] = 1
            nQueenUtil(board, row+1, n, result)
            board[row][i] = 0


def nQueen(n):
    mat = [[0 for i in range(n)] for j in range(n)]
    result = []
    nQueenUtil(mat, 0, n, result)
    if(len(result) > 0):
        return(''.join(result))
    else:
        return(-1)


t = int(input())

for _ in range(t):
    n = int(input())
    print(nQueen(n))
