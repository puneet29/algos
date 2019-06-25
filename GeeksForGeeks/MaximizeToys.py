# Problem Description: https://practice.geeksforgeeks.org/problems/maximize-toys/0

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()

    count = 0
    i = 0
    while(k > 0 and i < n):
        if(a[i]+count < k):
            k -= a[i]
            count += 1
        else:
            break
        i += 1

    print(count)
