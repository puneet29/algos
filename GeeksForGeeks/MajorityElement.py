# Problem Description: https://practice.geeksforgeeks.org/problems/majority-element/0

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    freq = {}
    res = -1

    for i in range(n):
        curr = arr[i]
        if(curr in freq):
            freq[curr] += 1
        else:
            freq[curr] = 1

    for item, value in freq.items():
        if(value > n/2):
            res = item
            break
    print(res)
