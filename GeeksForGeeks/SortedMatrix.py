# Problem Description: https://practice.geeksforgeeks.org/problems/sorted-matrix/0

def sortMatrix(a, n):
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append(a[i][j])

    temp.sort()

    for i in range(n):
        for j in range(n):
            a[i][j] = temp[n*i+j]


t = int(input())

for _ in range(t):
    n = int(input())
    inputArr = [int(x) for x in input().split()]
    a = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = inputArr[n*i+j]

    sortMatrix(a, n)

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
    print()
