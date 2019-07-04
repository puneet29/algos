# Problem Description: https://practice.geeksforgeeks.org/problems/shortest-source-to-destination-path/

import queue


def bfsDistance(u, v, mat, n, m):

    if(not mat[u[0]][u[1]] or not mat[v[0]][v[1]]):
        return(-1)

    rowNum, colNum = [-1, 0, 1, 0], [0, -1, 0, 1]
    visited = [[False for i in range(m)] for j in range(n)]
    q = queue.Queue(n*m)

    q.put({'pt': u, 'dist': 0})
    visited[u[0]][u[1]] = True

    while(not q.empty()):
        node = q.get()
        pt = node['pt']

        if(pt[0] == v[0] and pt[1] == v[1]):
            return(node['dist'])

        for i in range(4):
            row = pt[0] + rowNum[i]
            col = pt[1] + colNum[i]

            if(isValid(row, col, n, m) and mat[row][col] and not visited[row][col]):
                visited[row][col] = True
                neighbor = {'pt': [row, col], 'dist': node['dist'] + 1}
                q.put(neighbor)
    return(-1)


def isValid(row, col, n, m):
    return(row >= 0 and row < n and col >= 0 and col < m)


def convert2D(arr, n, m):
    a = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            a[i][j] = arr[m*i+j]
    return(a)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        x, y = [int(x) for x in input().split()]
        a = convert2D(a, n, m)

        print(bfsDistance([0, 0], [x, y], a, n, m))
