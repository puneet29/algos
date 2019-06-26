# Problem Description: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0

def getMaxValue(val, wt, W, n):
    K = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if(wt[i-1] <= W):
                K[i][w] = max(K[i-1][w],  val[i-1] + K[i-1][w-wt[i-1]])
            else:
                K[i][w] = K[i-1][w]
    return(K[n][W])


t = int(input())

for _ in range(t):
    n = int(input())
    w = int(input())
    val = [int(x) for x in input().split()]
    wt = [int(x) for x in input().split()]

    value = getMaxValue(val, wt, w, n)
    print(value)
