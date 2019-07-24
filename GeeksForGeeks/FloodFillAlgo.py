# Problem Description: https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0/

def floodFill(mat, m, n, x, y, k, prev):
    if(x >= m or y >= n or x < 0 or y < 0):
        return
    if(mat[x][y] == prev):
        mat[x][y] = k

        floodFill(mat, m, n, x+1, y, k, prev)
        floodFill(mat, m, n, x-1, y, k, prev)
        floodFill(mat, m, n, x, y+1, k, prev)
        floodFill(mat, m, n, x, y-1, k, prev)


t = int(input())

for _ in range(t):
    m, n = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    x, y, k = [int(x) for x in input().split()]

    mat = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            mat[i][j] = a[i*n + j]

    prev = mat[x][y]

    floodFill(mat, m, n, x, y, k, prev)

    for i in mat:
        print(*i, end=' ')
    print()
