# Problem Description: https://practice.geeksforgeeks.org/problems/kth-smallest-element/0

def kthSmallest(a, n, k):
    maxEle = max(a)

    h = [0 for i in range(maxEle+1)]

    for i in range(n):
        h[a[i]] += 1

    for i in range(1, maxEle+1):
        if(h[i] >= 1):
            k -= 1
        if(k == 0):
            print(i)
            break


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    k = int(input())
    kthSmallest(a, n, k)
