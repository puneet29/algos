# Problem Description: https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array/0

def longestCommonPrefixUtil(a, b):
    i = 0
    j = 0
    res = ''

    while(i < len(a) and j < len(b)):
        if(a[i] == b[j]):
            res += a[i]
            i += 1
            j += 1
        else:
            break
    return res


def longestCommonPrefix(a, n):
    if(n == 1):
        return a[0]
    if(n == 2):
        return longestCommonPrefixUtil(a[0], a[1])
    res1 = longestCommonPrefix(a[:n//2], n//2)
    res2 = longestCommonPrefix(a[n//2:], n-n//2)
    return longestCommonPrefixUtil(res1, res2)


t = int(input())

for _ in range(t):
    n = int(input())
    a = [x for x in input().split()]

    res = longestCommonPrefix(a, n)

    if(res != ''):
        print(res)
    else:
        print(-1)
