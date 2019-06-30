# Problem Description: https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0

import sys

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    dp = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):

            if(j == 1 or i == 1):
                dp[i][j] = j
                continue

            minVal = sys.maxsize
            for x in range(1, j+1):
                res = max(dp[i-1][x-1], dp[i][j-x])
                if(res < minVal):
                    minVal = res
            dp[i][j] = minVal + 1
    print(dp[n][k])
