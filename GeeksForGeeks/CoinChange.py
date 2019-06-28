# Problem Description: https://practice.geeksforgeeks.org/problems/coin-change/0

t = int(input())

for _ in range(t):
    m = int(input())
    a = [int(x) for x in input().split()]
    n = int(input())

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(n+1):
            if(j == 0):
                dp[i][j] = 1
            elif(j < a[i-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-a[i-1]] + dp[i-1][j]

    print(dp[m][n])
