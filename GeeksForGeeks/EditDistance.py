# Problem Description: https://practice.geeksforgeeks.org/problems/edit-distance/0

t = int(input())

for _ in range(t):
    p, q = [int(x) for x in input().split()]
    a, b = [x for x in input().split()]

    dp = [[0 for i in range(q+1)] for j in range(p+1)]

    for i in range(p+1):
        for j in range(q+1):
            if(i == 0):
                dp[i][j] = j
            elif(j == 0):
                dp[i][j] = i
            elif(a[i-1] == b[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    print(dp[p][q])
