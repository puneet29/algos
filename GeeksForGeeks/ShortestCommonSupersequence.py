# Problem Description: https://practice.geeksforgeeks.org/problems/shortest-common-supersequence/0

t = int(input())

for _ in range(t):
    a, b = [x for x in input().split()]

    dp = [[0 for j in range(len(b) + 2)] for i in range(len(a) + 2)]

    for i in range(len(a)+1):
        for j in range(len(b)+1):

            if(i == 0):
                dp[i][j] = j
            elif(j == 0):
                dp[i][j] = i
            elif(a[i-1] == b[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    print(dp[len(a)][len(b)])
