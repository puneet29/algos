# Problem Description: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def maxLen(n, arr):
    d = {}
    total = 0
    maxLen = 0

    for i in range(n):
        total += arr[i]

        if arr[i] is 0 and maxLen is 0:
            maxLen = 1

        if total is 0:
            maxLen = i + 1

        if(total in d):
            maxLen = max(maxLen, i - d[total])
        else:
            d[total] = i
    return(maxLen)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n, arr))
