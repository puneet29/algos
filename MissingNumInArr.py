# Problem Description: https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]

    total = n * (n+1) // 2

    print(total - sum(arr))
