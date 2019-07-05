# Problem Description: https://practice.geeksforgeeks.org/problems/relative-sorting/0

t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    d = {}
    output = []

    for i in range(n):
        if(a[i] in d):
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    for i in range(m):
        if(b[i] in d):
            for j in range(d[b[i]]):
                output.append(b[i])
            del d[b[i]]

    temp = []
    for k, v in d.items():
        for i in range(v):
            temp.append(k)
    temp.sort()
    output += temp

    print(' '.join([str(x) for x in output]))
