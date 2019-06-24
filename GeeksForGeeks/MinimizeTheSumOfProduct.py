# Problem Description: https://practice.geeksforgeeks.org/problems/minimize-the-sum-of-product/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    a.sort()
    b.sort(reverse=True)
    total = 0

    for i in range(n):
        total += a[i] * b[i]

    print(total)
