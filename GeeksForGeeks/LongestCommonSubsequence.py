# Problem Description: https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0

t = int(input())

for _ in range(t):
    x, y = [int(x) for x in input().split()]
    a = list(input())
    b = list(input())

    dp = [[0 for i in range(y+1)] for j in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if(a[i-1] == b[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[x][y])
