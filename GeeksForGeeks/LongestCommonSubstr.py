# Problem Description: https://practice.geeksforgeeks.org/problems/longest-common-substring/0


def commonSubstr(a, b, n, m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    maxSubLen = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if(a[i-1] == b[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                if(maxSubLen < dp[i][j]):
                    maxSubLen = dp[i][j]
                    #row = i
                    #col = j
    # if(maxSubLen==0):
    #     return -1
    # else:
    #     res = ''
    #     for i in range(maxSubLen):
    #         res = a[row-1] + res
    #         row -= 1
    #         col -= 1
    #     return res

    return maxSubLen


t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = input()
    b = input()

    print(commonSubstr(a, b, n, m))
