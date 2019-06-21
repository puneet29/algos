# Problem Description: https://practice.geeksforgeeks.org/problems/twice-counter/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = [x for x in input().split()]
    freq = {}

    for i in range(n):
        if(a[i] in freq):
            freq[a[i]] += 1
        else:
            freq[a[i]] = 1

    count = 0
    for key, value in freq.items():
        if(value == 2):
            count += 1

    print(count)
