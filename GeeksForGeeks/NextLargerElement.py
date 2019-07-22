# Problem Description: https://practice.geeksforgeeks.org/problems/next-larger-element/0

def getNextLarger(a, n):
    res = [-1 for i in range(n)]
    for i in reversed(range(n-1)):
        j = i + 1
        while(j < n-1 and a[i] > a[j] and a[i] > res[j]):
            j += 1
        if(a[i] < a[j]):
            res[i] = a[j]
        elif(a[i] < res[j]):
            res[i] = res[j]

    print(' '.join(map(str, res)))


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    getNextLarger(a, n)
