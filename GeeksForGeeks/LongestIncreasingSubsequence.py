# Problem Description: https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if(a[j] < a[i] and dp[i] < dp[j]+1):
                dp[i] = 1 + dp[j]

    print(max(dp))
