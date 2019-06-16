# Problem Description: https://practice.geeksforgeeks.org/problems/boolean-matrix-problem/0


def getBoolMat(a, r, c):
    row = set()
    col = set()

    for i in range(r):
        for j in range(c):
            if(a[i][j] == 1):
                row.add(i)
                col.add(j)

    for i in range(r):
        if(i in row):
            a[i] = [1 for x in range(c)]
        for j in col:
            a[i][j] = 1


t = int(input())

for _ in range(t):
    r, c = [int(x) for x in input().split()]
    a = []

    for row in range(r):
        a.append([int(x) for x in input().split()])

    getBoolMat(a, r, c)

    for i in range(r):
        print(" ".join([str(x) for x in a[i]]))
