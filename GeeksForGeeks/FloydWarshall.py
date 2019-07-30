# Problem Description: https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall/0/

def floydWarshall(mat, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(i == j or i == k or j == k):
                    continue
                mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])


t = int(input())

for _ in range(t):
    n = int(input())
    mat = [[] for i in range(n)]

    for i in range(n):
        a = [int(x) for x in input().split()]
        mat[i] = a

    floydWarshall(mat, n)

    for i in range(n):
        for j in range(n):
            if(mat[i][j] >= 1e7):
                print('INF', end=' ')
            else:
                print(mat[i][j], end=' ')
        print()
