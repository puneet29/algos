# Problem Description: https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    dp = a[:]

    for i in range(n):
        for j in range(i):
            if(a[j] < a[i] and dp[i] < dp[j]+a[i]):
                dp[i] = dp[j] + a[i]

    print(max(dp))
