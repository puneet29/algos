# Problem Description: https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    leaders = []
    prev = arr[-1]

    for i in reversed(range(n)):
        if(arr[i] >= prev):
            prev = arr[i]
            leaders.append(str(prev))

    print(" ".join(reversed(leaders)))
