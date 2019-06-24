# Problem Description: https://practice.geeksforgeeks.org/problems/shop-in-candy-store/0

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()

    minCost = 0
    maxCost = 0
    i, j = 0, n

    while(i < j):
        minCost += a[i]
        j -= k
        i += 1

    i, j = 0, n
    while(i < j):
        maxCost += a[j-1]
        i += k
        j -= 1
    print(minCost, maxCost)
