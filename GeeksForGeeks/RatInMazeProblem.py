# Problem Description: https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1


def valid(arr, i, j, n, visited):
    if(i >= 0 and i < n and j >= 0 and j < n and arr[i][j] == 1 and visited[i][j] == 0):
        return True
    return False


def getPaths(direction, path):
    paths = []
    for i in range(len(path)):
        if(path[i] != '' and path[i][-1] == '$'):
            paths.append(direction + path[i])
    return paths


def findPathUtil(arr, i, j, n, visited):
    if(i == n-1 and j == n-1):
        return ['$']

    if(valid(arr, i, j, n, visited)):
        paths = []
        visited[i][j] = 1
        path1 = findPathUtil(arr, i+1, j, n, visited)
        path2 = findPathUtil(arr, i-1, j, n, visited)
        path3 = findPathUtil(arr, i, j+1, n, visited)
        path4 = findPathUtil(arr, i, j-1, n, visited)
        visited[i][j] = 0

        paths += getPaths('D', path1)
        paths += getPaths('U', path2)
        paths += getPaths('R', path3)
        paths += getPaths('L', path4)

        return paths
    return ['']


def findPath(arr, n):
    visited = [[0 for i in range(n)] for j in range(n)]
    path = findPathUtil(arr, 0, 0, n, visited)
    path.sort()
    for i in range(len(path)):
        path[i] = path[i][:-1]
    return(' '.join(path))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])] for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1
        print(findPath(matrix, n[0]))
